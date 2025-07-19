import pytest
from pages.calculator_page import CalculatorPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay(45)

    page.press_button("7")
    page.press_button("+")
    page.press_button("8")

    previous_text = page.get_result("")

    page.press_button("=")

    result = page.get_result(previous_text)
    assert result == "15"

