import time
from typing import TypedDict
from httpx import Response
from clients.http.client import HTTPClient
from clients.http.gateway.gateway_client import build_gateway_http_client
from clients.http.gateway.users.user_schema import (
    GetUserResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema
)


class UsersGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/users сервиса http-gateway.
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Получить данные пользователя по его user_id.

        :param user_id: Идентификатор пользователя.
        :return: Ответ от сервера (объект httpx. Response).
        """
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создание нового пользователя.

        :param request: Словарь с данными нового пользователя.
        :return: Ответ от сервера (объект httpx. Response).
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        # return GetUserResponseSchema(**response.json())
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        request = CreateUserRequestSchema(
            email=f"user.{time.time()}@example.com",
            last_name="string",
            first_name="string",
            middle_name="string",
            phone_number="string"
        )
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


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



