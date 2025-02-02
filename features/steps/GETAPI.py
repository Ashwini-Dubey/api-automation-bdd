from behave import *
import json
import requests


@given(u'accessToken')
def step_impl(context):
    context.url = "https://dummyjson.com/auth/me"
    context.headers = {
        "Content-Type": "application/json",
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcm5hbWUiOiJlbWlseXMiLCJlbWFpbCI6ImVtaWx5LmpvaG5zb25AeC5kdW1teWpzb24uY29tIiwiZmlyc3ROYW1lIjoiRW1pbHkiLCJsYXN0TmFtZSI6IkpvaG5zb24iLCJnZW5kZXIiOiJmZW1hbGUiLCJpbWFnZSI6Imh0dHBzOi8vZHVtbXlqc29uLmNvbS9pY29uL2VtaWx5cy8xMjgiLCJpYXQiOjE3Mzg0MzI2NDQsImV4cCI6MTc0MDIzMjY0NH0.OisJZi8mcyxe-_ZZ5aXA4RC7lry188Yy_U6XEY_rGEM"
    }


@when(u'we execute the GET method to parse the CurrentAuthUser')
def step_impl(context):
    context.response = requests.get(context.url, headers=context.headers)


@then(u'CurrentAuthUser details are parsed')
def step_impl(context):
    assert context.response.status_code == 200, f"Expected status code 200, but got {context.response.status_code}"
    print(context.response.json())
    response_data = context.response.json()
    assert response_data['username'] == "emilys"
    print(response_data)