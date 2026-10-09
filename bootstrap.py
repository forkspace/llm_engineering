import os
from typing import ClassVar

from openai import OpenAI


class OpenAIModelAPI:
    __instance: ClassVar["OpenAIModelAPI"] = None

    OPENROUTER_MODEL_AUTO = "auto"
    OPENROUTER_MODEL_CLAUDE = "anthropic/claude-sonnet-5.5"
    OPENROUTER_MODEL_CLAUDE_SMALL = "anthropic/claude-haiku-4.5"
    OPENROUTER_MODEL_GPT_SMALL = "openai/gpt-5-nano"
    OPENROUTER_MODEL_GPT = "openai/gpt-5.6-luna"
    OPENROUTER_MODEL_GPT_OSS = "openai/gpt-oss-120b"
    OPENROUTER_MODEL_GEMINI = "google/gemini-3-flash-preview"
    OPENROUTER_MODEL_GEMINI_SMALL = "google/gemini-3.5-flash-lite"
    OPENROUTER_MODEL_GROK = "x-ai/grok-4.3"
    OPENROUTER_MODEL_GROK_SMALL = "x-ai/grok-4.3:batch"
    OPENROUTER_MODEL_DEEPSEEK = "deepseek/deepseek-v4-flash-0731"
    OPENROUTER_MODEL_DEEPSEEK_SMALL = "deepseek/deepseek-r1-0528"
    

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
            self._model = "gpt-5-nano" # "openai_gpt4o_mini"  # "openai_gpt6_luna"

        self._api = OpenAI(base_url=self._api_url, api_key=self._api_key)

    
