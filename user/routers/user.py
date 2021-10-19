from fastapi import APIRouter, status, HTTPException, Depends
from .. import database, schemas, models
from ..hashing import Hash
from sqlalchemy.orm.session import Session

router = APIRouter(tags=["Users"])

get_db = database.get_db


@router.post("/signup", response_model=schemas.ShowUser)
def signup(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(
        full_name=request.full_name,
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/user/{id}", response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with the id {id} is not found",
        )
    return user
