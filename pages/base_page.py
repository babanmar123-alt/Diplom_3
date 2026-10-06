from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех Page Object."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open(self, url: str):
        """Открывает страницу по URL."""
        self.driver.get(url)

    def find(self, locator: tuple):
        """Находит элемент на странице."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator: tuple):
        """Находит кликабельный элемент."""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def find_all(self, locator: tuple):
        """Находит все элементы по локатору."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator: tuple):
        """Кликает по элементу (через JS, если перекрыт)."""
        element = self.find_clickable(locator)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator: tuple) -> str:
        """Возвращает текст элемента."""
        return self.find(locator).text

    def is_visible(self, locator: tuple) -> bool:
        """Проверяет, виден ли элемент."""
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def wait_for_url(self, url_part: str):
        """Ждёт, пока URL не будет содержать указанную часть."""
        return self.wait.until(EC.url_contains(url_part))

    def wait_for_invisibility(self, locator: tuple):
        """Ждёт, пока элемент не станет невидимым."""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def get_current_url(self) -> str:
        """Возвращает текущий URL."""
        return self.driver.current_url

    def execute_script(self, script: str, *args):
        """Выполняет JS-скрипт (для drag-and-drop)."""
        return self.driver.execute_script(script, *args)
    
