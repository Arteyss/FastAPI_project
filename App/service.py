import requests
from fastapi import HTTPException


def get_data_from_api(questions_num: int) -> list:
    api_url = f'https://jservice.io/api/random?count={questions_num}'
    response = requests.get(api_url)
    if response.ok:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Data not found")
