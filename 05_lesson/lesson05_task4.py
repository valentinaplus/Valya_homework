from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

try:
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(3)

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("tomsmith")
    password_input.send_keys("SuperSecretPassword!")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(3)

    success_message = driver.find_element(By.CSS_SELECTOR, "div.flash.success")

    print(success_message.text.strip())

    time.sleep(2)
finally:
    driver.quit()
