from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from config import find_elements_timeout as timeout

def click(driver, *element):
    wait(driver, timeout).until(lambda s: driver.find_element(*element)).click()

# Use in case selenium doesn't consider element is visible or clickable but it actually is
def click_via_actions(driver, *element):
    actions = ActionChains(driver)
    target = wait(driver, timeout).until(lambda s: driver.find_element(*element))
    actions.move_to_element(target).click().perform()

def send_keys(driver, text, *element):
    wait(driver, timeout).until(lambda s: driver.find_element(*element)).send_keys(text)

def wait_until_present(driver, element):
    wait(driver, timeout).until(EC.presence_of_element_located((element)))

def wait_until_visible(driver, element):
    wait(driver, timeout).until(EC.visibility_of_element_located((element)))

def switch_to_frame(driver, element):
    iframe = wait(driver, timeout).until(lambda s: driver.find_element(*element))
    driver.switch_to.frame(iframe)

def get_text(driver, element):
    web_element = wait(driver, timeout).until(lambda s: driver.find_element(*element))
    return web_element.text