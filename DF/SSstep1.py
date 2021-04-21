from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver

def capture():
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
    webdriver = seleniumlib.driver

    S = lambda X: webdriver.execute_script('return document.body.parentNode.scroll' + X)
    webdriver.set_window_size(S('Width'), S('Height'))  # May need manual adjustment

    webdriver.find_element_by_tag_name('body').screenshot('image_name.png')
    # capturing body tag gives full page screenshot
    #body_tag = webdriver.find_element_by_tag_name('body')
    #body_tag.screenshot('image_name.png')