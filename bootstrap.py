import os
from typing import ClassVar

from openai import OpenAI


class OpenAIModelAPI:
    __instance: ClassVar["OpenAIModelAPI"] = None

    @staticmethod
    def _instance():
        if OpenAIModelAPI._OpenAIModelAPI__instance is None:
            OpenAIModelAPI._OpenAIModelAPI__instance = OpenAIModelAPI()
        return OpenAIModelAPI._OpenAIModelAPI__instance

    @staticmethod
    def api():
        return OpenAIModelAPI._instance()._api

    @staticmethod
    def api_url():
        return OpenAIModelAPI._instance()._api_url

    @staticmethod
    def api_key():
        return OpenAIModelAPI._instance()._api_key

    @staticmethod
    def model():
        return OpenAIModelAPI._instance()._model

    def __init__(self):

        self._api_url: str = "https://openrouter.ai/api/v1"
        self._api_key: str = os.getenv("OPENROUTER_API_KEY")
        self._model: str = "auto"

        api_url_w = os.getenv("NN_AI_MARKETPLACE_API")
        if api_url_w is not None:
            self._api_url = api_url_w
            self._api_key = os.getenv("NN_AI_MARKETPLACE_API_TOKEN")  # pyright: ignore[reportAssignmentType]
            self._model = "openai_gpt_nano_latest"  # "openai_gpt6_luna"

        self._api = OpenAI(base_url=self._api_url, api_key=self._api_key)
