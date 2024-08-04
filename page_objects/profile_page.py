import allure
from page_objects.base_page import BasePage
from locators import ProfileLocators


class ProfilePage(BasePage):
    link_orders_history = ProfileLocators.LINK_ORDERS_HISTORY
    order_number_in_history = ProfileLocators.ORDER_NUMBER_IN_HISTORY

    @allure.step('Открыть Историю заказов')
    def open_orders_history(self):
        self.click_to_element_with_wait_overlay(self.link_orders_history)
