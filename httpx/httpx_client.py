import time

import httpx

# Инициализируем клиент с авторизацией
client = httpx.Client(
    base_url="http://localhost:8003",
    timeout=100,
    headers={"Authorization": "Bearer ..."}
)

payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "test_last_name",
    "firstName": "test_first_name",
    "middleName": "test_middle_name",
    "phoneNumber": "test_phone_number"
}

# Выполняем запрос с авторизацией
response = client.post("/api/v1/users", json=payload)
print(response.text)
print(response.headers)

