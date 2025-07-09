import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()


def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()="8"]').click()

    wait = WebDriverWait(driver, 60)
    equal_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="="]'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", equal_button)
    driver.execute_script("arguments[0].click();", equal_button)

    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), "15"))
    res = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert res == "15"
