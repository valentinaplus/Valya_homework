from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    PRODUCTS_IDS = {
        "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
    }

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def add_to_cart_by_name(self, product_name):
        product_id = self.PRODUCTS_IDS.get(product_name)
        if not  product_id:
            raise ValueError(f"Unknown product name: {product_name}")
        button = self.wait.until(EC.element_to_be_clickable(
            (By.ID, product_id)))
        button.click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
