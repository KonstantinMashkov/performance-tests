# Импортируем фабричные функции для создания API-клиентов
from clients.grpc.gateway.accounts.account_client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.cards.cards_client import build_cards_gateway_grpc_client
from clients.grpc.gateway.users.users_client import build_users_gateway_grpc_client
from clients.grpc.gateway.documents.documents_client import build_documents_gateway_grpc_client

# Создаём API-клиенты для работы с сервисами Users, Accounts и Cards
users_gateway_client = build_users_gateway_grpc_client()
cards_gateway_client = build_cards_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
documents_gateway_client = build_documents_gateway_grpc_client()

# Шаг 1. Создаём пользователя
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

# Открыть кредитный счёт с
open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(create_user_response.user.id)
print('Open credit card account response:', open_credit_card_account_response)

# Получить документ тарифа
get_tariff_document_response = documents_gateway_client.get_tariff_document(open_credit_card_account_response.account.id)
print('Get tarif document response:', get_tariff_document_response)

# Получить документ контракта
get_contract_document_response = documents_gateway_client.get_contract_document(open_credit_card_account_response.account.id)
print('Get contract document response:', get_contract_document_response)