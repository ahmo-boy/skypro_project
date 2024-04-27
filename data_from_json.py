import zipfile
import json

# Путь к zip архиву
zip_file_path = "operations.zip"

# Имя файла внутри архива
json_file_name = "operations.json"

# Открываем zip архив для чтения
with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
    # Извлекаем JSON файл из архива
    with zip_ref.open(json_file_name) as json_file:
        # Читаем данные из JSON файла
        data = json.load(json_file)
