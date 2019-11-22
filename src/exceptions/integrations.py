from exceptions import ServerError


class SpeechRecognitionError(ServerError):
    status_code = 500
    message = 'Ошибка распознавания текста'
