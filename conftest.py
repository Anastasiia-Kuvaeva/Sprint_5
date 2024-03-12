import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import configuration
import data
import locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", type=str)

# Фикстура получения и закрытия driver
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = None
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


# Фикстура генерации email
@pytest.fixture
def email():
    return "akuvaeva" + str(random.randint(1000, 9999)) + "@yandex.com"


# Фикстура авторизации
@pytest.fixture
def authorization(driver):
    # Открываем страницу
    driver.get(configuration.URL_LOGIN)
    # получение полей формы авторизации
    email_input = driver.find_element(By.XPATH, locators.LOGIN_FORM_EMAIL_INPUT)
    password_input = driver.find_element(By.XPATH, locators.LOGIN_FORM_PASSWORD_INPUT)
    submit_button = driver.find_element(By.XPATH, locators.LOGIN_FORM_SUBMIT_BUTTON)
    # заполнение полей формы авторизации
    email_input.send_keys(data.USER_EMAIL)
    password_input.send_keys(data.USER_PASSWORD)
    submit_button.click()
    # ожидаем перехода на новую страницу
    WebDriverWait(driver, 10).until(EC.staleness_of(submit_button))
