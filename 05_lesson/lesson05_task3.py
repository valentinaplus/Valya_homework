from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.common.by import By

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)

    input_field = driver.find_element(By.TAG_NAME, "input")

    input_field.send_keys("Sky")
    time.sleep(2)

    input_field.clear()
    time.sleep(2)

    input_field.send_keys("Pro")
    time.sleep(2)

finally:
    driver.quit()
