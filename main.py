import uvicorn
from fastapi import FastAPI
from user.database import engine
from user import models
from user.routers import authentication, user

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(authentication.router)


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)
