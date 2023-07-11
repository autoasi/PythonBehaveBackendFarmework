import requests
from behave import *
from api.api_resources import *
from utilities.configurations import *


@given('I have github auth credentials with invalid password')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = auth = ('autoasi', get_api_password())


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)