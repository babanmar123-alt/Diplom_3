import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):
    """Главная страница (Конструктор)."""

    # Локаторы
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_ITEM = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")

    def open(self):
        """Открывает главную страницу."""
        super().open("https://stellarburgers.education-services.ru/")
        return self

    def click_constructor(self):
        """Кликает на «Конструктор»."""
        self.click(self.CONSTRUCTOR_BUTTON)
        return self

    def click_orders_feed(self):
        """Кликает на «Лента Заказов»."""
        self.click(self.ORDERS_FEED_BUTTON)
        return self

    def click_ingredient(self):
        """Кликает на первый ингредиент."""
        self.click(self.INGREDIENT_ITEM)
        return self

    def is_modal_visible(self) -> bool:
        """Проверяет, видно ли модальное окно."""
        return self.is_visible(self.MODAL_WINDOW)

    def close_modal(self):
        """Закрывает модальное окно."""
        self.click(self.MODAL_CLOSE_BUTTON)
        self.wait_for_invisibility(self.MODAL_WINDOW)
        return self

    def get_ingredient_counter(self) -> int:
        """Возвращает значение счётчика ингредиента."""
        text = self.get_text(self.INGREDIENT_COUNTER)
        return int(text) if text else 0

    def add_ingredient_to_order(self):
        """Добавляет ингредиент в заказ (drag-and-drop)."""
        ingredient = self.find(self.INGREDIENT_ITEM)
        basket = self.find(self.BASKET)

        # JS drag-and-drop
        self.driver.execute_script("""
            function createEvent(typeOfEvent) {
                var event = document.createEvent("CustomEvent");
                event.initCustomEvent(typeOfEvent, true, true, null);
                event.dataTransfer = {
                    data: {},
                    setData: function(key, value) { this.data[key] = value; },
                    getData: function(key) { return this.data[key]; }
                };
                return event;
            }
            function dispatchEvent(element, event, transferData) {
                if (transferData !== undefined) {
                    event.dataTransfer = transferData;
                }
                element.dispatchEvent(event);
            }
            var source = arguments[0];
            var target = arguments[1];
            var dragStartEvent = createEvent('dragstart');
            dispatchEvent(source, dragStartEvent);
            var dropEvent = createEvent('drop');
            dispatchEvent(target, dropEvent, dragStartEvent.dataTransfer);
            var dragEndEvent = createEvent('dragend');
            dispatchEvent(source, dragEndEvent, dragStartEvent.dataTransfer);
        """, ingredient, basket)

        time.sleep(1)

    def click_order_button(self):
        """Кликает на «Оформить заказ»."""
        self.click(self.ORDER_BUTTON)
        return self

    def get_order_number(self) -> str:
        """Возвращает номер оформленного заказа."""
        self.wait.until(EC.visibility_of_element_located(self.ORDER_NUMBER))
        return self.get_text(self.ORDER_NUMBER)