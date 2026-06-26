from . import models

from sqlalchemy.orm import Session

from typing import Optional


def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category_by_title(db: Session, title: str):
    return db.query(models.Category).filter(models.Category.title == title).first()


def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def update_category(db: Session, category_id: int, title: str):
    category = get_category(db, category_id)
    if category:
        category.title = title
        db.commit()
        db.refresh(category)
    return category


def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    if category:
        db.delete(category)
        db.commit()
    return category


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100, category_id: Optional[int] = None):
    query = db.query(models.Book)
    if category_id is not None:
        query = query.filter(models.Book.category_id == category_id)
    return query.offset(skip).limit(limit).all()


def update_book(db: Session, book_id: int, book_data: dict):
    book = get_book(db, book_id)
    if book:
        for key, value in book_data.items():
            if value is not None:
                setattr(book, key, value)
        db.commit()
        db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)
    if book:
        db.delete(book)
        db.commit()
    return book


def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    category = get_category(db, category_id)
    if not category:
        print(f"Ошибка: Категория с id {category_id} не найдена.")
        return None

    db_book = models.Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
