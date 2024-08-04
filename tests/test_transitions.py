import pytest
import allure

from page_objects.transitions import Transitions
from data import URL_LOGIN_PAGE, URL_FORGOT_PASSWORD, URL_PROFILE, TransitionsData


class TestTransitions:

    @allure.title('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_transition_from_login_to_forgot_password(self, driver):
        driver.get(URL_LOGIN_PAGE)
        transition = Transitions(driver)
        transition.click_to_forgot_password()
        assert driver.current_url == URL_FORGOT_PASSWORD

    @allure.title('Переход по клику на Личный кабинет - с токеном авторизации')
    def test_transition_from_main_to_profile_with_access_token(self, driver, create_and_delete_user, set_token):
        transition = Transitions(driver)
        transition.click_to_header_profile()
        assert driver.current_url == URL_PROFILE

    @allure.title('Переход в раздел История заказов / Выход из аккаунта - с токеном авторизации')
    @pytest.mark.parametrize('locator,target,url', TransitionsData.dataset_account)
    def test_transition_account_links_with_access_token(self, driver, create_and_delete_user, set_token, locator, target, url):
        transition = Transitions(driver)
        transition.click_to_header_profile()
        transition.click_to_transition_link(locator, target)

        assert driver.current_url == url

    @allure.title('Переходы в хедере - без токена авторизации')
    @pytest.mark.parametrize('url,locator,target,result', TransitionsData.dataset_headers)
    def test_transitions_nav_bar_without_access_token(self, driver, url, locator, target, result):
        driver.get(url)
        transition = Transitions(driver)
        transition.click_to_transition_link(locator, target)

        assert driver.current_url == result
