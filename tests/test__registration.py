from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import configuration
import data
import locators
import pytest
from selenium.webdriver.common.by import By


class TestRegistration:

    # тетирование успешной регистрации
    @pytest.mark.usefixtures("driver")
    @pytest.mark.usefixtures("email")
    def tests_registration_positive(self, driver, email):
        # Открываем страницу
        driver.get(configuration.URL_REGISTER)
        # Находим поля на форме
        name_input = driver.find_element(By.XPATH, locators.NAME_INPUT)
        email_input = driver.find_element(By.XPATH, locators.EMAIL_INPUT)
        password_input = driver.find_element(By.XPATH, locators.PASSWORD_INPUT)
        submit_button = driver.find_element(By.XPATH, locators.SUBMIT_BUTTON)
        # Заполняем поля
        name_input.send_keys(data.USER_NAME)
        email_input.send_keys(email)
        password_input.send_keys(data.USER_PASSWORD)
        submit_button.click()
        # Ожидаем наличия кнопки "Войти" формы авторизации
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.LOGIN_FORM_SUBMIT_BUTTON))
        )
        # проверка перехода на нужную страницу
        assert driver.current_url == configuration.URL_LOGIN

    # тестирование неуспешной регистрации (некорректный пароль)
    @pytest.mark.usefixtures("driver")
    def tests_registration_negative(self, driver):
        # Открываем страницу
        driver.get(configuration.URL_REGISTER)
        # Находим поля на форме
        password_input = driver.find_element(By.XPATH, locators.PASSWORD_INPUT)
        submit_button = driver.find_element(By.XPATH, locators.SUBMIT_BUTTON)
        # Регистрация с некорректным паролем
        password_input.send_keys("123")
        submit_button.click()
        # Ожидаем наличия поля сообщения об ошибке
        password_error = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locators.ERROR_MESSAGE))
        )
        # Проверка наличие ошибки при вводе некорректного пароля. error.text должен быть равен "Некорректный пароль"
        assert password_error is not None and password_error.text == "Некорректный пароль"