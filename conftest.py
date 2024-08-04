import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from halper import Halper
from data import BASE_URL, ENDPOINT_REGISTER, ENDPOINT_USER
from page_objects.constructor_page import ConstructorPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def user_data():
    user_data = Halper.unique_user_data()
    return user_data


@pytest.fixture(scope='function')
def create_and_delete_user(user_data):
    response = requests.post(f'{BASE_URL}{ENDPOINT_REGISTER}', data=user_data)
    yield response
    headers = {'Authorization': response.json()['accessToken']}
    requests.delete(f'{BASE_URL}{ENDPOINT_USER}', headers=headers)


@pytest.fixture(scope='function')
def set_token(driver, create_and_delete_user):
    driver.get(BASE_URL)
    access_token = create_and_delete_user.json()['accessToken']
    refresh_token = create_and_delete_user.json()['refreshToken']
    driver.execute_script(f"localStorage.setItem('accessToken', '{access_token}');")
    driver.execute_script(f"localStorage.setItem('refreshToken', '{refresh_token}');")
    driver.refresh()
    return access_token


@pytest.fixture(scope='function')
def create_order_ui(driver, create_and_delete_user, set_token):
    constructor = ConstructorPage(driver)
    constructor.drag_and_drop_ingredient()
    constructor.click_to_checkout()
    return constructor


@pytest.fixture(scope='function')
def create_order_api(driver, create_and_delete_user, set_token):
    create_order_api = Halper.create_order(set_token)
    return create_order_api

