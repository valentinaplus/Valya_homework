import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    """Инициализация и завершение сеанса Selenium. :yeld: Объект
    драйвера. """
    options = Options()
    options.add_argument("--headless")
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@allure.title("Тест медленного калькулятора")
@allure.description("Проверяет работу калькулятора с заданной задержкой")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.NORMAL)
def test_slow_calculator(driver):
    """Тест проверяет правильность работы калькулятора с долгими расчетами. """
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)

    with allure.step("Ввод первого числа (7)"):
        page.press_button("7")

    with allure.step("Выбор оператора (+)"):
        page.press_button("+")

    with allure.step("Ввод второго числа (8)"):
        page.press_button("8")

    previous_text = page.get_result("")

    with allure.step("Начало вычесления (нажатие '=')"):
        page.press_button("=")

    result = page.get_result(previous_text)

    with allure.step("Проверка результата (должно быть 15)"):
        assert result == "15", (
            f"Неправильный результат расчёта: ожидается 15, получено {result}")
