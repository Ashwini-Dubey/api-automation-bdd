# **Core Components of the BDD Stack**

* Language: Depends on your project’s primary programming language (e.g., Python, Java, JavaScript, Ruby, etc.).
* BDD Framework: For writing Gherkin-style feature files and automating them.
* Test Runner: To execute the automated test cases.
* Assertion Library: For validating test results.
* Report Generator: For generating detailed test reports.
* Integration Tools: For CI/CD pipelines and collaboration.

Python Tech Stack
    
* **Language:** Python.
* **BDD Framework:** Behave.
* **Test Runner:** Behave built-in runner or pytest for advanced features.
* **Assertion Library:** Python's built-in assert or external libraries like pytest.
* **Report Generator:** Plugins like allure-behave for Allure reports.
* **Integration Tools:**
  * **Continuous Integration:** Jenkins, GitHub Actions, GitLab CI/CD
  * **Version Control:** Git
  * **Collaboration:** JIRA (for linking Gherkin features to requirements)

## Prerequisites
- Python 3.x
- `pytest`, `Behave`, `requests`, `json`, `openpyxl`, etc.

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Ashwini-Dubey/api-automation-bdd.git
    cd api-automation-bdd
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the tests:
    ```bash
    behave
    ```

## Folder Structure
api-automation-bdd/ │ ├── features/ │ ├── steps/ │ └── api.feature │ ├── tests/ │ ├── api_test.py │ ├── requirements.txt └── README.md


## Example Test Case

In the `features/api.feature` file, define the BDD scenario:

```gherkin
Feature: Testing API endpoints

  Scenario: Verify the status of a GET request
    Given the API endpoint is "https://jsonplaceholder.typicode.com/posts/1"
    When I send a GET request
    Then the response status code should be 200
```

In features/steps/api_steps.py, write the steps to implement the scenario:

```python
from behave import given, when, then
import requests

@given('the API endpoint is "{url}"')
def step_impl(context, url):
    context.url = url

@when('I send a GET request')
def step_impl(context):
    context.response = requests.get(context.url)

@then('the response status code should be {status_code}')
def step_impl(context, status_code):
    assert context.response.status_code == int(status_code), f"Expected {status_code}, but got {context.response.status_code}"
```
