from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")

button = driver.find_element(By.ID, "updatingButton")
button.click()

wait = WebDriverWait(driver, 20)
wait.until(EC.text_to_be_present_in_element((By.ID, "updatingButton"),
                                            "SkyPro"))

button_text = driver.find_element(By.ID, "updatingButton").text
print(button_text)

driver.quit()
