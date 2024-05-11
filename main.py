from model_starter import model_pipeline

from fastapi import FastAPI

from typing import Union

from fastapi import FastAPI, UploadFile
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

    # image = Image(image.file)
    image = Image.open(io.BytesIO(content))

    result = model_pipeline(text, image)
    return {"answer": result}
