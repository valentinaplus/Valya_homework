import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.overview_page import OverviewPage


@pytest.fixture
def driver():
    options = Options()
    service = FirefoxService()
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def test_shop_flow(driver):
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = OverviewPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for product in products:
        products_page.add_to_cart_by_name(product)

    products_page.go_to_cart()
    cart_page.click_checkout()

    checkout_page.fill_form_and_continue("Valentina", "Plyusnina", "12345")

    total_str = overview_page.get_total()

    assert total_str == "58.29"
