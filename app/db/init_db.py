from . import models
from .crud import create_category, create_book
from .db import SessionLocal


def init_db():
    db = SessionLocal()

    models.Base.metadata.create_all(bind=db.get_bind())

    category_names = ["Фантастика", "Научная литература"]
    categories = {}
    for name in category_names:
        existing = db.query(models.Category).filter(models.Category.title == name).first()
        if existing:
            categories[name] = existing
        else:
            categories[name] = create_category(db, name)
        print(f"Категория: {name}")

    books_data = {
        "Фантастика": [
            {"title": "Дюна", "description": "Фантастическая сага Фрэнка Герберта", "price": 1200, "url": ""},
            {"title": "1984", "description": "Роман-антиутопия Джорджа Оруэлла", "price": 850, "url": ""},
            {"title": "Идиот", "description": "Классика Федора Достоевского", "price": 950, "url": ""},
        ],
        "Научная литература": [
            {"title": "Краткая история времени", "description": "Научпоп Стивена Хокинга", "price": 1100, "url": ""},
            {"title": "Думай медленно, решай быстро", "description": "Психология Даниэля Канемана", "price": 1300, "url": ""},
            {"title": "Сапиенс", "description": "Взгляд на эволюцию Юваля Ной Харари", "price": 1400, "url": ""},
        ]
    }

    for category_name, books in books_data.items():
        category = categories.get(category_name)
        if category:
            for book_info in books:
                existing_book = db.query(models.Book).filter(
                    models.Book.title == book_info["title"],
                    models.Book.category_id == category.id
                ).first()
                if not existing_book:
                    create_book(
                        db,
                        title=book_info["title"],
                        description=book_info["description"],
                        price=book_info["price"],
                        url=book_info["url"],
                        category_id=category.id
                    )
                    print(f"Добавлена книга: {book_info['title']}")

    db.close()


if __name__ == "__main__":
    init_db()
    print("БД инициализирована.")
