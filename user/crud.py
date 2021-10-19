# from datetime import datetime, timedelta
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from sqlalchemy.orm import Session
# from fastapi import FastAPI
# from . import models, schemas

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# def get_password_hash(password):
#     return pwd_context.hash(password)


# def verify_password(password, hashed_password):
#     return pwd_context.verify(password, hashed_password)


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_user_by_full_name(db: Session, full_name: str):
#     return db.query(models.User).filter(models.User.full_name == full_name).first()


# def get_user_by_username(db, username: str):
#     return db.query(models.User).filter(models.User.username == username)


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = models.User(
#         email=user.email,
#         full_name=user.full_name,
#         username=user.username,
#         hashed_password=get_password_hash(user.password),
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def authenticate_user(db, username: str, password: str):
#     user = get_user_by_username(db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.password):
#         return False
#     return user


# # def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
# #     to_encode = data.copy()
# #     if expires_delta:
# #         expire = datetime.utcnow() + expires_delta
# #     else:
# #         expire = datetime.utcnow() + timedelta(minutes=15)
# #     to_encode.update({"exp": expire})
# #     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
# #     return encoded_jwt
