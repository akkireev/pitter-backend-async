from marshmallow import Schema
from marshmallow import fields

from integrations.speech_to_text.base import Language


class SpeechRecognizeRequestSchema(Schema):
    storage_file_path = fields.Str(required=True, description='Путь к аудио файлу на удаленном хранилище',)
    language_code = fields.Str(required=True, description='Код языка записи в 2 символьном значении',
                               validate=Language.validate_language_code)


class SpeechRecognizeResponseSchema(Schema):
    speech_transcription = fields.Str(required=True, description='Распознаный текст')
