import allure
from page_objects.base_page import BasePage
from locators import ConstructorLocators


class ConstructorPage(BasePage):

    first_ingredient = ConstructorLocators.FIRST_INGREDIENT
    p_first_ingredient_counter = ConstructorLocators.P_FIRST_INGREDIENT_COUNTER
    modal_ingredient = ConstructorLocators.MODAL_INGREDIENT
    modal_order = ConstructorLocators.MODAL_ORDER
    h_ingredients_details = ConstructorLocators.H_INGREDIENTS_DETAILS
    button_close_ingredient_modal = ConstructorLocators.BUTTON_CLOSE_INGREDIENT_MODAL
    button_close_order_modal = ConstructorLocators.BUTTON_CLOSE_ORDER_MODAL
    ul_burger_constructor = ConstructorLocators.BERGER_CONSTRUCTOR
    button_checkout = ConstructorLocators.BUTTON_CHECKOUT
    h_order_number = ConstructorLocators.H_ORDER_NUMBER

    @allure.step('Нажать на первый ингредиент в конструкторе')
    def click_to_first_ingredient(self):
        self.click_to_element_with_wait_overlay(self.first_ingredient)

    @allure.step('Закрыть модальное окно')
    def click_to_close_modal(self):
        self.clic_to_element(self.button_close_ingredient_modal)

    @allure.step('Перетащить ингредиент')
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(self.first_ingredient, self.ul_burger_constructor)

    @allure.step('Нажать кнопку "Оформить заказ"')
    def click_to_checkout(self):
        self.clic_to_element(self.button_checkout)
