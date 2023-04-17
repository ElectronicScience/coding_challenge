# National Archives API Coding Challenge
This is a Python script project that fetches data from the National Archives API using a given record ID (UUID) and displays the record title, description, or citable reference in return.
## Prerequisites
- Python 3.6 or higher
## Create a virtual environment (recommended)
Before running the script, setting up a virtual environment to manage the project's dependencies is recommended.

### Ubuntu
1.	Install the Python virtualenv package if you haven't already:

```
sudo apt-get install python3-venv
```
2.	Navigate to the project folder and create a virtual environment:
```
python3 -m venv env
```
3.	Activate the virtual environment:
```
source env/bin/activate
```
### Windows
1.	Navigate to the project folder and create a virtual environment:
```
python -m venv env
```
2.	Activate the virtual environment:
```
.\env\Scripts\activate
```
## Installing dependencies (required)
1.	Ensure that the virtual environment if installed is activated.
2.	Install the required dependencies from the requirements.txt file:
```
pip install -r requirements.txt
```
## How to build the code
No build process is required for this project, as it is a standalone Python script. However, creating and activating a virtual environment is recommended before running it.
## How to run the output
1. Clone this repository or download the project files.
2. Open a terminal/command prompt and navigate to the project folder.
3. Create and Activate the virtual environment. (Recommended but not required)
4. Install dependencies
5. Run the script using the following command:

For Both windows and Linux-based systems:

**Tip: Run from with in the src folder**

```
python coding_challenge_run.py
```
## How to run tests

**Tip: Run from with in the src folder**

```
python -m unittest ./tests/test_coding_challenge.py
```
# Assumptions
1. The user will provide a valid UUID.
2. The National Archives API will return JSON data.
3. The API will be available and accessible when the script is run.
4. The audience downloading this code is technical
5. Have an understanding of environments like VS Code, VS Studio or PyCharm etc

# Additional Notes
1. The script makes use of the urllib library for handling API requests and the json library for parsing JSON data.
2. The project includes a utils.py file which contains utility functions and classes, such as ResponseCodes for handling HTTP status codes and is_uuid_valid for UUID validation.
3. The script gives 3 chances to input a valid ID in the form of a UUID, run the script multiple times to input different UUID's and get different results.
