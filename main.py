
from fastapi import FastAPI
import models
from database import engine
from routers import blog, user, authentication


app = FastAPI()

# create all the models into the database.
# migrating/creating all the database tables
models.Base.metadata.create_all(engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

