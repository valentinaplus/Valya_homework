from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def all_images_loaded(driver, images):
    for img in images:
        loaded = driver.execute_script(
            "return arguments[0].complete && "
            "typeof arguments[0].naturalWidth != 'undefined' && "
            "arguments[0].naturalWidth > 0", img
        )
        if not loaded:
            return False
    return True


service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 60)

    wait.until(lambda d: len(d.find_elements(By.TAG_NAME, "img")) >= 3)

    images = driver.find_elements(By.TAG_NAME, "img")
    print(f"Количество найденных изображений: {len(images)}")

    wait.until(lambda d: all_images_loaded(d, images))

    if len(images) >= 3:
        third_img_src = images[2].get_attribute("src")
        print("Src третьей картинки:", third_img_src)
    else:
        print("Третья картинка не найдена")

finally:
    driver.quit()
