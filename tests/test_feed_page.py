import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from halper import Halper

from page_objects.feed_page import FeedPage
from page_objects.profile_page import ProfilePage
from data import URL_FEED, URL_ACCOUNT


class TestFeedPage:

    @allure.title('Проверка открытия всплывающего окна с деталями о заказе по клику на плитку заказа')
    def test_open_order_details_successful_opening(self, driver, create_order_api):
        driver.get(URL_FEED)
        feed = FeedPage(driver)
        feed.click_to_last_order()

        assert (feed.find_element_with_wait(feed.modal_order_info) and
                feed.get_text_from_element(feed.modal_order_number) == f"#0{create_order_api['order_number']}" and
                feed.get_text_from_element(feed.modal_burger_name) == create_order_api['name'])

    @allure.title('Проверка отображения заказов из Истории пользователя в Ленте заказов')
    def test_check_user_orders_in_feed(self, driver, set_token):
        driver.get(URL_ACCOUNT)
        order = ProfilePage(driver)
        order.open_orders_history()
        Halper.create_order(set_token)
        history_order_number = order.get_text_from_element(ProfilePage.order_number_in_history)
        driver.get(URL_FEED)

        try:
            order.find_element_with_wait([By.XPATH, '//ul/li/a/div/p[text()="{}"]'.format(history_order_number)])
        except NoSuchElementException:
            is_visible = False
        else:
            is_visible = True

        assert (is_visible == True), 'Номер заказа из профиля не найден в Ленте заказов'

    @allure.title('Проверка увеличения счетчика заказов "Выполнено за все время"')
    def test_alltime_order_counter(self, driver, set_token):
        driver.get(URL_FEED)
        feed = FeedPage(driver)
        orders_count = feed.get_text_from_element(feed.alltime_order_counter)
        orders_number = Halper.create_order(set_token)['order_number']
        new_orders_count = feed.get_text_from_element(feed.alltime_order_counter)

        assert new_orders_count == str(orders_number) and new_orders_count == str(int(orders_count)+1)

    @allure.title('Проверка увеличения счетчика заказов "Выполнено за сегодня"')
    def test_today_order_counter(self, driver, set_token):
        driver.get(URL_FEED)
        feed = FeedPage(driver)
        orders_count = feed.get_text_from_element(feed.today_order_counter)
        Halper.create_order(set_token)
        total_count_from_api = Halper.get_orders_counts()['totalToday']
        new_orders_count = feed.get_text_from_element(feed.today_order_counter)

        assert new_orders_count == str(total_count_from_api) and new_orders_count == str(int(orders_count)+1)

    @allure.title('Проверка отображения заказа в списке "в работе"')
    def test_order_on_in_progress_list(self, driver, create_order_api):
        driver.get(URL_FEED)
        feed = FeedPage(driver)
        number_from_order_list = feed.get_text_from_element([By.XPATH,
                                                             '//ul[contains(@class, "OrderFeed_orderListReady")]/li[1][contains(text()[2], "{}")]'.format(
                                                                 create_order_api['order_number'])])

        assert number_from_order_list == f"0{create_order_api['order_number']}"
