from fastapi import FastAPI, Body

from utils.find_form import find_suitable_form
from utils.validator import validator

app = FastAPI()


@app.post("/get_form")
def read_item(data=Body()):
    for key, value in data.items():
        data[key] = validator(value)

    result_data = find_suitable_form(data)
    if result_data:
        return result_data
    else:
        return data
