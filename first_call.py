# pip install python-dotenv
#For this file you need to add a credits in the open AI API key in the .env file. The key is not included in this repo for security reasons. You can get your own key from https://platform.openai.com/account/api-keys
from dotenv import load_dotenv
# pip install openai
from openai import OpenAI
load_dotenv()                 # loads everything from .env

client = OpenAI()   # reads your API key from the environment

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user",   "content": "Suggest one thing to do in Chennai."},
    ],
)
print(response.choices[0].message.content)


# now OpenAI() finds the key automatically — no key in your code 🎉