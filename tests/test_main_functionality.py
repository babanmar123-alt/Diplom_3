import allure
import pytest

from pages.main_page import MainPage


@allure.feature("Основная функциональность")
class TestMainFunctionality:
    """Тесты основной функциональности."""

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        """Переход по клику на «Конструктор»."""
        page = MainPage(driver)
        page.open()
        page.click_orders_feed()
        page.wait_for_url("feed")
        page.click_constructor()
        page.wait_for_url("stellarburgers")

        assert "stellarburgers" in page.get_current_url()

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_orders_feed(self, driver):
        """Переход по клику на «Лента заказов»."""
        page = MainPage(driver)
        page.open()
        page.click_orders_feed()
        page.wait_for_url("feed")

        assert "feed" in page.get_current_url()

    @allure.title("Клик на ингредиент открывает модальное окно")
    def test_click_ingredient_opens_modal(self, driver):
        """При клике на ингредиент появляется всплывающее окно с деталями."""
        page = MainPage(driver)
        page.open()
        page.click_ingredient()

        assert page.is_modal_visible()

    @allure.title("Модальное окно закрывается по крестику")
    def test_modal_closes_by_cross(self, driver):
        """Всплывающее окно закрывается кликом по крестику."""
        page = MainPage(driver)
        page.open()
        page.click_ingredient()
        page.close_modal()

        assert not page.is_modal_visible()

    @allure.title("Счётчик ингредиента увеличивается")
    def test_ingredient_counter_increases(self, driver):
        """При добавлении ингредиента в заказ счётчик увеличивается."""
        page = MainPage(driver)
        page.open()
        page.add_ingredient_to_order()

        assert page.get_ingredient_counter() >= 1