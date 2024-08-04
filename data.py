from locators import LoginLocators, CommonLocators, FeedLocators, ConstructorLocators
from page_objects.transitions import Transitions

BASE_URL = 'https://stellarburgers.nomoreparties.site'

URL_CONSTRUCTOR = f'{BASE_URL}/'  # страница конструктора
URL_FEED = f'{BASE_URL}/feed'  # страница ленты заказов
URL_LOGIN_PAGE = f'{BASE_URL}/login'  # страница авторизации
URL_FORGOT_PASSWORD = f'{BASE_URL}/forgot-password'  # страница восстановления пароля
URL_RESET_PASSWORD = f'{BASE_URL}/reset-password'  # страница сброса пароля
URL_ACCOUNT = f'{BASE_URL}/account'  # страница аккаунта
URL_PROFILE = f'{BASE_URL}/account/profile'  # страница профиля пользователя
URL_ORDERS_HISTORY = f'{BASE_URL}/account/order-history'

# ENDPOINTS:
ENDPOINT_REGISTER = '/api/auth/register'
ENDPOINT_LOGIN = '/api/auth/login'
ENDPOINT_USER = '/api/auth/user'


class TransitionsData:
    # датасет для проверки переходов в Личном кабинете
    dataset_account = [(Transitions.link_orders_history, Transitions.link_orders_history, URL_ORDERS_HISTORY),
                       (Transitions.button_logout, LoginLocators.BUTTON_LOGIN, URL_LOGIN_PAGE)]
    # датасет для проверки переходов в хедере
    dataset_headers = [(URL_FEED, CommonLocators.HEADER_CONSTRUCTOR, ConstructorLocators.BUTTON_LOGIN_MAIN_PAGE,
                        URL_CONSTRUCTOR),
                       (URL_CONSTRUCTOR, CommonLocators.HEADER_ORDERS_FEED, FeedLocators.LAST_ORDER, URL_FEED)]
