# To-Do

1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Запустите сервер:
```bash
python manage.py runserver
```

## Эндпоинты

После запуска сервера API будет доступно по адресу: `http://127.0.0.1:8000/api/`

### Основные эндпоинты:

- `GET /api/tasks/` - получить список всех задач
- `POST /api/tasks/` - создать новую задачу
- `GET /api/tasks/{id}/` - получить задачу по ID
- `PUT /api/tasks/{id}/` - обновить задачу (полное обновление)
- `PATCH /api/tasks/{id}/` - частично обновить задачу
- `DELETE /api/tasks/{id}/` - удалить 

## Тестирование

 `http://127.0.0.1:8000/api/tasks/`



