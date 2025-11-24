from openai_api import chat
import pyperclip
import os


with open(os.path.join(os.path.dirname(__file__), 'system_prompt.txt'), 'r') as f:
    SYSTEM_PROMPT = f.read()


def say_no(input_text: str) -> str:
    response = chat(user_prompt=input_text, system_prompt=SYSTEM_PROMPT)
    return response


if __name__ == '__main__':
    # import os
    # with open(os.path.join(os.path.dirname(__file__), 'test_input.txt'), 'r') as f:
    #     test_input = f.read()

    test_input = pyperclip.paste()
    result = say_no(test_input)
    print(result.content)
    pyperclip.copy(result.content)