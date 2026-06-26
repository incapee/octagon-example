from fastapi import APIRouter, Depends, HTTPException, status, Query

from sqlalchemy.orm import Session

from typing import List, Optional

from ..db.db import get_db
from ..db import crud
from .. import schemas


router = APIRouter(prefix="/books", tags=["books"])


@router.get("/", response_model=List[schemas.BookResponse])
def read_books(
    skip: int = 0,
    limit: int = 100,
    category_id: Optional[int] = Query(None, description="Фильтр по категории"),
    db: Session = Depends(get_db)
):
    books = crud.get_books(db, skip=skip, limit=limit, category_id=category_id)
    return books


@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/", response_model=schemas.BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    category = crud.get_category(db, book.category_id)
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")

    return crud.create_book(
        db,
        title=book.title,
        description=book.description,
        price=book.price,
        url=book.url,
        category_id=book.category_id
    )


@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    if book.category_id is not None:
        category = crud.get_category(db, book.category_id)
        if not category:
            raise HTTPException(status_code=400, detail="Category not found")

    update_data = book.dict(exclude_unset=True)
    db_book = crud.update_book(db, book_id, update_data)
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = crud.delete_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return None
