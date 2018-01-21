from selenium.webdriver.common.by import By

class MainPageLocators:

    LOGIN_BUTTON   = (By.CSS_SELECTOR, '[id="auth"] [type="submit"]')

    EMAIL_FIELD    = (By.ID, 'mailbox:login')

    PASSWORD_FIELD = (By.ID, 'mailbox:password')

class InboxPageLocators:

    COMPOSE_BUTTON = (By.CSS_SELECTOR, '[class*="not-sticky"] [data-name="compose"]')

class ComposePageLocators:

    RECEPIENT_FIELD = (By.CSS_SELECTOR, 'textarea[data-original-name="To"]')

    SUBJECT_FIELD   = (By.NAME, 'Subject')

    EDITOR_IFRAME   = (By.CSS_SELECTOR, '[name*="composeEditor"]')

    MESSAGE_EDITOR  = (By.ID, 'tinymce')

    SEND_BUTTON     = (By.CSS_SELECTOR, '[id*="b-toolbar__right"] [data-name="send"]')

    MESSAGE_SENT_LABEL = (By.CSS_SELECTOR, '[class*="message-sent__title"]')


