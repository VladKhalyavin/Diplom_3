from selenium.webdriver.common.by import By


class CommonLocators:
    """
    Общие локаторы \n
    [Встречаются болле чем на одной странице]
    """
    HEADER_CONSTRUCTOR = [By.XPATH, './/p[text()="Конструктор"]//parent::a']  # ссылка на Конструктор в шапке
    HEADER_ORDERS_FEED = [By.XPATH, './/p[text()="Лента Заказов"]//parent::a']  # ссылка на Ленту Заказов в шапке
    HEADER_PROFILE = [By.XPATH, '//p[text()="Личный Кабинет"]/parent::a']  # ссылка на Личный кабинет в шапке
    INPUT_NAME = [By.XPATH, '//label[text()="Имя"]/following-sibling::input']  # поле ввода имени
    INPUT_EMAIL = [By.XPATH, './/label[text()="Email"]/following-sibling::input']  # поле ввода почты
    INPUT_PASSWORD = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']  # поле ввода пароля
    PASSWORD_IS_ACTIVE = [By.XPATH,
                          '//label[text()="Пароль"]/parent::div[contains(@class, "input_status_active")]']  # поле ввода
    # пароля подсвечено
    BUTTON_SHOW_PASSWORD = [By.XPATH, '//div[contains(@class, "input__icon")]']  # кнопка показать пароль
    OVERLAY1 = [By.XPATH, '//div[contains(@class,"Modal_modal")]/div[contains(@class,"Modal_modal_overlay")]']
    OVERLAY2 = [By.XPATH, '//section/div[contains(@class,"Modal_modal_overlay")]']


class LoginLocators:
    """
    Локаторы страницы авторизации
    """
    BUTTON_LOGIN = [By.XPATH, './/button[text()="Войти"]']  # кнопка "Войти"
    LINK_FORGOT_PASSWORD = [By.XPATH, '//a[@href="/forgot-password"]']  # ссылка "Восстановить пароль"


class ForgotPasswordLocators:
    """
    Локаторы страницы восстановления пароля
    """
    BUTTON_RESTORE = [By.XPATH, '//button[text()="Восстановить"]']  # кнопка "Восстановить"
    BUTTON_SAVE = [By.XPATH, '//button[text()="Сохранить"]']  # кнопка "Сохранить"


class ProfileLocators:
    LINK_ORDERS_HISTORY = [By.XPATH, '//a[text() = "История заказов"]']  # ссылка на Историю заказов пользователя
    # номер заказа в истрии заказов
    ORDER_NUMBER_IN_HISTORY = [By.XPATH, '//ul/li/a/div/p[contains(@class, "text_type_digits-default")]']
    BUTTON_LOGOUT = [By.XPATH, '//button[text() = "Выход"]']  # кнопка выхода из аккаунта в профиле


class FeedLocators:
    LAST_ORDER = [By.XPATH, '//ul[contains(@class, "OrderFeed_list")]/li[1]']  # плитка последнего заказа
    MODAL_ORDER_INFO = [By.XPATH, '//div[contains(@class, "Modal_orderBox")]'] # модальное окно информации о заказе
    # номер заказа в модальном окне информации о заказе
    MODAL_ORDER_NUMBER = [By.XPATH,
                          '//div[contains(@class, "Modal_orderBox")]/p[contains(@class, "text_type_digits-default")]']
    # название бургера в модальном окне
    MODAL_BURGER_NAME = [By.XPATH, '//div[contains(@class, "Modal_orderBox")]/h2']
    UL_ORDERS_IN_PROGRESS = [By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]']  # список заказов в работе
    # счетчик всех заказов
    ALLTIME_ORDERS_COUNTER = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "OrderFeed_number")]']
    # счетчик заказов за сегодня
    TODAY_ORDERS_COUNTER = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "OrderFeed_number")]']


class ConstructorLocators:
    BUTTON_LOGIN_MAIN_PAGE = [By.XPATH, './/button[text()="Войти в аккаунт"]']  # кнопка "Войти в аккаунт" на главной странице
    FIRST_INGREDIENT = [By.XPATH, './/ul[1]/a[1]']  # первый ингредиент в конструкторе
    P_FIRST_INGREDIENT_COUNTER = [By.XPATH, '//ul[1]/a[1]/div/p[contains(@class, "counter_counter__num")]']  # счетчик количества первого ингредиента
    LAST_INGREDIENT = './/ul[last()]/a[last()]'  # последний ингредиент в конструкторе
    # модальное окно ингредиента
    MODAL_INGREDIENT = [By.XPATH,
                        '//section[contains(@class, "Modal_modal_opened")]'
                        '/div[contains(@class, "Modal_modal__container")]']
    MODAL_ORDER = [By.XPATH, '//div[contains(@class, "Modal_modal__contentBox")]']
    H_INGREDIENTS_DETAILS = [By.XPATH, '//h2[text()="Детали ингредиента"]']  #  заголовок в модальном окне "Детали ингредиента"
    H_ORDER_NUMBER = [By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]']  # номер заказа в модальном окне
    # кнопка закрыть модальное окно ингредиента
    BUTTON_CLOSE_INGREDIENT_MODAL = [By.XPATH,
                          '//section[contains(@class, "Modal_modal_opened")]'
                          '//button[contains(@class, "Modal_modal__close_modified")]']
    BUTTON_CLOSE_ORDER_MODAL = [By.XPATH, '//button[contains(@class, "Modal_modal__close_modified")]']  # кнопка закрыть модальное окно заказа
    BERGER_CONSTRUCTOR = [By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]']  # конструктор бургера
    BUTTON_CHECKOUT = [By.XPATH, '//button[text()="Оформить заказ"]']  # кнопка "Оформить заказ"

