from typing import Dict

from aiohttp import ClientResponse

from integrations.speech_to_text.base import SpeechToTextBase, Language

from settings import REMOTE_STORAGE_BUCKET_NAME, REMOTE_STORAGE_API_KEY


class Google(SpeechToTextBase):
    url = f"https://speech.googleapis.com/v1/speech:recognize?key={REMOTE_STORAGE_API_KEY}"
    languages = {
        Language.RU: "ru-RU",
        Language.EN: "en-US"
    }

    def create_request_data(self, storage_file_path: str, language_code: Language) -> Dict:
        config = {
            "languageCode": self.languages[language_code]
        }
        audio = {
            "uri": f"gs://{REMOTE_STORAGE_BUCKET_NAME}/{storage_file_path}"
        }

        return {
            "config": config,
            "audio": audio
        }

    def create_request_headers(self, storage_file_path: str, language_type: Language) -> Dict:
        pass

    async def get_text_from_response(self, response: ClientResponse) -> str:
        data = await response.json()
        alternatives = data["results"][0]["alternatives"]
        best_alternative = alternatives[0]
        return best_alternative["transcript"]
