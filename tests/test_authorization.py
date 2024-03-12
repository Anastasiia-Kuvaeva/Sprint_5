import pytest
import configuration
import data
import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestAuthorization:

    # Тестирование успешного входа
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
    @pytest.mark.usefixtures("driver")
    def tests_authorization_positive(self, selector, url, driver):
        # Открываем страницу
        driver.get(url)
        # кликаем по нужному элементу для перехода на страницу авторизации
        driver.find_element(By.XPATH, selector).click()
        # Ожидаем наличия кнопки "Войти" формы авторизации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.LOGIN_FORM_SUBMIT_BUTTON))
        )
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
        # Ожидаем наличия кнопки "Оформить заказ" на главной странице
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.CHECKOUT_BUTTON))
        )
        # переходим на страницу профиля
        driver.get(configuration.URL_ACCOUNT)
        # Ожидаем наличия кнопки "Выход" в профиле
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PROFILE_LOGOUT))
        )
        # проверка перехода на /account/profile
        assert driver.current_url == configuration.URL_ACCOUNT_PROFILE
