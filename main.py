from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import *
from authentication import *

#signals
from tortoise.signals import post_save
from typing import List, Type, Optional
from tortoise import BaseDBAsyncClient

app = FastAPI()

@post_save(User)
async def create_busuness(
    sender: "type[User]",
    instance: User,
    created: bool,
    using_db: "Optional[BaseDBAsyncClient]",
    update_feilds: List[str]
) -> None:
    if created: 
        business_obj = await Business.create(
            business_name = instance.username, owner = instance
        )
        await business_pydantic.from_tortoise_orm(business_obj)
        #send the email

@app.post('/registration')
async def register(user: user_pydanticIn):
    user_info = user.dict(exclude_unset = True)
    user_info["password"] = get_hashed_password(user_info["password"])
    user_obj = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_obj)
    return {
        "status": "ok",
        "data": f"Hello {new_user.username}. Please check your email to confirm your email."
    }


@app.get('/')
def index():
    return {"message": "Hello"}

register_tortoise(
    app,
    db_url= 'sqlite://database.sqlite3',
    modules = {"models": ["models"]},
    generate_schemas= True,
    add_exception_handlers= True
)