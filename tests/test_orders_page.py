import time

from pages.main_page import MainPage
from pages.orders_page import OrdersPage
from pages.login_page import LoginPage


class TestOrdersPage:
    """Тесты раздела «Лента заказов»."""

    def _login(self, driver, user):
        """Хелпер для логина."""
        login_page = LoginPage(driver).open()
        login_page.login(user["email"], user["password"])
        time.sleep(2)

    def _create_order(self, driver):
        """Хелпер для создания заказа."""
        main_page = MainPage(driver).open()
        main_page.add_ingredient_to_order()
        main_page.click_order_button()
        time.sleep(3)

    def test_total_orders_increases(self, driver, registered_user):
        """При создании нового заказа счётчик «Выполнено за всё время» увеличивается."""
        self._login(driver, registered_user)

        orders_page = OrdersPage(driver).open()
        total_before = orders_page.get_total_orders()

        self._create_order(driver)

        orders_page.open()
        time.sleep(2)
        total_after = orders_page.get_total_orders()

        assert total_after > total_before

    def test_today_orders_increases(self, driver, registered_user):
        """При создании нового заказа счётчик «Выполнено за сегодня» увеличивается."""
        self._login(driver, registered_user)

        orders_page = OrdersPage(driver).open()
        today_before = orders_page.get_today_orders()

        self._create_order(driver)

        orders_page.open()
        time.sleep(2)
        today_after = orders_page.get_today_orders()

        assert today_after > today_before

    def test_order_number_in_progress(self, driver, registered_user):
        """После оформления заказа его номер появляется в разделе «В работе»."""
        self._login(driver, registered_user)

        self._create_order(driver)

        orders_page = OrdersPage(driver).open()
        time.sleep(3)
        orders_in_progress = orders_page.get_orders_in_progress()

        assert len(orders_in_progress) > 0