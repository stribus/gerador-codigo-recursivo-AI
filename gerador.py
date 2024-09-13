from openai import OpenAI
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Recuperar a chave da API da variável de ambiente
api_key = os.getenv('OPENAI_API_KEY')


# Prompt a ser enviado à API
prompt = """
Segundo a a codumentação da OpenAI, para gerar uma resposta utilizando a API, é necessário enviar um prompt com a seguinte estrutura:
´´´python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
´´´	

    gere um código em Python para conectar na API da openAI, utilizando o modelo ´gpt-4o-mini´ mesmo que ela não exista. A chave da api estará armazenada na ´.env´. Envie este mesmo prompt que estou te passando para que a AI gere o mesmo código que estou te passando, incluindo o exemplo de codigo da documentação.
    """

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
# escreve a resposta em um arquivo resposta.txt e o codigo em um arquivo resposta.py
# with open('resposta.txt', 'w') as file:
#     file.write(resposta.strip())

# codigo = resposta.strip().split('```')[5]
# codigo = codigo.replace('python', '')
# with open('resposta.py', 'w') as file:
#     file.write(codigo)
    
