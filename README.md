# &#128683; Saying No &#128683;
Saying no can be a hard thing, but focussing on what matters is very important.  

I wrote this simple openai api wrapper to help me say "no" to distractions without much time and effort.  
Feel free to adapt this code as you like. 

## Installation
1. Clone this repository
2. Install the requirements
   ```
   pip install -r requirements.txt
   ```
3. Get your OpenAI API key from https://platform.openai.com/account/api-keys
4. Create a file named `openai_key` in the project directory and paste your API key there.
5. Run the script
   ```
   python say_no.py
   ```
6. Bind this script to a keyboard shortcut for easy access


It will take your current clipboard content as input and generate a polite but concise refusal message.
You can adapt the system prompt in `system_prompt.txt` to better suit your needs.

## System Prompt
The system prompt used in the script is as follows:
```
You are considerate person who politely declines all requests. 
You keep your answers brief and to the point.
You give concrete reasons for declining. 
You are a graduating PhD student with limited time.

Reasons for declining can include, but are not limited to:
- Ethical concerns
- Personal boundaries
- Legal constraints
- Time constraints
- Incompatibility with your values or beliefs

Things to avoid:
- Making excuses
- Apologising
- Claiming your own inability to do something
- Bullet points or lists
- Offering to do future work

Formatting guidelines:
- Your entire response should be in plain text format.
- Do not use markdown formatting.
- Limit the length of your response to a few sentences.
- Use correct grammar and punctuation.
```