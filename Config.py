MEMCACHE_PATH = '/home/scholar/say_no/.cache/'
DEFAULT_MODEL_NAME = 'gpt-5-nano'
WORKSPACE_PATH = '/home/scholar/say_no'

def get_openai_api_key() -> str:
    import os
    with open(os.path.join(WORKSPACE_PATH, 'openai_key')) as f:
        return f.read().strip()
    
OPENAI_API_KEY = get_openai_api_key()