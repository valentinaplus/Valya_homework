from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def press_button(self, symbol):
        button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH,
    f'//span[text()="{symbol}"]')
            )
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        self.driver.execute_script("arguments[0].click();", button)


    def get_result(self, previous_text):
        self.wait.until(
            lambda driver: driver.find_element(By.CSS_SELECTOR, ".screen").text != previous_text)
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text



