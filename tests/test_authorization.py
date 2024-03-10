import time
import pytest
import configuration
import data
import locators
from selenium import webdriver
from selenium.webdriver.common.by import By

# тестирование успешного входа
# - вход по кнопке «Войти в аккаунт» на главной
# - вход через кнопку «Личный кабинет»
# - вход через кнопку в форме регистрации
# - вход через кнопку в форме восстановления пароля
@pytest.mark.parametrize("selector, url", [
    (locators.ACCOUNT_BUTTON, configuration.URL_SERVICE),
    (locators.PROFILE_BUTTON, configuration.URL_SERVICE),
    (locators.REGISTER_BUTTON, configuration.URL_REGISTER),
    (locators.FORGOT_PASSWORD_BUTTON, configuration.URL_FORGOT_PASSWORD)
])
def tests_authorization_positive(selector, url):
    # Открываем браузер
    driver = webdriver.Chrome()
    # Открываем страницу
    driver.get(url)
    # вход по кнопке «Войти в аккаунт» на главной
    driver.find_element(By.XPATH, selector).click()
    time.sleep(1)
    # проверяем, что мы на странице авторизации
    assert driver.current_url == configuration.URL_LOGIN
    # получение полей формы авторизации
    email_input = driver.find_element(By.XPATH, locators.LOGIN_FORM_EMAIL_INPUT)
    password_input = driver.find_element(By.XPATH, locators.LOGIN_FORM_PASSWORD_INPUT)
    submit_button = driver.find_element(By.XPATH, locators.LOGIN_FORM_SUBMIT_BUTTON)
    # заполнение полей формы авторизации
    email_input.send_keys(data.USER_EMAIL)
    password_input.send_keys(data.USER_PASSWORD)
    submit_button.click()
    time.sleep(3)
    # переходим на страницу профиля
    driver.get(configuration.URL_ACCOUNT)
    time.sleep(2)  # Ожидаем перехода на новую страницу
    # проверка перехода на /account/profile
    assert driver.current_url == configuration.URL_ACCOUNT_PROFILE
    driver.quit()