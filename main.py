import openai
import time
from dotenv import load_dotenv
import os

load_dotenv

openai.api_key = os.getenv("OPENAI_API_KEY")

messagees = [
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