from pages.main_page import MainPage


class TestMainFunctionality:
    """Тесты основной функциональности."""

    def test_go_to_constructor(self, driver):
        """Переход по клику на «Конструктор»."""
        page = MainPage(driver).open()
        # Закрываем возможную модалку
        if page.is_modal_visible():
            page.close_modal()
        page.click_orders_feed()
        page.wait_for_url("feed")
        page.click_constructor()
        page.wait_for_url("stellarburgers")
        assert "stellarburgers" in driver.current_url

    def test_go_to_orders_feed(self, driver):
        """Переход по клику на «Лента заказов»."""
        page = MainPage(driver).open()
        # Закрываем возможную модалку
        if page.is_modal_visible():
            page.close_modal()
        page.click_orders_feed()
        page.wait_for_url("feed")
        assert "feed" in driver.current_url

    def test_click_ingredient_opens_modal(self, driver):
        """При клике на ингредиент появляется всплывающее окно с деталями."""
        page = MainPage(driver).open()
        page.click_ingredient()
        assert page.is_modal_visible()

    def test_modal_closes_by_cross(self, driver):
        """Всплывающее окно закрывается кликом по крестику."""
        page = MainPage(driver).open()
        page.click_ingredient()
        assert page.is_modal_visible()
        page.close_modal()
        assert not page.is_modal_visible()

    def test_ingredient_counter_increases(self, driver):
        """При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается."""
        page = MainPage(driver).open()
        page.add_ingredient_to_order()
        counter = page.get_ingredient_counter()
        assert counter >= 1