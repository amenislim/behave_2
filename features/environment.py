import os
from os import getcwd

from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from selenium import webdriver

from pages.dragndrop import dragndrop


def before_scenario(context,scenario):
    path=os.getcwd()
    print(path+"\drivers\chromedriver.exe")
    option=webdriver.ChromeOptions()
    #option.add_argument("--start-maximized")
    option.add_argument("headless")
    context.browser = webdriver.Chrome(executable_path=path+"\drivers\chromedriver.exe",chrome_options=option)
    #context.browser.maximize_window()
    #contenu du variable
    context.dd=dragndrop(context.browser)
def after_step(context,step):
        if step.status == "failed":
            context.browser.save_screenshot('c://b/screenshot.png')
            attach(
                context.browser.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=AttachmentType.PNG)
