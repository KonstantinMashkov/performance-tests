import httpx

# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

# print(response.status_code)  # 200
# print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}


# import httpx

# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }

# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

# print(response.status_code)  # 201 (Created)
# print(response.json())       # Ответ с созданной записью


# header = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("https://httpbin.org/get", headers=header)

# print(response.json())
# print(response.status_code)

# params = {
#     "userId": 1
# }
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

# print(response.json())
# print(response.status_code)


# # Открываем файл с указанием имени файла в строковом формате
# with open("httpx/example.txt", "rb") as file:
#     # Формируем словарь с файлом
#     files = {"file": ("httpx/example.txt", file)}
    
#     # Отправляем POST-запрос с передачей файла
#     response = httpx.post("https://httpbin.org/post", files=files)

# # Получаем JSON-данные и статус-код ответа
# print(response.json())
# print(response.status_code)

# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

# print(response1.json())  # Данные первой задачи
# print(response2.json())  


# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()  # Вызовет исключение при 4xx/5xx
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка запроса: {e}")
    
    
try:
    response = httpx.get("https://httpbin.org/delay/5")
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")