from typing import Union #Allows us to specify optional types like Union[str, None]
from fastapi import FastAPI #Imports FastAPI so we can create an API application
from pydantic import BaseModel #BaseMofel is used to define data validation models

app = FastAPI() #creates an instance of the FastAPI application

#Defines a Pydantic model for the structure of an item
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

#GET endpoints for the root URL
@app.get("/")
def read_root():
    return {"Hello": "World"}

#GET endpoint that retrieves an item by its ID
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q} #returns the item ID and optional query parameter

#PUT endpoint that updates an item by ID
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}