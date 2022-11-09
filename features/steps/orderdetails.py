from behave import *
from Utilities.configreader import ConfigReader
from features.pageobject.order import order

@given(u'we navigate to flipkart')
def step_impl(context):
    context.order = order(context.driver)
    context.order.OpenPage(ConfigReader("base info", "URL"))

@then(u'close the popup')
def step_impl(context):
    context.order.clickclose()

@when(u'click login')
def step_impl(context):
    context.order.Click_loginhomepage()

@then(u'we type "{username1}" field')
def step_impl(context, username1):
    context.order.Enter_Username(username1)

@then(u'we type in "{password1}" the field')
def step_impl(context, password1):
    context.order.Enter_password(password1)

@then(u'we click on the sign in button')
def step_impl(context):
    context.order.Click_login()



@then(u'we over on profile')
def step_impl(context):
    context.order.over_to_profile()


@then(u'click on Orders')
def step_impl(context):
    context.order.Click_order()



@then(u'click on On the way')
def step_impl(context):
    context.order.Click_ontheway()

@then(u'click on Delivered')
def step_impl(context):
    context.order.Click_delivered()


@then(u'click on Cancelled')
def step_impl(context):
    context.order.Click_cancelled()


@then(u'click on Returned')
def step_impl(context):
    context.order.Click_Returned()


@then(u'click on Last 30 days')
def step_impl(context):
    context.order.Click_Last()


@then(u'click on 2022')
def step_impl(context):
    context.order.Click_2022()


@then(u'click on 2021')
def step_impl(context):
    context.order.Click_2021()

@then(u'click on 2020')
def step_impl(context):
    context.order.Click_2020()


@then(u'click on 2019')
def step_impl(context):
    context.order.Click_2019()



@then(u'click on older')
def step_impl(context):
    context.order.Click_older()






