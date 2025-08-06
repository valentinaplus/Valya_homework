import allure
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
    """Инициализирует и закрывает экземпляр Webdriver."""
    options = Options()
    service = FirefoxService()
    driver = webdriver.Firefox(service=service, options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@allure.title("Полный цикл покупки товаров")
@allure.description(
    """Проверяет добавления товаров в корзину, оформление заказа и итоговую
    сумму."""
    )
@allure.feature("Покупка товаров")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_flow(driver):
    """Выполняет полный цикл покупок:
    авторизацию, выбор товаров, оформление заказа и проверка суммы."""
    login_page = LoginPage(driver)
    products_page = ProductsPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    overview_page = OverviewPage(driver)

    @allure.step("Авторизуемся на сайте")
    def perform_login():
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    @allure.step("Выбираем товары и добавляем их в корзину")
    def add_products_to_cart():
        products = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for product in products:
            products_page.add_to_cart_by_name(product)

    @allure.step("Переходим в корзину и переходим к оформлению заказа")
    def proceed_to_checkout():
        products_page.go_to_cart()
        cart_page.click_checkout()

    @allure.step("Оформляем заказ, заполняя форму доставки")
    def fill_delivery_form():
        checkout_page.fill_form_and_continue("Valentina", "Plyusnina", "12345")

    @allure.step("Получаем итоговую сумму заказа")
    def verify_total():
        total_str = overview_page.get_total()
        expected_total = "58.29"
        assert total_str == expected_total, \
            f"Ожидаемая сумма: {expected_total}, фактическая сумма: {
                total_str}"

    perform_login()
    add_products_to_cart()
    proceed_to_checkout()
    fill_delivery_form()
    verify_total()
