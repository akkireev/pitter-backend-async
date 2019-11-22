from aiohttp import web
from aiohttp_apispec import docs
from aiohttp_apispec import request_schema
from aiohttp_apispec import response_schema

from exceptions import SpeechRecognitionError
from integrations.speech_to_text import speech_to_text_handler
from schemas import SpeechRecognizeRequestSchema
from schemas import SpeechRecognizeResponseSchema


@docs(
    tags=['Pitter: speech'], summary='Запрос перевода', description='Описание запроса',
)
@request_schema(SpeechRecognizeRequestSchema)
@response_schema(SpeechRecognizeResponseSchema)
async def recognize_speech(request):
    """
    Переводит речь в текст
    :param request:
    :return:
    """
    try:
        speech_transcription: str = await speech_to_text_handler.recognize_speech(
            storage_file_path=request['data']['storage_file_path'],
            language_code=request['data']['language_code']
        )

        res = dict(
            speech_transcription=speech_transcription,
        )

        validated_text_transcription = SpeechRecognizeResponseSchema().load(res)

        return web.json_response(validated_text_transcription)

    except Exception as e:
        raise SpeechRecognitionError()
