from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации."""

    # Локаторы
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    def open(self):
        """Открывает страницу авторизации."""
        super().open("https://stellarburgers.education-services.ru/login")
        return self

    def login(self, email: str, password: str):
        """Авторизует пользователя."""
        self.find(self.EMAIL_INPUT).send_keys(email)
        self.find(self.PASSWORD_INPUT).send_keys(password)
        self.click(self.LOGIN_BUTTON)
        return self