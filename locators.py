# Форма регистрации
# Поля Input формы регистрации
NAME_INPUT = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"  # Имя
EMAIL_INPUT = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"  # e-mail
PASSWORD_INPUT = "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input"  # Пароль

SUBMIT_BUTTON = "//*[@id='root']/div/main/div/form/button" # Кнопка submit в форме регистрации
ERROR_MESSAGE = "input__error"  # Тег в котором выводится ошибка при некорректном вводе в поле пароля

#Форма Авторизации
ACCOUNT_BUTTON = '//*[@id="root"]/div/main/section[2]/div/button'  # Кнопка "Войти в аккаунт" на на главной
PROFILE_BUTTON = ".//a[@href='/account']"  # Кнопка "Личный кабинет" на главной станице
REGISTER_BUTTON = "//a[contains(@class, 'Auth_link__1fOlj')]"  # Кнопка "Войти"ё на странице регистрации
FORGOT_PASSWORD_BUTTON = "//a[contains(@class, 'Auth_link__1fOlj')]"  # Кнопка "Войти" на странице восстановления пароля

# Форма авторизации
# Поле "Email"
LOGIN_FORM_EMAIL_INPUT = "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input"
# Поле "Пароль"
LOGIN_FORM_PASSWORD_INPUT = "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"
# Кнопка "Войти"
LOGIN_FORM_SUBMIT_BUTTON = "//*[@id='root']/div/main/div/form/button"

# Личный кабинет
# Ссылка "Конструктор" в личном кабинете
PROFILE_CONSTRUCTOR = "(//a[contains(@class, 'AppHeader_header__link__3D_hX')])[1]"
PROFILE_LOGOUT = "//button[contains(@class, 'Account_button__14Yp3')]"

# Конструктор
# Кнопки категорий
CONSTRUCTOR_CATEGORIES_BUTTON = "//section[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//div[1]//div"
# Заголовок категории в меню
CONSTRUCTOR_CATEGORIES_TITLE = "//section[contains(@class, 'BurgerIngredients_ingredients__1N8v2')]//div[2]//h2"