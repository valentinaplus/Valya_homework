from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class OverviewPage:
    def __init__(self, driver: WebDriver, timeout: int = 10):
        """ Конструктор объекта страницы общего обзора заказа. Аргумент:
        driver (WebDriver): Веб-драйвер Selenium. timeout (int, optional):
        Таймаут ожидания элемента (секунды), по умолчанию 10. """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_total(self) -> str:
        """ Получает итоговую сумму заказа. Returns: str:
        Итоговая сумма заказа. """
        total_label = self.wait.until(EC.visibility_of_element_located((
            By.CLASS_NAME, "summary_total_label")))
        total_text = total_label.text
        return total_text.split("$")[-1].strip()
