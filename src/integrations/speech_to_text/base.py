from typing import Dict

import logging
from aiohttp import ClientSession, ClientResponse


class Language:
    RU = "ru"
    EN = "en"

    @classmethod
    def validate_language_code(cls, language_code: str):
        return language_code in [value for name, value in vars(cls).items() if name.isupper()]


class SpeechToTextBase:
    url = None
    languages = None

    async def recognize_speech(self, storage_file_path: str, language_code: Language) -> str:
        try:
            request_data = self.create_request_data(storage_file_path, language_code)
            request_headers = self.create_request_headers(storage_file_path, language_code)
            async with ClientSession() as session:
                async with session.post(self.url, json=request_data, headers=request_headers) as response:
                    return await self.get_text_from_response(response)

        except Exception as e:
            logging.exception(e)
            raise

    def create_request_data(self, storage_file_path: str, language_type: Language) -> Dict:
        raise NotImplementedError("create_request_data method must be implemented")

    def create_request_headers(self, storage_file_path: str, language_type: Language) -> Dict:
        raise NotImplementedError("create_request_header method must be implemented")

    async def get_text_from_response(self, response: ClientResponse) -> str:
        raise NotImplementedError("get_text_from_response method must be implemented")
