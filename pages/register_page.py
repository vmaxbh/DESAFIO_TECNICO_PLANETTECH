from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegisterPage(BasePage):
    # Locators
    NAME_INPUT = (By.NAME, "nome")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "senha")
    CONFIRM_PASSWORD_INPUT = (By.NAME, "confirmarSenha")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Cadastrar')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://frontend.provaqa.planettech.com.br/"

    def navigate(self):
        self.driver.get(self.url)

    def register(self, name, email, password, confirm_password):
        self.input_text(*self.NAME_INPUT, name)
        self.input_text(*self.EMAIL_INPUT, email)
        self.input_text(*self.PASSWORD_INPUT, password)
        self.input_text(*self.CONFIRM_PASSWORD_INPUT, confirm_password)
        self.click(*self.REGISTER_BUTTON)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)
