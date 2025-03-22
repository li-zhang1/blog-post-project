from typing import List
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
import schemas, database
from repository import blog
from oauth2 import get_current_user

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db = database.get_db

@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create(request, db)

@router.get('/', response_model=List[schemas.ShowBolg])
def all(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user) ):
    return blog.get_all(db)


@router.get('/{id}', status_code=200, response_model=schemas.ShowBolg)
def show(id: int, response: Response, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user) ):
    return blog.show(id, response, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user) ):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user) ):
    return blog.destroy(id, db)



