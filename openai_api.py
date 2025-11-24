from openai import OpenAI
from joblib import Memory
from pydantic import BaseModel
from Config import MEMCACHE_PATH, DEFAULT_MODEL_NAME, OPENAI_API_KEY
memory = Memory(MEMCACHE_PATH, verbose=0)

@memory.cache
def chat(user_prompt: str, system_prompt: str = None, message_history: list = [], model_name=DEFAULT_MODEL_NAME) -> dict:
    response = batch_chat(n=1, user_prompt=user_prompt, system_prompt=system_prompt, message_history=message_history, model_name=model_name)
    return response.choices[0].message


def batch_chat(n: int, user_prompt: str, system_prompt: str = None, message_history: list = [], model_name=DEFAULT_MODEL_NAME) -> dict:
    client = OpenAI(api_key=OPENAI_API_KEY)
    message_history.extend(format_messages(user_prompt, system_prompt) if system_prompt else format_messages(user_prompt))
    
    response = client.chat.completions.create(
        model=DEFAULT_MODEL_NAME,
        messages=message_history,
        n=n
    )
    return response

@memory.cache
def get_formatted_chat_response(response_format: BaseModel, user_prompt: str, system_prompt: str = None) -> BaseModel:
    """
    Example response_format:
    class Recipe(BaseModel):
        name: str
        ingredients: list[str]
    """
    client = OpenAI(api_key=OPENAI_API_KEY)

    response = client.responses.parse(
        model=DEFAULT_MODEL_NAME,
        input=format_messages(user_prompt, system_prompt) if system_prompt else format_messages(user_prompt),
        text_format=response_format,
    )
    return response.output_parsed

client = OpenAI(api_key=OPENAI_API_KEY)
    
def format_messages(user_prompt: str, system_prompt: str = "You are a helpful assistant.") -> list[dict]:
    assert isinstance(user_prompt, str), "User prompt must be a string."
    assert isinstance(system_prompt, str), "System prompt must be a string."
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]


if __name__=='__main__':
    message_reply = chat(user_prompt="Count up by only one integer in your reply. Starting count is 1", system_prompt="You are a helpful assistant.")
    print(message_reply)
