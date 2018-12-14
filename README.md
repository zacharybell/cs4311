# ntbsg

## Installation
1. First make sure you have python3.6 installed and pip3.
2. Type 'python3 --version' and 'pip3 --version' to check installation.
3. Make sure you have pipenv installed. This is a tool that allows for easy dependency management.
4. To install 'pip3 install -U pipenv'
5. Clone this repo (git clone <repo_url>)
6. Install dependencies (pipenv install)

## Running Tests
Pipenv should have already installed pytest which is the package we are using to test. To run tests from the root directory 
type 'py.test' and this should run all the tests you need.

Add any additional tests into the 'tests' directory with the following name 'test_<module_name>.py'. Pytest should be able to 
locate any test files named with this convention.
