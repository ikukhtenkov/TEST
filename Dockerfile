# Используем образ с Python
From python:3

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем исходный код в контейнер 
Copy main.py/app/main.py

# Запускаем приложение при старте контейнера
CMD ["python", "/app/main.py"]
