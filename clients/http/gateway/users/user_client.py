from typing import TypedDict
from httpx import Response
from clients.http.client import HTTPClient
from clients.http.gateway.gateway_client import build_gateway_http_client


class CreateUserRequestDict(TypedDict):
    """
    Структура данных для создания нового пользователя.
    """
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class UsersGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/users сервиса http-gateway.
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Создание нового пользователя.

        :param request: Словарь с данными нового пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/users", json=request)
    

def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(client=build_gateway_http_client())




# client_user = build_users_gateway_http_client()
#
# # Данные нового пользователя
# new_user = CreateUserRequestDict(
#     email="example77667@example.com",
#     lastName="Иванов",
#     firstName="Иван",
#     middleName="Иванович",
#     phoneNumber="+79999999999",
# )
#
# response = client_user.create_user_api(new_user)
# print(response.status_code)
# print(response.json())




# from httpx import Client
# if __name__ == "__main__":
#     # Создание экземпляра HTTPX-клиента
#     base_url = "http://localhost:8003"  # Замените на реальный URL вашего API
#     http_client = Client(base_url=base_url)

#     # Создание специализированного клиента для работы с пользователями
#     users_client = UsersGatewayHTTPClient(http_client)

#     # Данные нового пользователя
#     new_user = CreateUserRequestDict(
#         email="example7777@example.com",
#         lastName="Иванов",
#         firstName="Иван",
#         middleName="Иванович",
#         phoneNumber="+79999999999",
#     )

#     # Отправляем запрос на создание пользователя
#     response = users_client.create_user_api(new_user)

#     # Выводим статус и тело ответа
#     print("Код статуса:", response.status_code)
#     try:
#         data = response.json()
#         print("Ответ сервера:", data)
#     except Exception as e:
#         print("Ошибка преобразования JSON:", e)
#         print("Тело ответа:", response.text)



