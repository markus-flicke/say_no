# Saying No
Saying no is one of the hardest things, but focussing on what matters is very important.  

I wrote this simple openai api wrapper to help me say no to distractions without much time and effort.  
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

It will take your current clipboard content as input and generate a polite but concise refusal message.
You can adapt the system prompt in the `say_no.py` file to better suit your needs.