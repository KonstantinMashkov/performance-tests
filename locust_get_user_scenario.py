from locust import HttpUser, between, task, User

from tools.fakers import fake  # генератор случайных данных
from clients.http.gateway.users.user_client import build_users_gateway_locust_http_client, UsersGatewayHTTPClient
from  clients.http.gateway.users.user_schema import CreateUserResponseSchema

class GetUserScenarioUser(User):
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayHTTPClient
    create_user_response: CreateUserResponseSchema

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def get_user(self):
        """
        Основная нагрузочная задача: получение информации о пользователе.
        Здесь мы выполняем GET-запрос к /api/v1/users/{user_id}.
        """
        self.users_gateway_client.get_user(self.create_user_response.user.id)

