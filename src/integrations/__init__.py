from typing import Callable
from typing import List

from .speech_to_text import SPEECH_TO_TEXT_HANDLER

INTEGRATIONS: List[Callable] = []

__all__ = [
    'INTEGRATIONS',
    'SPEECH_TO_TEXT_HANDLER',
]
