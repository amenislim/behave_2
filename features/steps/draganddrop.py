from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from numpy.testing import assert_equal


@given(u':the user navigate in ur')
def step_open(context):
    context.browser.get("https://qavbox.github.io/demo/dragndrop/")


@when(u':he drag and drop the little square in the big square')
def dragndrop(context):
    #methode drag n'a pas de variable a l'interieur
    context.dd.drag()

@then(u'he sees a massage Dropped')
def step_verif(context):
    #target = context.browser.find_element_by_id("droppable")
    context.dd.drog()
    assert_equal("Dropp", context.dd.drog.text)
