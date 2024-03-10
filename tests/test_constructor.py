from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait
import configuration
import locators
from selenium.webdriver.common.by import By
from selenium import webdriver


# тестирование переходов к разделам конструктора
# - переход к булкам
# - переход к соусам
# - переход к начинкам
def tests_navigation_positive():
    # Открываем браузер
    driver = webdriver.Chrome()
    # Открываем страницу
    driver.get(configuration.URL_SERVICE)
    time.sleep(2)
    # получение кнопок категорий
    constructor_categories_button = driver.find_elements(By.XPATH, locators.CONSTRUCTOR_CATEGORIES_BUTTON)[::-1]
    # получение заголовков категорий в меню
    constructor_categories_title = driver.find_elements(By.XPATH, locators.CONSTRUCTOR_CATEGORIES_TITLE)[::-1]
    # перебираем кнопки и названия категориий в меню
    for button, title in zip(constructor_categories_button, constructor_categories_title):
        time.sleep(2)
        # кликаем на кнопку [Начинки, Соусы, Булки]
        button.click()
        # ждем пока элемент-заголовок не станет видимым
        element = WebDriverWait(driver, 15).until(EC.visibility_of(title))
        # проверяем совпадение названий на кнопке и в заголовке в меню
        assert element.text == button.text

    driver.quit()