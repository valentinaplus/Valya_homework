from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        """ Конструктор объекта страницы корзины. Аргумент:
        driver (WebDriver): Веб-драйвер Selenium. timeout (int, optional):
        Таймаут ожидания элемента (секунды), по умолчанию 10. """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_checkout(self) -> None:
        """ Нажимает кнопку "Check Out" на странице корзины """
        button = self.wait.until(EC.element_to_be_clickable((
            By.ID, "checkout")))
        button.click()
