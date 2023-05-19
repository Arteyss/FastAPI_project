from uuid import uuid4

import requests
from fastapi import HTTPException
from pydub import AudioSegment


def get_data_from_api(questions_num: int) -> list:
    api_url = f'https://jservice.io/api/random?count={questions_num}'
    response = requests.get(api_url)
    if response.ok:
        return response.json()
    else:
        raise HTTPException(status_code=404, detail="Data not found")


def generate_token() -> str:
    return str(uuid4())


def convert_wav_mp3(file):
    if file.content_type != "audio/wav":
        raise HTTPException(status_code=400, detail="Only wav files are allowed")
    file_id = generate_token()
    mp3_path = f"./audio/{file_id}.mp3"

    sound = AudioSegment.from_wav(file.file)
    sound.export(mp3_path, format="mp3")

    return file_id
