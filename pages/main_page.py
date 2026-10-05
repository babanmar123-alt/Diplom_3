import allure

from locators.main_locators import MainLocators
from pages.base_page import BasePage
from helpers.urls import MAIN_PAGE


class MainPage(BasePage):
    """Главная страница (Конструктор)."""

    @allure.step("Открыть главную страницу")
    def open(self):
        """Открывает главную страницу."""
        super().open(MAIN_PAGE)

    @allure.step("Кликнуть на «Конструктор»")
    def click_constructor(self):
        """Кликает на «Конструктор»."""
        self.click(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на «Лента Заказов»")
    def click_orders_feed(self):
        """Кликает на «Лента Заказов»."""
        self.click(MainLocators.ORDERS_FEED_BUTTON)

    @allure.step("Кликнуть на первый ингредиент")
    def click_ingredient(self):
        """Кликает на первый ингредиент."""
        self.click(MainLocators.INGREDIENT_ITEM)

    @allure.step("Проверить, видно ли модальное окно")
    def is_modal_visible(self) -> bool:
        """Проверяет, видно ли модальное окно."""
        return self.is_visible(MainLocators.MODAL_WINDOW)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        """Закрывает модальное окно."""
        self.click(MainLocators.MODAL_CLOSE_BUTTON)
        self.wait_for_invisibility(MainLocators.MODAL_WINDOW)

    @allure.step("Получить счётчик ингредиента")
    def get_ingredient_counter(self) -> int:
        """Возвращает значение счётчика ингредиента."""
        try:
            text = self.get_text(MainLocators.INGREDIENT_COUNTER)
            return int(text) if text else 0
        except Exception:
            return 0

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self):
        """Добавляет ингредиент в заказ через JS drag-and-drop (DataTransfer)."""
        ingredient = self.find(MainLocators.INGREDIENT_ITEM)
        basket = self.find(MainLocators.BASKET)

        self.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var dataTransfer = new DataTransfer();

            var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragStartEvent);

            var dragEnterEvent = new DragEvent('dragenter', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dragEnterEvent);

            var dragOverEvent = new DragEvent('dragover', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dragOverEvent);

            var dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            target.dispatchEvent(dropEvent);

            var dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            source.dispatchEvent(dragEndEvent);
        """, ingredient, basket)

        # Ждём, пока счётчик станет >= 1
        self.wait.until(
            lambda d: int(d.find_element(*MainLocators.INGREDIENT_COUNTER).text or 0) >= 1
        )

    @allure.step("Кликнуть на «Оформить заказ»")
    def click_order_button(self):
        """Кликает на «Оформить заказ»."""
        self.click(MainLocators.ORDER_BUTTON)

    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self) -> str:
        """Возвращает номер оформленного заказа."""
        return self.get_text(MainLocators.ORDER_NUMBER)