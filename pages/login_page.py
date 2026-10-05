import allure

from locators.login_locators import LoginLocators
from pages.base_page import BasePage
from helpers.urls import LOGIN_PAGE


class LoginPage(BasePage):
    """Страница авторизации."""

    @allure.step("Открыть страницу авторизации")
    def open(self):
        """Открывает страницу авторизации."""
        super().open(LOGIN_PAGE)

    @allure.step("Авторизоваться пользователем {email}")
    def login(self, email: str, password: str):
        """Авторизует пользователя."""
        self.find(LoginLocators.EMAIL_INPUT).send_keys(email)
        self.find(LoginLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginLocators.LOGIN_BUTTON)