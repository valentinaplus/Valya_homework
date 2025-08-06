from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        """ Конструктор объекта страницы оформления заказа. Аргумент:
        driver (WebDriver): Веб-драйвер Selenium. timeout (int, optional):
        Таймаут ожидания элемента (секунды), по умолчанию 10. """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def fill_first_name(self, first_name: str) -> None:
        """ Заполняет поле "First Name" на странице оформления заказа.
        Аргумент: first_name (str): Имя пользователя. """
        elem = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "first-name")))
        elem.clear()
        elem.send_keys(first_name)

    def fill_last_name(self, last_name: str) -> None:
        """ Заполняет поле "Last Name" на странице оформления заказа. Аргумент:
        last_name (str): Фамилия пользователя. """
        elem = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "last-name")))
        elem.clear()
        elem.send_keys(last_name)

    def fill_postal_code(self, postal_code: str) -> None:
        """ Заполняет поле "Postal Code" на странице оформления заказа.
        Аргумент: postal_code (str): Почтовый индекс. """
        elem = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "postal-code")))
        elem.clear()
        elem.send_keys(postal_code)

    def click_continue(self) -> None:
        """ Нажимает кнопку "Continue" на странице оформления заказа. """
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "continue"))).click()

    def fill_form_and_continue(self, first_name: str, last_name: str,
                               postal_code: str) -> None:
        """ Заполняет всю необходимую информацию и продолжает оформление
        заказа. Аргумент: first_name (str): Имя пользователя. last_name (str):
        Фамилия пользователя. postal_code (str): Почтовый индекс. """
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)
        self.click_continue()
