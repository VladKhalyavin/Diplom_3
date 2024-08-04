import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from data import BASE_URL
from page_objects.constructor_page import ConstructorPage
from halper import Halper


class TestConstructorPage:

    @allure.title('Проверка появления всплывающего окна с деталями по клику на ингредиент')
    def test_open_ingredients_details(self, driver):
        driver.get(BASE_URL)
        constructor = ConstructorPage(driver)
        constructor.click_to_first_ingredient()

        try:
            driver.find_element(*constructor.modal_ingredient)
            driver.find_element(*constructor.h_ingredients_details)
        except NoSuchElementException:
            is_visible = False
        else:
            is_visible = True

        assert (is_visible == True), 'Детали ингредиента не отражается на странице'

    @allure.title('Проверка закрытия всплывающего окна с деталями по клику на крестик')
    def test_close_modal_window(self, driver):

        driver.get(BASE_URL)
        constructor = ConstructorPage(driver)
        constructor.click_to_first_ingredient()
        constructor.click_to_close_modal()

        try:
            driver.find_element(*constructor.h_ingredients_details)
            driver.find_element(*constructor.button_close_ingredient_modal)
        except NoSuchElementException:
            is_visible = False
        else:
            is_visible = True

        assert (is_visible == False), 'Детали ингредиента отражается на странице'

    @allure.title('Проверка увеличения каунтера ингредиента, при добавлении ингредиента в заказ')
    def test_adding_ingredient_increasing_counter(self, driver):
        driver.get(BASE_URL)
        constructor = ConstructorPage(driver)
        constructor.drag_and_drop_ingredient()

        assert constructor.get_text_from_element(constructor.p_first_ingredient_counter) == '2'

    @allure.title('Проверка создание заказа - авторизованный пользователь - успешное создание заказа')
    def test_create_order_with_access_token_successful_creation(self, driver, set_token, create_order_ui):
        create_order_ui.wait_overlay()
        WebDriverWait(driver, 10).until(lambda d: d.find_element(*create_order_ui.h_order_number).text != '9999')
        order_number = create_order_ui.get_text_from_element(create_order_ui.h_order_number)

        assert (create_order_ui.find_element_with_wait(create_order_ui.modal_order) and
                Halper.check_order_creation(set_token, order_number) == True), ('Заказ не создан, либо не открылось'
                                                                                ' модальное окно')
