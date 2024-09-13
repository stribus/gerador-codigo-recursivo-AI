from openai import OpenAI
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Recuperar a chave da API da variável de ambiente
api_key = os.getenv('OPENAI_API_KEY')


# Prompt a ser enviado à API
prompt = "gere um código em Python para conectar na API da openAI, utilizando o modelo ´gpt-4o´ mesmo que ela não exista. A chave da api estará armazenada na ´.env´. Envie este mesmo prompt que estou te passando para que a AI gere o mesmo código."

# Função para gerar resposta usando a API da OpenAI
def gerar_resposta(prompt):
    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1200,
            stream=False
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

# Enviar o prompt e imprimir a resposta
resposta = gerar_resposta(prompt)
print(resposta.strip())
