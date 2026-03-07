# Импортируем фабричные функции для создания API-клиентов
from clients.grpc.gateway.accounts.account_client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.cards.cards_client import build_cards_gateway_grpc_client
from clients.grpc.gateway.users.users_client import build_users_gateway_grpc_client
from clients.grpc.gateway.documents.documents_client import build_documents_gateway_grpc_client
from clients.grpc.gateway.operations.operations_client import build_operations_gateway_grpc_client


# Создаём API-клиенты для работы с сервисами Users, Accounts и Cards
users_gateway_client = build_users_gateway_grpc_client()
cards_gateway_client = build_cards_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
documents_gateway_client = build_documents_gateway_grpc_client()
operations_gateway_client = build_operations_gateway_grpc_client()


# Шаг 1. Создаём пользователя
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

# Открыть кредитный счёт с
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(create_user_response.user.id)
print('Open debit card account response:', open_debit_card_account_response)

# Создать операцию пополнения счета
make_top_up_operations_response = operations_gateway_client.make_top_up_operation(
    card_id=open_debit_card_account_response.account.cards[0].id,
    account_id=open_debit_card_account_response.account.id)
print('Make top up operation response:', make_top_up_operations_response)