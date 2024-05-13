import google.generativeai as genai
import os
import textwrap
from dotenv import load_dotenv
from IPython.display import display
from IPython.display import Markdown

def configure_api():
    # Carrega as variáveis de ambiente do arquivo .env
    load_dotenv()

    # Obtém a chave da API do Google do ambiente
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

    # Configura a chave da API do Google para uso com genai
    genai.configure(api_key=GOOGLE_API_KEY)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

model = genai.GenerativeModel('gemini-pro')