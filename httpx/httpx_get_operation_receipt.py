import time
import httpx

# Шаг 1: создаём пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

# Шаг 2: открываем кредитный счёт
open_credit_card_account_payload = {
    "userId": create_user_response_data["user"]["id"]
}
open_credit_card_account_response = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-credit-card-account",
    json=open_credit_card_account_payload
)
open_credit_card_account_response_data = open_credit_card_account_response.json()
print("Open credit card account response:",open_credit_card_account_response_data)
print("Status Code:", open_credit_card_account_response.status_code)

# Шаг 3: Покупка
make_purchase_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": open_credit_card_account_response_data["account"]["cards"][0]["id"],
    "accountId": open_credit_card_account_response_data["account"]["id"],
    "category": "pivo"
}
make_purchase_response = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation", json=make_purchase_payload)
make_purchase_response_data = make_purchase_response.json()
print("Make purchase response:", make_purchase_response_data)
print("Status Code:", make_purchase_response.status_code)

#Шаг 4: Получение чека
get_operation_receipt_response = httpx.get(f"http://localhost:8003/api/v1/operations/operation-receipt/{make_purchase_response_data['operation']['id']}")

print("Get operation receipt response:", get_operation_receipt_response.text)
print("Status Code:", get_operation_receipt_response.status_code)
