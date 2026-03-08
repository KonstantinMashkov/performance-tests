from locust import between, task, User


from clients.http.gateway.accounts.accounts_client import build_accounts_gateway_locust_http_client, AccountsGatewayHTTPClient
from clients.http.gateway.users.user_client import build_users_gateway_locust_http_client, UsersGatewayHTTPClient
from  clients.http.gateway.users.user_schema import CreateUserResponseSchema


class GetUserScenarioUser(User):
    # Пауза между запросами для каждого виртуального пользователя (в секундах)
    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayHTTPClient
    create_user_response: CreateUserResponseSchema
    account_gateway_client: AccountsGatewayHTTPClient


    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()
        self.account_gateway_client = build_accounts_gateway_locust_http_client(self.environment)


    @task
    def open_debit_card_account(self):
        """
        Основная нагрузочная задача: получение информации о пользователе.
        Здесь мы выполняем GET-запрос к /api/v1/accounts/{user_id}.
        """
        self.account_gateway_client.open_debit_card_account(self.create_user_response.user.id)