from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://uitestingplayground.com/ajax")
driver.find_element(By.ID, "ajaxButton").click()

wait = WebDriverWait(driver, 20)
green_message = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bg-success"))
)

print(green_message.text.strip())

driver.quit()
