import unittest
from time import gmtime, strftime

import os, sys
test_folder_abs_path=os.path.abspath("..")
sys.path.append(test_folder_abs_path)

from test_data import test_data_dict
data = test_data_dict.data
from fixtures     import common_fixture
from page_objects import page
from page_objects import locators
from helpers      import common_helper as helper

class SendMailTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        common_fixture.create_common_fixture(cls)

    def test_login_on_main_page(self):
        main_page = page.MainPage(self.driver)
        main_page.login(data['users']['sender'])
        helper.wait_until_present(self.driver, locators.InboxPageLocators.COMPOSE_BUTTON)
        assert (data["urlMarkers"]["inbox"] in self.driver.current_url), "URL doesn't contain '/inbox'"

    def test_open_editor_from_inbox(self):
        inbox_page = page.InboxPage(self.driver)
        inbox_page.click_compose_button()
        helper.wait_until_present(self.driver, locators.ComposePageLocators.RECIPIENT_FIELD)
        assert data["urlMarkers"]["compose"] in self.driver.current_url, "URL doesn't contain '/compose'"

    def test_send_message(self):
        compose_page = page.ComposePage(self.driver)
        compose_page.type_recipient(data["users"]["recipient"]["email"])
        compose_page.type_subject("Test message " + strftime("%H%M%S", gmtime()))
        helper.switch_to_frame(self.driver, locators.ComposePageLocators.EDITOR_IFRAME)
        compose_page.type_message(data["messageText"])
        self.driver.switch_to.default_content()
        compose_page.click_send_button()
        helper.wait_until_visible(self.driver, locators.ComposePageLocators.MESSAGE_SENT_LABEL)
        message_sent_text = helper.get_text(self.driver, locators.ComposePageLocators.MESSAGE_SENT_LABEL)
        self.assertEqual(message_sent_text,data["messageSentText"]), "Wrong text when message is sent"

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        
if __name__ == '__main__':
    unittest.main()