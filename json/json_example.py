import json

json_data = {"name": "Иван", "age": 30, "is_student": False}
# parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)

# print(parsed_data["name"])  

with open("json\json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Загружаем JSON из файла
    print(data)
    
with open("json\data_json_example.json", "w", encoding="utf-8") as file:
    json.dump(json_data, file, indent=4, ensure_ascii=False)  # Сохраняем JSON в файл
