from views import recognize_speech


def setup_routes(app):
    """
    Устанавливает пути запросов
    :param app:
    """
    app.router.add_post('/api/pitter/v1/speech-recognition', recognize_speech)
