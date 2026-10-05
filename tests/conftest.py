import pytest
import requests
from selenium import webdriver

from helpers.data_generator import generate_user_data
from helpers.urls import API_REGISTER, API_USER


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    """Фикстура для запуска браузера Chrome или Firefox."""
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()


@pytest.fixture
def registered_user():
    """Создаёт уникального пользователя через API и удаляет после теста.

    ВАЖНО: без ассертов — только подготовка и очистка данных.
    """
    user_data = generate_user_data()

    response = requests.post(API_REGISTER, json=user_data)

    if response.status_code != 200:
        yield {"email": None, "password": None, "name": None, "token": None}
        return

    token = response.json().get("accessToken")

    yield {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"],
        "token": token
    }

    if token:
        requests.delete(API_USER, headers={"Authorization": token})