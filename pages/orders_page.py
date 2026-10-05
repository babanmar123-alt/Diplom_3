from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrdersPage(BasePage):
    """Страница «Лента заказов»."""

    # Локаторы
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")

    def open(self):
        """Открывает ленту заказов."""
        super().open("https://stellarburgers.education-services.ru/feed")
        return self

    def get_total_orders(self) -> int:
        """Возвращает счётчик «Выполнено за всё время»."""
        text = self.get_text(self.TOTAL_ORDERS_COUNTER)
        return int(text) if text else 0

    def get_today_orders(self) -> int:
        """Возвращает счётчик «Выполнено за сегодня»."""
        text = self.get_text(self.TODAY_ORDERS_COUNTER)
        return int(text) if text else 0

    def get_orders_in_progress(self) -> list:
        """Возвращает список номеров заказов в работе."""
        elements = self.find_all(self.ORDERS_IN_PROGRESS)
        return [el.text for el in elements]