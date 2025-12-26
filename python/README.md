# To-Do CRUD API

Минимальное CRUD API для управления личными задачами с приоритетами и статусом выполнения.

## Установка

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

## API Endpoints

После запуска сервера API будет доступно по адресу: `http://127.0.0.1:8000/api/`

### Основные эндпоинты:

- `GET /api/tasks/` - получить список всех задач
- `POST /api/tasks/` - создать новую задачу
- `GET /api/tasks/{id}/` - получить задачу по ID
- `PUT /api/tasks/{id}/` - обновить задачу (полное обновление)
- `PATCH /api/tasks/{id}/` - частично обновить задачу
- `DELETE /api/tasks/{id}/` - удалить задачу

### Пример создания задачи:

```json
{
    "title": "Изучить Django REST Framework",
    "description": "Изучить основы DRF",
    "status": "pending",
    "priority": "high",
    "due_date": "2024-12-31T23:59:59Z"
}
```

### Статусы задач:
- `pending` - Ожидает выполнения
- `in_progress` - В процессе
- `completed` - Завершена

### Приоритеты:
- `low` - Низкий
- `medium` - Средний
- `high` - Высокий

## Тестирование

Используйте интерфейс DRF в браузере по адресу `http://127.0.0.1:8000/api/tasks/` или инструменты типа Postman/curl.

