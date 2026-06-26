# Book API

API для управления книгами и категориями на FastAPI + PostgreSQL.


## Запуск

1. Активировать виртуальное окружение:
    ```
    bash
    source venv/bin/activate
    ```

2. Запустить сервер:
    ```
    bash
    uvicorn app.main:app --reload
    ```

3. Открыть документацию:
    Swagger: http://127.0.0.1:8000/docs
    Health: http://127.0.0.1:8000/health


## Эндпоинты

#### Категории
    - GET /categories/ — список категорий
    - GET /categories/{id} — категория по ID
    - POST /categories/ — создать категорию
    - PUT /categories/{id} — обновить категорию
    - DELETE /categories/{id} — удалить категорию

#### Книги
    - GET /books/ — список книг (фильтр по ?category_id=)
    - GET /books/{id} — книга по ID
    - POST /books/ — создать книгу
    - PUT /books/{id} — обновить книгу
    - DELETE /books/{id} — удалить книгу