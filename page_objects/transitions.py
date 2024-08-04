import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from locators import LoginLocators, CommonLocators, ProfileLocators


class Transitions(BasePage):

    link_forgot_password = LoginLocators.LINK_FORGOT_PASSWORD
    header_profile = CommonLocators.HEADER_PROFILE
    link_orders_history = ProfileLocators.LINK_ORDERS_HISTORY
    button_logout = ProfileLocators.BUTTON_LOGOUT

    @allure.step('Нажатие на ссылку "Восстановить пароль"')
    def click_to_forgot_password(self):
        self.click_to_element_with_wait_overlay(self.link_forgot_password)

    @allure.step('Нажатие на ссылку "Личный кабинет" на панели навигации')
    def click_to_header_profile(self):
        self.click_to_element_with_wait_overlay(self.header_profile)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(self.link_orders_history))

    @allure.step('Нажатие на кнопку перехода c ожиданием появления элемента')
    def click_to_transition_link(self, locator, target):
        self.click_to_element_with_wait_overlay(locator)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(target))

