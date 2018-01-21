from selenium import webdriver
from config   import base_url

def create_common_fixture(object):
    object.driver = webdriver.Chrome()
    object.driver.maximize_window()
    object.driver.get(base_url)