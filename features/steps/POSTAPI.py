from behave import *
import json
import requests

@given('User Details')
def step_impl(context):
    context.url = "https://dummyjson.com/auth/login"
    context.payload = json.dumps({
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30000
    })
    context.headers =  {
        "Content-Type": "application/json"
    }

@when('we execute the POST method to generate the access token')
def step_impl(context):
    context.response = requests.request("POST", context.url, headers=context.headers, data=context.payload)

@then('access token and refresh token is generated.')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"
    response_data = context.response.json()
    assert response_data['username'] == "emilys"
    print(response_data)