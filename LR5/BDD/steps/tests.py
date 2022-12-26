from lab_5.field import field
from json import loads as load_jstr
from behave import *


@given('a goods list')
def given_a_list(context):
    context.list = load_jstr(context.text)


@given("fields #1 {f1} and #2 {f2}")
def given_a_fields(context, f1: {str}, f2: {str}):
    context.F1 = f1
    context.F2 = f2


@given("fields #1 {f1}")
def given_a_field(context, f1: {str}):
    context.F1 = f1
    context.F2 = None


@when('we call function with that data we get result')
def func_call(context):
    if context.F2 is not None:
        context.data = tuple(i for i in field(context.list, context.F1, context.F2))
        return
    context.data = tuple(i for i in field(context.list, context.F1))


@Then("we can assert this data with the tuple")
def check_data(context):
    assert context.data == tuple(load_jstr(context.text))
