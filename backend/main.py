from fastapi import FastAPI
from enum import Enum

app = FastAPI()


@app.get("/")
async def product_list():
    data = [
        {
        "name": "Iphone 14 pro",
        "qty":1,
        "price": 1000
    },
    {
        "name": "Iphone 15 pro max",
        "qty":1,
        "price": 1500
    }
    ]
    return data


@app.get("/{order_id}")
async def product_details(order_id):
    data = {
        "product_name": "Lenovo",
        "order_id": order_id
    }
    return data


class ConstantValueEnum(Enum):
    """Enum will set constant value."""
    django = "django"
    fastapi = "fastapi"
    flask = "flask"


@app.get("/language/{language_list}")
async def programming_language_list(language_list: ConstantValueEnum):
    if language_list == ConstantValueEnum.django:
        return {"message": f"language is {ConstantValueEnum.django.value}"}
    if language_list == ConstantValueEnum.fastapi:
        return {"message": f"language is {ConstantValueEnum.fastapi.value}"}
    if language_list == ConstantValueEnum.flask:
        return {"message": f"language is {ConstantValueEnum.flask.value}"}
