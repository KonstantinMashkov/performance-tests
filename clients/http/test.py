# import time
# from httpx import Client
# from clients.http.user_client import UsersGatewayHTTPClient, CreateUserRequestDict
# from clients.http.accounts_client import AccountsGatewayHTTPClient, OpenDepositAccountRequestDict
# from  clients.http.gateway.operations.operation_client import OperationsGatewayHTTPClient, GetOperationsSummaryQueryDict
#
#
# # Создание экземпляра HTTPX-клиента
# base_url = "http://localhost:8003"  # Замените на реальный URL вашего API
# http_client = Client(base_url=base_url)
#
# # Создание специализированного клиента для работы с пользователями
# users_client = UsersGatewayHTTPClient(http_client)
#
#
# # Данные нового пользователя
# new_user = CreateUserRequestDict(
#     email=f"user.{time.time()}@example.com",
#     lastName="Иванов",
#     firstName="Иван",
#     middleName="Иванович",
#     phoneNumber="+79999999999",
# )
#
# # Отправляем запрос на создание пользователя
# response = users_client.create_user_api(new_user)
#
# # Выводим статус и тело ответа
# print("Код статуса:", response.status_code)
#
# data = response.json()
# print("Ответ сервера:", data)
# print("ID пользователя:", data['user']['id'])
# user_id = data['user']['id']
#
#
# # Создаем депозит
# account_client = AccountsGatewayHTTPClient(http_client)
# user_id = OpenDepositAccountRequestDict(userId=user_id)
# response_open_deposit_account = account_client.open_deposit_account_api(user_id)
#
# data_deposit_account = response_open_deposit_account.json()
#
# print("Статус код", response_open_deposit_account.status_code)
# print("Ответ сервера:", data_deposit_account)
# print("ID акаунта", data_deposit_account['account']['id'])
#
# #Получаем список операций
# operations_client = OperationsGatewayHTTPClient(http_client)
# account_id = GetOperationsSummaryQueryDict(accountId=data_deposit_account['account']['id'])
# response_get_operations_api = operations_client.get_operations_api(account_id)
#
# print("Staus code", response_get_operations_api.status_code)
# data_response_get_operations_api = response_get_operations_api.json()
# print("Ответ сервера", data_response_get_operations_api)
