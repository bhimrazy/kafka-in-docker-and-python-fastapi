from typing import Optional
from fastapi import BackgroundTasks, FastAPI
from producer import publish

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello! , Welcome to my App."}


@app.post("/api")
async def api(name: str, price: float, background_tasks: BackgroundTasks, description: Optional[str] = None):
    data = {"item_name": name, "item_price": price,
            "item_description": description}
    background_tasks.add_task(publish, method='create_product', body=data)
    return data
