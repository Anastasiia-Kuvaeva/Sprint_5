import pytest
import configuration
import locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestProfile:

    # Тестирование переходов в личный кабинет по клику на «Личный кабинет»
    @pytest.mark.usefixtures("driver")
    @pytest.mark.usefixtures("authorization")
    def tests_go_to_profile_positive(self, driver, authorization):
        # переходим на главную страницу
        driver.get(configuration.URL_SERVICE)
        # Ожидаем наличия кнопки "Оформить заказ"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.CHECKOUT_BUTTON))
        )
        # кликаем по кнопке «Личный кабинет»
        driver.find_element(By.XPATH, locators.PROFILE_BUTTON).click()
        # Ожидаем наличия на странице кнопки "Выход"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PROFILE_LOGOUT))
        )
        # проверка перехода на нужную страницу
        assert driver.current_url == configuration.URL_ACCOUNT_PROFILE

    # Тестирование переходов из личного кабинета в конструктор
    @pytest.mark.usefixtures("driver")
    @pytest.mark.usefixtures("authorization")
    def tests_go_to_constructor_positive(self, driver, authorization):
        # переходим в личный кабинет
        driver.get(configuration.URL_ACCOUNT)
        # Ожидаем наличия кнопки "Выход"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PROFILE_LOGOUT))
        )
        # кликаем по кнопке «Конструктор»
        driver.find_element(By.XPATH, locators.PROFILE_CONSTRUCTOR).click()
        # Ожидаем наличия на странице кнопки "Оформить заказ"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.CHECKOUT_BUTTON))
        )
        # проверка перехода на нужную страницу
        assert driver.current_url == configuration.URL_SERVICE

    # Тестирование выхода из аккаунта
    @pytest.mark.usefixtures("driver")
    @pytest.mark.usefixtures("authorization")
    def tests_profile_logout_positive(self, driver, authorization):
        # переходим в личный кабинет
        driver.get(configuration.URL_ACCOUNT)
        # Ожидаем наличия кнопки "Выход"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.PROFILE_LOGOUT))
        )
        # кликаем по кнопке «Выход»
        driver.find_element(By.XPATH, locators.PROFILE_LOGOUT).click()
        # Ожидаем наличия на странице кнопки "Войти"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.LOGIN_FORM_SUBMIT_BUTTON))
        )
        # проверка перехода на нужную страницу
        assert driver.current_url == configuration.URL_LOGIN
