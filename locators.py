# Форма регистрации
# Поля Input формы регистрации
# Имя
NAME_INPUT = ".//form[contains(@class, 'Auth_form__3qKeq')]//label[text() = 'Имя']/parent::div/input"
# Email
EMAIL_INPUT = ".//form[contains(@class, 'Auth_form__3qKeq')]//label[text() = 'Email']/parent::div/input"
# Пароль
PASSWORD_INPUT = ".//form[contains(@class, 'Auth_form__3qKeq')]//input[@name='Пароль']"
# Кнопка submit в форме регистрации
SUBMIT_BUTTON = ".//form[contains(@class, 'Auth_form__3qKeq')]//button[text() = 'Зарегистрироваться' and contains(@class, 'button_button__33qZ0')]"
# Тег в котором выводится ошибка при некорректном вводе в поле пароля
ERROR_MESSAGE = ".//form[contains(@class, 'Auth_form__3qKeq')]//p[contains(@class, 'input__error')]"

# Переход на форму авторизации
# Кнопка "Войти в аккаунт" на на главной
ACCOUNT_BUTTON = ".//button[text() = 'Войти в аккаунт' and contains(@class, 'button_button__33qZ0')]"
# Кнопка "Личный кабинет" на главной станице
PROFILE_BUTTON = ".//a[@href='/account']"
# Кнопка "Войти" на странице регистрации
REGISTER_BUTTON = "//a[contains(@class, 'Auth_link__1fOlj')]"
# Кнопка "Войти" на странице восстановления пароля
FORGOT_PASSWORD_BUTTON = "//a[contains(@class, 'Auth_link__1fOlj')]"

# Форма авторизации
# Поле "Email"
LOGIN_FORM_EMAIL_INPUT = ".//form[contains(@class, 'Auth_form__3qKeq')]//label[text() = 'Email']/parent::div/input"
# Поле "Пароль"
LOGIN_FORM_PASSWORD_INPUT = ".//form[contains(@class, 'Auth_form__3qKeq')]//input[@name='Пароль']"
# Кнопка "Войти"
LOGIN_FORM_SUBMIT_BUTTON = ".//form[contains(@class, 'Auth_form__3qKeq')]//button[text() = 'Войти' and contains(@class, 'button_button__33qZ0')]"

# Кнопка "Оформить заказ"
CHECKOUT_BUTTON = ".//button[text() = 'Оформить заказ']"

# Личный кабинет
# Ссылка "Конструктор" в личном кабинете
PROFILE_CONSTRUCTOR = ".//p[text() = 'Конструктор' and contains(@class, 'AppHeader_header__linkText__3q_va ')]/parent::a"
# Кнопка "Выход"
PROFILE_LOGOUT = ".//button[text() = 'Выход' and contains(@class, 'Account_button__14Yp3')]"

# Конструктор
# Таб "Булки"
CONSTRUCTOR_CATEGORIES_BUTTON_BULKI = ".//section[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//div[contains(@class, 'tab_tab__1SPyG ')]/span[text() = 'Булки']/parent::div"
# Таб "Соусы"
CONSTRUCTOR_CATEGORIES_BUTTON_SOUSI = ".//section[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//div[contains(@class, 'tab_tab__1SPyG ')]/span[text() = 'Соусы']/parent::div"
# Таб "Начинки"
CONSTRUCTOR_CATEGORIES_BUTTON_NACHINKI = ".//section[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//div[contains(@class, 'tab_tab__1SPyG ')]/span[text() = 'Начинки']/parent::div"