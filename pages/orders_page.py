import allure

from locators.orders_locators import OrdersLocators
from pages.base_page import BasePage
from helpers.urls import ORDERS_FEED


class OrdersPage(BasePage):
    """Страница «Лента заказов»."""

    @allure.step("Открыть ленту заказов")
    def open(self):
        """Открывает ленту заказов."""
        super().open(ORDERS_FEED)

    @allure.step("Получить счётчик «Выполнено за всё время»")
    def get_total_orders(self) -> int:
        """Возвращает счётчик «Выполнено за всё время»."""
        text = self.get_text(OrdersLocators.TOTAL_ORDERS_COUNTER)
        return int(text) if text else 0

    @allure.step("Получить счётчик «Выполнено за сегодня»")
    def get_today_orders(self) -> int:
        """Возвращает счётчик «Выполнено за сегодня»."""
        text = self.get_text(OrdersLocators.TODAY_ORDERS_COUNTER)
        return int(text) if text else 0

    @allure.step("Получить список заказов в работе")
    def get_orders_in_progress(self) -> list:
        """Возвращает список номеров заказов в работе."""
        elements = self.find_all(OrdersLocators.ORDERS_IN_PROGRESS)
        return [el.text for el in elements]