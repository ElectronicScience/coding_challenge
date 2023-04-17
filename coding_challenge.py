import json
from utils import ResponseCodes
from utils import is_uuid_valid
from urllib.request import urlopen
from urllib.error import URLError, HTTPError

url_prefix = "http://discovery.nationalarchives.gov.uk/API/records/v1/details/"


class CodingChallenge:

    """
    A class to handle the National Archives coding challenge. Gets data from
    National Archives API and displaying the record title,
    description, or citable reference.

    """

    def __init__(self) -> None:
        self.input_uuid = None
        self.output_json = None

    def get_user_input(self) -> bool:

        """
        Gets user input of a UUID and validates it.

        Returns:
            bool: True if the input is valid, False otherwise.
        """

        input_attempts = 3
        self.input_uuid = None

        while input_attempts > 0:
            temp_uuid = input(
                "Input Your ID (UUID), you "
                f"have {input_attempts} attempts left :"
                )
            input_attempts -= 1
            if is_uuid_valid(temp_uuid):
                self.input_uuid = temp_uuid
                print("Valid UUID, lets try and get the data")
                return True
            else:
                print("Invalid UUID, please try again")

        print("You ran out off input attempts, "
              "no record found, please try again ! ")

        return False

    def get_url_data(self) -> bool:

        """
        Get data from the National Archives API for the given UUID.

        Returns:
            bool: True if data is fetched successfully, False otherwise.
        """

        self.output_json = None
        url = url_prefix + self.input_uuid
        try:
            with urlopen(url) as response:
                try:
                    if response.code == ResponseCodes.pass_code.value:
                        body = response.read()
                        self.output_json = json.loads(body)
                        return True
                    elif response.code == ResponseCodes.fail_code.value:
                        return False
                except json.JSONDecodeError as e:
                    print(f"JSONDecodeError: {e.reason}")
                    return False
        except HTTPError as e:
            print(f"HTTPError: {e.reason}")
            return False
        except URLError as e:
            print(f"URLError: {e.reason}")
            return False

    def display_record_title(self):

        """
        Displays the record title, description,
        or citable reference for the given UUID.

        """

        is_user_input = self.get_user_input()

        if is_user_input:
            is_url_data = self.get_url_data()
        else:
            is_url_data = False

        if is_user_input and is_url_data:

            if self.output_json["title"] is not None:
                title = self.output_json["title"]
                print(f"Title is : {title}")
            elif self.output_json["title"] is None  \
                    and self.output_json["scopeContent"]["description"] \
                    is not None:
                description = self.output_json["scopeContent"]["description"]
                print(f"Description is : {description}")
            elif self.output_json["title"] is None  \
                and self.output_json["scopeContent"]["description"] is None \
                    and self.output_json["citableReference"] is not None:
                citableReference = self.output_json["citableReference"]
                print(f"citableReference is : {citableReference}")
            elif self.output_json["title"] is None  \
                and self.output_json["scopeContent"]["description"] is None \
                    and self.output_json["citableReference"] is None:
                print("not sufficient information")

        elif is_user_input is True and is_url_data is False:
            print("No record found, please try again ! ")
