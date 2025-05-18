from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # Locators
    EMAIL_INPUT = (By.NAME, "emailLogin")
    PASSWORD_INPUT = (By.NAME, "senhaLogin")
    LOGIN_BUTTON = (By.XPATH, "//button[@onclick='logar()']")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://frontend.provaqa.planettech.com.br/"

    def navigate(self):
        self.driver.get(self.url)

    def login(self, email, password):
        self.input_text(*self.EMAIL_INPUT, email)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)
