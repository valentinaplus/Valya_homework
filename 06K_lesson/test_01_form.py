import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    yield driver
    driver.quit()


def get_border_color(element):
    return element.value_of_css_property('border-color')


def test_form_validation(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CLASS_NAME, "btn").click()

    zip_code = driver.find_element(By.ID, "zip-code")
    wait.until(lambda d: "alert-danger" in zip_code.get_attribute("class"))

    zip_color = get_border_color(zip_code)
    assert zip_color in ["#f5c2c7", "rgb(245, 194, 199)"], (
        f"Zip code color is {zip_color}, expected red"
    )

    green_expected = ["rgb(0, 128, 0)", "rgb(186, 219, 204)"]

    other_fields_ids = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"
    ]

    for fid in other_fields_ids:
        field = driver.find_element(By.ID, fid)
        color = get_border_color(field)
        assert color in green_expected, (
            f"Field {fid} color is {color}, expected green"
        )

    print("Все проверки пройдены успешно!")
