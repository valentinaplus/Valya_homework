from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
sleep(2)
blue_button.click()
sleep(3)
