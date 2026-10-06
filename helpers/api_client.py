import requests

from helpers.urls import API_LOGIN, API_ORDERS, API_INGREDIENTS


class ApiClient:
    """Клиент для работы с API Stellar Burgers."""

    def login(self, email: str, password: str) -> str:
        """Авторизация, возвращает accessToken."""
        response = requests.post(API_LOGIN, json={
            "email": email,
            "password": password
        })
        return response.json().get("accessToken")

    def get_ingredients(self) -> list:
        """Возвращает список ID ингредиентов."""
        response = requests.get(API_INGREDIENTS)
        data = response.json()["data"]
        return [data[0]["_id"], data[1]["_id"]]

    def create_order(self, token: str) -> dict:
        """Создаёт заказ и возвращает ответ."""
        ingredients = self.get_ingredients()
        response = requests.post(
            API_ORDERS,
            json={"ingredients": ingredients},
            headers={"Authorization": token}
        )
        return response.json()
    
