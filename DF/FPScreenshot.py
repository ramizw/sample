from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver

def capture_full_page_screenshot():
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    webdriver = seleniumlib.driver

    body_tag = webdriver.find_element_by_tag_name('body')
    body_tag.screenshot('image.png')