from uuid import uuid4

from aiohttp import web
from aiohttp_apispec import docs
from aiohttp_apispec import request_schema
from aiohttp_apispec import response_schema

from integrations.speech_to_text import speech_to_text_handler
from schemas import SpeechRecognizeRequestSchema
from schemas import SpeechRecognizeResponseSchema


@docs(
    tags=['SMS'], summary='Запрос перевода', description='Описание запроса',
)
@request_schema(SpeechRecognizeRequestSchema)
@response_schema(SpeechRecognizeResponseSchema)
async def recognize_speech(request):
    """
    Отправляет сообщение
    :param request:
    :return:
    """
    try:
        text_transcription: str = speech_to_text_handler.recognize_speech(
            storage_file_path=request.data['storage_file_path'],
            language_code=request.data['language_code']
        )
        return web.json_response({"text_transcription": text_transcription})

    except:
        pass
