# from model import model_pipeline

from fastapi import FastAPI

from typing import Union

from fastapi import FastAPI
from PIL import Image
import io

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


"""@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}"""


@app.post("/ask")
def ask(text: str, image: UploadFile):
    content = image.file.read()

    image = Image(io.BytesIO(content))
