import requests
from typing import Dict
from faker import Faker
from data import BASE_URL


class Halper:

    @staticmethod
    def unique_user_data(password: int = 10) -> Dict:
        """
        Создает словарь с данными пользователя
        :param password: длинна пароля (по умолчанию 10 символов)
        :return: словарь данных пользователя с ключами 'name','email','password'
        """

        fake = Faker("ru_RU")
        return {'name': fake.user_name(),
                'email': fake.email(domain='yandex.ru'),
                'password': fake.password(password, False)}

    @staticmethod
    def check_order_creation(token, number):
        """
        Проверяет, что номер последнего заказа соответсвует номеру созданного заказа, отраженного в модальном окне
        :param token: accessToken пользователя
        :param number: номер заказа, полученный с модального окна
        :return: True - в случае совпадения номера последнего заказа пользователя с номером, отраженным в модульном
        окне.
        False - в случае, если номер заказа в окне не равен номеру последнего заказа пользователя.
        """
        headers = {'Authorization': token}
        response = requests.get(f'{BASE_URL}/api/orders', headers=headers)

        if int(number) == response.json()['orders'][-1]['number']:
            return True
        else:
            return False

    @staticmethod
    def create_order(token: str) -> Dict:
        """
        Создает заказ с одним ингредиентом
        :param token: accessToken пользователя
        :return: name - имя бургера, order_number - номер заказа.
        """
        headers = {'Authorization': token}
        data = {"ingredients": ["61c0c5a71d1f82001bdaaa6f"]}
        response = requests.post(f'{BASE_URL}/api/orders', headers=headers, data=data).json()

        return {'name': response['name'],
                'order_number': response['order']['number']}

    @staticmethod
    def get_orders_counts() -> Dict:
        """
        Возвращает количество заказов сегодня и за все время
        :return: total - заказов всего, totalToday - заказов сегодня.
        """
        response = requests.get(f'{BASE_URL}/api/orders/all').json()

        return {'total': response['total'],
                'totalToday': response['totalToday']}

