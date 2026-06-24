from sqlalchemy.orm import Session

from . import models


def create_category(db: Session, title: str):
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category_by_title(db: Session, title: str):
    return db.query(models.Category).filter(models.Category.title == title).first()


def get_all_categories(db: Session):
    return db.query(models.Category).all()


def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
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


def get_books_by_category(db: Session, category_id: int):
    return db.query(models.Book).filter(models.Book.category_id == category_id).all()


def get_all_books(db: Session):
    return db.query(models.Book).all()
