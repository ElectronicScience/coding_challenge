import unittest
import json
from coding_challenge import Coding_Challenge
from unittest.mock import patch


class TestCodingChallenge(unittest.TestCase):

    def setUp(self):
        self.coding_challenge = Coding_Challenge()
        self.test_record_found_result = self.test_record_found()

    def test_get_user_input_valid_uuid(self):
        with patch('builtins.input',
                   return_value='123e4567-e89b-12d3-a456-426614174000'):
            self.assertTrue(self.coding_challenge.get_user_input())
            self.assertEqual(self.coding_challenge.input_uuid,
                             '123e4567-e89b-12d3-a456-426614174000')

    def test_get_user_input_partially_invalid(self):
        with patch('builtins.input',
                   side_effect=['wrong_uuid',
                                '123e4567-e89b-12d3-a456-426614174000']):
            self.assertTrue(self.coding_challenge.get_user_input())
            self.assertEqual(self.coding_challenge.input_uuid,
                             '123e4567-e89b-12d3-a456-426614174000')

    def test_get_user_input_totally_invalid(self):
        with patch('builtins.input',
                   side_effect=['wrong_uuid',
                                'another_wrong_uuid',
                                'totally_wrong_uuid']):
            self.assertFalse(self.coding_challenge.get_user_input())
            self.assertEqual(self.coding_challenge.input_uuid, None)

    def test_record_not_found(self):
        with patch.object(
                self.coding_challenge,
                'get_url_data',
                return_value=False):
            self.output_json = None
            assert self.output_json is None

    def test_record_found(self):
        with patch.object(
                self.coding_challenge,
                'get_url_data',
                return_value=True):
            with open('./tests/data/test_data.json') as data:
                json_data = json.load(data)
                self.output_json = json_data
            assert self.output_json == json_data

    @unittest.skipUnless(
        condition=lambda self: self.test_record_found_result,
        reason="test record not found")
    def test_title(self):
        self.output_json["title"] = "Test title"
        result = self.display_record_title()
        self.assertEqual(result, self.output_json["title"])

    @unittest.skipUnless(
        condition=lambda self: self.test_record_found_result,
        reason="test record not found")
    def test_description(self):
        self.output_json["title"] = None
        self.output_json["scopeContent"]["description"] = "Test description"
        result = self.display_record_title()
        self.assertEqual(
            result,
            self.output_json["scopeContent"]["description"])

    @unittest.skipUnless(
        condition=lambda self: self.test_record_found_result,
        reason="test record not found")
    def test_citable_reference(self):
        self.output_json["title"] = None
        self.output_json["scopeContent"]["description"] = None
        self.output_json["citableReference"] = "Test citable reference"
        result = self.display_record_title()
        self.assertEqual(
            result,
            self.output_json["citableReference"])

    @unittest.skipUnless(
        condition=lambda self: self.test_record_found_result,
        reason="test record not found")
    def test_not_sufficient_information(self):
        self.output_json["title"] = None
        self.output_json["scopeContent"]["description"] = None
        self.output_json["citableReference"] = None
        result = self.display_record_title()
        self.assertEqual(
            result,
            "not sufficient information")

    def display_record_title(self):
        if self.output_json["title"] is not None:
            title = self.output_json["title"]
            return title
        elif self.output_json["title"] is None and \
                self.output_json["scopeContent"]["description"] \
                is not None:
            description = self.output_json["scopeContent"]["description"]
            return description
        elif self.output_json["title"] is None  \
            and self.output_json["scopeContent"]["description"] is None \
                and self.output_json["citableReference"] is not None:
            citableReference = self.output_json["citableReference"]
            return citableReference
        elif self.output_json["title"] is None  \
            and self.output_json["scopeContent"]["description"] is None \
                and self.output_json["citableReference"] is None:
            return "not sufficient information"
