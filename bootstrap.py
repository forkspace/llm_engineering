import os
from typing import ClassVar

from openai import OpenAI


class OpenAIModelAPI:
    __instance: ClassVar["OpenAIModelAPI"] = None
    __provider: ClassVar[str] = "openrouter"
    __models: ClassVar[dict[str, dict[str, str]]] = {
        "auto": {
            "openrouter": "auto",
            "marketplace": "gpt-5-nano",
        },
        "claude": {
            "openrouter": "anthropic/claude-sonnet-5.5",
            "marketplace": "anthropic_claude_sonnet_5_5",
        },
        "claude-small": {
            "openrouter": "anthropic/claude-haiku-4.5",
            "marketplace": "anthropic_claude_haiku_4_5_v1_0",
        },
        "gpt-small": {
            "openrouter": "openai/gpt-5-nano",
            "marketplace": "openai_gpt5_nano",
        },
        "gpt": {
            "openrouter": "openai/gpt-5.6-luna",
            "marketplace": "openai_gpt56_luna",
        },
        "gemini": {
            "openrouter": "google/gemini-3-flash-preview",
            "marketplace": "gemini_3_flash",
        },
        "gemini-small": {
            "openrouter": "google/gemini-3.5-flash-lite",
            "marketplace": "gemini_2_5_flash_lite",
        },
        "grok": {
            "openrouter": "x-ai/grok-4.3",
            "marketplace": "xai_grok_4_1_fast_reasoning_azure",
        },
        "grok-small": {
            "openrouter": "x-ai/grok-4.3:batch",
            "marketplace": "xai_grok_4_1_fast_reasoning_azure",
        },
        "deepseek": {
            "openrouter": "deepseek/deepseek-v4-flash-0731",
            "marketplace": "deepseek_v4_flash_azure",
        },
        "deepseek-small": {
            "openrouter": "deepseek/deepseek-r1-0528",
            "marketplace": "deepseek_v4_flash_azure",
        },
    }

    @staticmethod
    def get_model(model: str, small: bool = True) -> str:
        key = model
        if small:
            key += "-small"
        return OpenAIModelAPI.__models[key][OpenAIModelAPI.__provider]

    @staticmethod
    def _instance():
        if OpenAIModelAPI.__instance is None:
            OpenAIModelAPI.__instance = OpenAIModelAPI()
        return OpenAIModelAPI.__instance

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
        self._api_key: str = os.getenv("OPENROUTER_API_KEY") # pyright: ignore[reportAttributeAccessIssue]
        self._model: str = "auto"

        api_url_w = os.getenv("NN_AI_MARKETPLACE_API")
        if api_url_w is not None:
            OpenAIModelAPI.__provider = "marketplace"
            self._api_url = api_url_w
            self._api_key = os.getenv("NN_AI_MARKETPLACE_API_TOKEN")  # pyright: ignore[reportAttributeAccessIssue, reportAssignmentType]
            self._model = "gpt-5-nano" # "openai_gpt4o_mini"  # "openai_gpt6_luna"

        self._api = OpenAI(base_url=self._api_url, api_key=self._api_key)
        self._model = OpenAIModelAPI.__models["auto"][OpenAIModelAPI.__provider]

    
