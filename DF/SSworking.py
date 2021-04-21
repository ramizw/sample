import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


cd = os.getcwd()
add = '\Browsers'
readypath = cd+add

os.environ['PATH'] = readypath

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

URL = 'https://pypi.org/project/robotframework-jsonvalidator/'

driver.get(URL)



S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

driver.quit()