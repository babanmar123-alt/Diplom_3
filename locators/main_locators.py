from selenium.webdriver.common.by import By


class MainLocators:
    """Локаторы главной страницы (Конструктор)."""

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDERS_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_ITEM = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    MODAL_WINDOW = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")
    BASKET = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")