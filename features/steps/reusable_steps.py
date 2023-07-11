from behave import *


@then('status code of response should be {status_code:d}')
def step_impl(context, status_code):
    print(context.response.status_code)
    assert context.response.status_code == status_code
