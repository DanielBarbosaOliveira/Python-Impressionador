from google import genai
from chaves import chave_gemini

client = genai.Client(api_key=chave_gemini)

for modelo in client.models.list():
    print(modelo.name)