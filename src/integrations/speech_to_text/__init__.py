from settings import REMOTE_STORAGE_TYPE
from .google import Google

HANDLERS = {
    'GS': Google,
}

SPEECH_TO_TEXT_HANDLER = HANDLERS[REMOTE_STORAGE_TYPE]()
