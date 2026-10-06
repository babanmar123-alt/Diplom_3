import allure

from helpers.api_client import ApiClient
from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from pages.login_page import LoginPage


@allure.feature("Лента заказов")
class TestOrdersPage:
    """Тесты раздела «Лента заказов».

    Заказ создаётся через API (подготовка данных),
    проверки — через UI.
    """

    @allure.title("Счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_increases(self, driver, registered_user):
        """При создании нового заказа счётчик «Выполнено за всё время» увеличивается."""
        # Логин через UI
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(registered_user["email"], registered_user["password"])

        # Открываем ленту заказов и запоминаем счётчик
        orders_page = OrdersPage(driver)
        orders_page.open()
        total_before = orders_page.get_total_orders()

        # Создаём заказ через API
        api = ApiClient()
        token = api.login(registered_user["email"], registered_user["password"])
        api.create_order(token)

        # Обновляем страницу и проверяем счётчик
        orders_page.open()
        total_after = orders_page.get_total_orders()

        assert total_after > total_before

    @allure.title("Счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_increases(self, driver, registered_user):
        """При создании нового заказа счётчик «Выполнено за сегодня» увеличивается."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(registered_user["email"], registered_user["password"])

        orders_page = OrdersPage(driver)
        orders_page.open()
        today_before = orders_page.get_today_orders()

        api = ApiClient()
        token = api.login(registered_user["email"], registered_user["password"])
        api.create_order(token)

        orders_page.open()
        today_after = orders_page.get_today_orders()

        assert today_after > today_before

    @allure.title("Номер заказа появляется в разделе «В работе»")
    def test_order_number_in_progress(self, driver, registered_user):
        """После оформления заказа его номер появляется в разделе «В работе»."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(registered_user["email"], registered_user["password"])

        # Создаём заказ через API
        api = ApiClient()
        token = api.login(registered_user["email"], registered_user["password"])
        api.create_order(token)

        # Открываем ленту заказов
        orders_page = OrdersPage(driver)
        orders_page.open()
        orders_in_progress = orders_page.get_orders_in_progress()

        assert len(orders_in_progress) > 0
        
