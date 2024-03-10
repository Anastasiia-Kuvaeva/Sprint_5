import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import configuration
import data
import locators
import time
@pytest.fixture
def authorization():
    # Фикстура авторизации
    def authorizationInner():
        # Открываем браузер
        driver = webdriver.Chrome()
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
        time.sleep(1)  # Ожидаем перехода на новую страницу
        return driver

    return authorizationInner