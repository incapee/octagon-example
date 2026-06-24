from db.db import SessionLocal
from db.models import Category, Book


def main():
    db = SessionLocal()

    print("Книги и категории")
    categories = db.query(Category).all()

    for category in categories:
        print(f"Категория: {category.title}")
        books = db.query(Book).filter(Book.category_id == category.id).all()
        if books:
            for book in books:
                print(f"- {book.title} | {book.price} руб. | {book.description}")
        else:
            print("(нет книг)")

    db.close()


if __name__ == "__main__":
    main()
