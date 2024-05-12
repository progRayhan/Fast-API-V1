from fastapi import FastAPI

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
