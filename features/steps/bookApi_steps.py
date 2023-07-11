import requests
from behave import *
from api.payloads import *
from api.api_resources import *
from utilities.configurations import *


@given('the Book details which needs to be added to Library')
def step_impl(context):
    # Context parameter lives throughout the feature file execution
    context.url = get_config()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = add_book_payload("afdga", "12552")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payload, headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.book_id = response_json['ID']
    print(context.book_id)
    assert response_json["Msg"] == "successfully added"


@given("the Book details with {isbn} and {aisle}")
def step_impl(context, isbn, aisle):
    context.url = get_config()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payload = add_book_payload(isbn, aisle)