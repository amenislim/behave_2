from selenium.webdriver import ActionChains

from browser import Browser

objecttodrag = "draggable"
objecttodrop = "droppable"

#browser (extends)bech nerihitou beha
#classe 3andi des attribut des classes
class dragndrop(Browser):

    def drag(self):
        element = self.driver.find_element_by_id(objecttodrag)
        target = self.driver.find_element_by_id(objecttodrop)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()
    def drog(self):
        target = self.driver.context.browser.find_element_by_id("droppable").text
        return target
    def slider(self):
        slider = self.driver.find_element_by_css_selector("form:nth-child(4) fieldset:nth-child(1) div.container:nth-child(2) div.slider1:nth-child(15) > input:nth-child(1)")
        ActionChains(self.driver).drag_and_drop_by_offset(slider,280,16).release().perform()
    def verif_slider(self):
        msg=self.driver.find_element_by_id("range").text
        return(msg)