from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from numpy.testing import assert_equal

@given(u':the user navigate in ur')

def step_open(context):

    context.driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")
    driver = context.driver
    driver.get("https://qavbox.github.io/demo/dragndrop/")
    driver.maximize_window()

@when(u':he drag and drop the little square in the big square')
def dragndrop(context):
    driver = context.driver
    element =driver.find_element_by_id("draggable")
    target = driver.find_element_by_id("droppable")
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(element, target).perform()

@then(u'he sees a massage Dropped')
def step_verif(context):
    driver = context.driver
    target = driver.find_element_by_id("droppable")
    assert_equal("Dropped!", target.text)

