from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def fill_first_name(self, first_name):
        elem = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "first-name")))
        elem.clear()
        elem.send_keys(first_name)

    def fill_last_name(self, last_name):
        elem = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "last-name")))
        elem.clear()
        elem.send_keys(last_name)

    def fill_postal_code(self, postal_code):
        elem = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "postal-code")))
        elem.clear()
        elem.send_keys(postal_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "continue"))).click()

    def fill_form_and_continue(self, first_name, last_name, postal_code):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_postal_code(postal_code)
        self.click_continue()

