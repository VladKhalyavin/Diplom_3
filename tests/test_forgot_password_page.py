import allure
from page_objects.forgot_password_page import ForgotPasswordPage
from data import URL_FORGOT_PASSWORD, URL_RESET_PASSWORD
from locators import CommonLocators


class TestForgotPasswordPage:

    @allure.title('Ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_click_refresh_button(self, driver, user_data, create_and_delete_user):
        driver.get(URL_FORGOT_PASSWORD)
        refresh = ForgotPasswordPage(driver)
        refresh.go_to_reset_password(user_data['email'])
        assert driver.current_url == URL_RESET_PASSWORD

    @allure.title('Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    def test_input_email_and_click_refresh_button(self, driver, user_data, create_and_delete_user):
        driver.get(URL_FORGOT_PASSWORD)
        refresh = ForgotPasswordPage(driver)
        refresh.go_to_reset_password(user_data['email'])
        refresh.click_to_show_password()
        assert driver.find_element(*CommonLocators.PASSWORD_IS_ACTIVE)




