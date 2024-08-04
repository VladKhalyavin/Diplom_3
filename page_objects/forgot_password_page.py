import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from page_objects.base_page import BasePage
from locators import ForgotPasswordLocators, CommonLocators


class ForgotPasswordPage(BasePage):
    button_restore = ForgotPasswordLocators.BUTTON_RESTORE
    button_save = ForgotPasswordLocators.BUTTON_SAVE
    button_show_password = CommonLocators.BUTTON_SHOW_PASSWORD
    input_email = CommonLocators.INPUT_EMAIL

    @allure.step('Ввод email на странице восстановления пароля')
    def input_email_to_form(self, email):
        self.add_text_to_element(self.input_email, email)

    @allure.step('Нажатие кнопки "Восстановить"')
    def click_to_restore(self):
        self.click_to_element_with_wait_overlay(self.button_restore)

    def go_to_reset_password(self, email):
        self.input_email_to_form(email)
        self.click_to_restore()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.button_save))

    def click_to_show_password(self):
        self.click_to_element_with_wait_overlay(self.button_show_password)

