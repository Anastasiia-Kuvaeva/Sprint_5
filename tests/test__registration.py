import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import configuration
import data
import locators
from selenium import webdriver
from selenium.webdriver.common.by import By


# тетирование успешной регистрации
def tests_registration_positive():
    # Открываем браузер
    driver = webdriver.Chrome()
    # Открываем страницу
    driver.get(configuration.URL_REGISTER)
    # Находим и заполняем поля для успешной регистрации
    name_input = driver.find_element(By.XPATH, locators.NAME_INPUT)
    email_input = driver.find_element(By.XPATH, locators.EMAIL_INPUT)
    password_input = driver.find_element(By.XPATH, locators.PASSWORD_INPUT)
    submit_button = driver.find_element(By.XPATH, locators.SUBMIT_BUTTON)

    name_input.send_keys(data.USER_NAME)
    email_input.send_keys(data.USER_EMAIL)
    password_input.send_keys(data.USER_PASSWORD)
    submit_button.click()

    time.sleep(3)

    assert driver.current_url == configuration.URL_LOGIN

    driver.quit()


# тестирование неуспешной регистрации (некорректный пароль)
def tests_registration_negative():
     # Открываем браузер
     driver = webdriver.Chrome()
     # Открываем страницу
     driver.get(configuration.URL_REGISTER)
     # Находим и заполняем поля для успешной регистрации
     password_input = driver.find_element(By.XPATH, locators.PASSWORD_INPUT)
     submit_button = driver.find_element(By.XPATH, locators.SUBMIT_BUTTON)

     # Регистрация с некорректным паролем
     password_input.send_keys("123")
     submit_button.click()

     password_error = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.CLASS_NAME, locators.ERROR_MESSAGE))
     )

     # Проверка наличие ошибки при вводе некорректного пароля. error.text должен быть равен "Некорректный пароль"
     assert password_error is not None and password_error.text == "Некорректный пароль"

     driver.quit()