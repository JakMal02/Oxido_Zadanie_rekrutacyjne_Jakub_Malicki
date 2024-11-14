import openai
import time
from dotenv import load_dotenv
import os

load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "You are helpful assistant"},
]

artykul = open("tresc_artykulu.txt", "r")
prompt = open("prompt.txt", "r")
text = prompt.read() + "\n" + artykul.read()

print("Czy chcesz przeksztalcic tresc artykulu z pliku na HTML gotowy do wklejenia w sekcji <body>? \t t/n")
odp = input()

if (odp == "n"):
    print("Przerywam dzialanie programu")
    exit()

if (odp == "t"):

    print("User: " + text)
    message = text
    
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
    try:
        chat = openai.ChatCompletion.create(
            model="gpt-4o", messages=messages
        )

        reply = chat.choices[0].message.content
        print(f"ChatGPT: {reply}")
        messages.append({"role": "assistant", "content": reply})