# This documentation was used as guidelines for page objects implementation:
# http://selenium-python.readthedocs.io/page-objects.html

from . import locators
from helpers import common_helper as helper

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def login(self, user):
        self.type_login(user["email"])
        self.type_password(user["password"])
        self.click_login_button()

    def click_login_button(self):
        helper.click(self.driver, *locators.MainPageLocators.LOGIN_BUTTON)

    def type_login(self, login):
        helper.send_keys(self.driver, login, *locators.MainPageLocators.EMAIL_FIELD)

    def type_password(self, password):
        helper.send_keys(self.driver, password, *locators.MainPageLocators.PASSWORD_FIELD)

class InboxPage(BasePage):

    def click_compose_button(self):
        helper.click_via_actions(self.driver, *locators.InboxPageLocators.COMPOSE_BUTTON)

class ComposePage(BasePage):

    def type_recepient(self, recepient):
        helper.send_keys(self.driver, recepient, *locators.ComposePageLocators.RECEPIENT_FIELD)

    def type_subject(self, subject):
        helper.send_keys(self.driver, subject, *locators.ComposePageLocators.SUBJECT_FIELD)

    def type_message(self, message):
        helper.send_keys(self.driver, message, *locators.ComposePageLocators.MESSAGE_EDITOR)

    def click_send_button(self):
        helper.click(self.driver, *locators.ComposePageLocators.SEND_BUTTON)