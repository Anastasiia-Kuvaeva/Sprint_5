import pytest
import time
import configuration
import locators
from selenium.webdriver.common.by import By


# тестирование переходов в личном кабинете
# - переход в личный кабинет по клику на «Личный кабинет»
# - переход из личного кабинета в конструктор
# - выход из аккаунта
@pytest.mark.parametrize("selector, url, target_url", [
    (locators.PROFILE_BUTTON, configuration.URL_SERVICE, configuration.URL_ACCOUNT_PROFILE),
    (locators.PROFILE_CONSTRUCTOR, configuration.URL_ACCOUNT, configuration.URL_SERVICE),
    (locators.PROFILE_LOGOUT, configuration.URL_ACCOUNT, configuration.URL_LOGIN)
])
def tests_navigation_positive(selector, url, target_url, authorization):
    driver = authorization()
    # переходим на главную страницу
    driver.get(url)
    time.sleep(2)
    # переход в личный кабинет по кнопке «Личный кабинет» на главной
    driver.find_element(By.XPATH, selector).click()
    # ждем перехода на новую страницу
    time.sleep(2)
    # проверка перехода на /account/profile
    assert driver.current_url == target_url
    driver.quit()