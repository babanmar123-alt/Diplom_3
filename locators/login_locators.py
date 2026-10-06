from selenium.webdriver.common.by import By


class LoginLocators:
    """Локаторы страницы авторизации."""

    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")