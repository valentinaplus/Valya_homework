from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        """ Инициализирует объект страницы логина. Аргументы:
        driver (WebDriver):
        Драйвер Selenium для взаимодействия с браузером. """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> None:
        """ Открывает страницу логина. """
        self.driver.get(self.URL)

    def enter_username(self, username: str) -> None:
        """Вводит имя пользователя в поле. Аргумент:
        username (str): Имя пользователя. """
        username_input = self.wait.until(EC.visibility_of_element_located((
            By.ID, "user-name")))
        username_input.clear()
        username_input.send_keys(username)

    def enter_password(self, password: str) -> None:
        """ Вводит пароль в соответствующее поле. Аргумент:
        password (str): Пароль пользователя. """
        password_input = self.driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self) -> None:
        """Нажимает кнопку "Log In". """
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def login(self, username: str, password: str) -> None:
        """Выполняет полное действие логина:
        ввод имени пользователя и пароля, нажимает кнопку "Log In". Аргумент:
        username (str): Имя пользователя. password (str):
        Пароль пользователя."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
