import allure
from page_objects.base_page import BasePage
from locators import FeedLocators


class FeedPage(BasePage):
    last_order = FeedLocators.LAST_ORDER
    modal_order_info = FeedLocators.MODAL_ORDER_INFO
    modal_order_number = FeedLocators.MODAL_ORDER_NUMBER
    modal_burger_name = FeedLocators.MODAL_BURGER_NAME
    ul_orders_in_progress = FeedLocators.UL_ORDERS_IN_PROGRESS
    alltime_order_counter = FeedLocators.ALLTIME_ORDERS_COUNTER
    today_order_counter = FeedLocators.TODAY_ORDERS_COUNTER

    @allure.step('Нажатие на плитку последнего заказа')
    def click_to_last_order(self):
        self.click_to_element_with_wait_overlay(self.last_order)
