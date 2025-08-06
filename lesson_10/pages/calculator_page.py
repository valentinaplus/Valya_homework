import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """ Класс для работы с калькулятором """

    # Адрес страницы калькулятора
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver) -> None:
        """
        Конструктор класса.
        :param driver: Экземпляр WebDriver для управления браузером
        :type driver: selenium.webdriver.remote.webdriver.Webdriver
        :return: None
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self) -> None:
        """
        Открыть страницу калькулятора.
        :return: None
        """
        with allure.step(f"Открыть страницу: {self.URL}"):
            self.driver.get(self.URL)

    def set_delay(self, seconds: int) -> None:
        """
        Установить задержку в калькуляторе.
        :param seconds: Кщличество секунд задержки.
        :return: None
        """
        with allure.step(f"Устфновить задержку: {seconds} секунд"):
            delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
            delay_input.clear()
            delay_input.send_keys(str(seconds))

    def press_button(self, symbol: str) -> None:
        """
        Нажать на кнопку с указанным символом на калькуляторе.
        :param symbol: Символ кнопки (цифра или оператор).
        :type symbol: str
        :return: None
        """
        with allure.step(f"Нажать кнопку '{symbol}'"):
            button = self.wait.until(
                EC.element_to_be_clickable((
                    By.XPATH, f'//span[text()="{symbol}"]')
                )
            )
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   button)
        self.driver.execute_script("arguments[0].click();", button)

    def get_result(self, previous_text: str) -> str:
        """
        Получить результат с экрана калькулятора, ожидая изменения текста.
        :param previous_text: Текст на экране до вычесления.
        :type previous_text: str
        :return: str
        """
        with allure.step("Ожидание обновления результата на экране"):
            self.wait.until(
                lambda driver: driver.find_element(
                    By.CSS_SELECTOR, ".screen").text != previous_text)
            result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
            allure.attach(result, name="Результат",
                          attachment_type=allure.attachment_type.TEXT)
            return result
