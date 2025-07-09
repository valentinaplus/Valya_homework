import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    options = Options()
    service = FirefoxService()
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()


def test_shop_flow(driver):
    wait = WebDriverWait(driver, 5)

    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located(
        (By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    products_to_add = [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]
    for product_id in products_to_add:
        wait.until(EC.element_to_be_clickable((By.ID, product_id))).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    wait.until(EC.visibility_of_element_located(
        (By.ID, "first-name"))).send_keys("Valentina")
    driver.find_element(By.ID, "last-name").send_keys("Plyusnina")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    total_text = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "summary_total_label"))).text
    total_value = total_text.split("$")[-1]

    assert total_value == "58.29", (
        f"Expected total 58.29, but got {total_value}"
    )
