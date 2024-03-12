from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.support.wait import WebDriverWait
import configuration
import locators
from selenium.webdriver.common.by import By


class TestConstructor:

    # тестирование переходов к разделу "Булки"
    @pytest.mark.usefixtures("driver")
    def tests_tab_bulki_positive(self, driver):
        # Открываем страницу
        driver.get(configuration.URL_SERVICE)
        # Ожидание кликабельности таба "Соусы"
        tab_sousi = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, locators.CONSTRUCTOR_CATEGORIES_BUTTON_SOUSI))
        )
        assert tab_sousi is not None
        # кликаем по табу "Соусы"
        tab_sousi.click()
        # получаем таб "Булки"
        tab_bulki = driver.find_element(By.XPATH, locators.CONSTRUCTOR_CATEGORIES_BUTTON_BULKI)
        # кликаем по табу "Булки"
        tab_bulki.click()
        # проверяем, что у таба "Булки" появился класс "tab_tab_type_current__2BEPc"
        assert 'tab_tab_type_current__2BEPc' in tab_bulki.get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' not in tab_sousi.get_attribute('class')

    # тестирование переходов к разделу "Соусы"
    @pytest.mark.usefixtures("driver")
    def tests_tab_sousi_positive(self, driver):
        # Открываем страницу
        driver.get(configuration.URL_SERVICE)
        # Ожидание кликабельности таба "Соусы"
        tab_sousi = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, locators.CONSTRUCTOR_CATEGORIES_BUTTON_SOUSI))
        )
        assert tab_sousi is not None
        # кликаем по табу "Соусы"
        tab_sousi.click()
        # проверяем, что у таба "Соусы" появился класс "tab_tab_type_current__2BEPc"
        assert 'tab_tab_type_current__2BEPc' in tab_sousi.get_attribute('class')

    # тестирование переходов к разделу "Начинки"
    @pytest.mark.usefixtures("driver")
    def tests_tab_nachinki_positive(self, driver):
        # Открываем страницу
        driver.get(configuration.URL_SERVICE)
        # Ожидание кликабельности таба "Начинки"
        tab_nachinki = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, locators.CONSTRUCTOR_CATEGORIES_BUTTON_NACHINKI))
        )
        assert tab_nachinki is not None
        # кликаем по табу "Начинки"
        tab_nachinki.click()
        # проверяем, что у таба "Начинки" появился класс "tab_tab_type_current__2BEPc"
        assert 'tab_tab_type_current__2BEPc' in tab_nachinki.get_attribute('class')
