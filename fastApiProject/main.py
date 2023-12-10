from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


class Item(BaseModel):
    name: str
    description: str
    price: str
    tax: str


@app.post("/item")
async def postuserData(item: Item):

    return {"statusCode": 200, "msg": "Register Successfully","data":item}
