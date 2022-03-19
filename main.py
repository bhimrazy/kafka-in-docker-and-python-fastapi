import json
import datetime
from typing import Optional
from fastapi import BackgroundTasks, FastAPI
from producer import publish

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello! , Welcome to my App."}


@app.post("/api/v1/product")
async def api_product(name: str, price: float, background_tasks: BackgroundTasks, description: Optional[str] = None):
    start_time = datetime.datetime.now()
    data = {"item_name": name, "item_price": price,
            "item_description": description}
    background_tasks.add_task(publish, method="create_product", body=data)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = f'{round(time_diff.total_seconds() * 1000)} ms'
    return {'message': 'Success', 'data': data, 'execution_time': execution_time}


@app.get("/api/v1/product")
async def api_product():
    start_time = datetime.datetime.now()
    with open("product.json") as f:
        data = json.load(f)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = f'{round(time_diff.total_seconds() * 1000)} ms'
    return {'message': 'Success', 'data': data, 'execution_time': execution_time}


@app.post("/api/v1/data")
async def api_data(name: str, price: float, background_tasks: BackgroundTasks, description: Optional[str] = None):
    start_time = datetime.datetime.now()
    data = {"item_name": name, "item_price": price,
            "item_description": description}
    background_tasks.add_task(publish, method="create_data", body=data)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = f'{round(time_diff.total_seconds() * 1000)} ms'
    return {'message': 'Success', 'data': data, 'execution_time': execution_time}
