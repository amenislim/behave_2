from behave import *
from selenium import webdriver
from numpy.testing import assert_equal
from selenium.webdriver import ActionChains


#@given(u':the user navigate in ur')
#def step_open(context):
    #context.browser.get("https://qavbox.github.io/demo/dragndrop/")

@when(u'the user slide the bar until he get a percentage')
def slidebar(context):
    context.dd.slider()


@then(u'he sees a percentage under the bar')
def step_verif(context):
    assert_equal(context.dd.verif_slider(),"100")
