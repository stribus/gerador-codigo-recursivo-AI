from groq import Groq
import os
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv()

# Recuperar a chave da API da variável de ambiente
api_key = os.getenv('GROQ_API_KEY')
model="gemma2-9b-it"



# Prompt a ser enviado à API
prompt = f"""
Segundo a a documentação da GROQ, para gerar uma resposta utilizando a API, é necessário enviar um prompt com a seguinte estrutura:
```python
import os
from groq import Groq

client = Groq( api_key=os.environ.get("GROQ_API_KEY"),)

chat_completion = client.chat.completions.create(
    messages=[
        {{
            "role": "user",
            "content": "Explain the importance of fast language models",
        }}
    ],
    model="{model}",    
    temperature=0.5,
)

print(chat_completion.choices[0].message.content)
```	

Com isso gere um código em Python para conectar na API da GROQ, utilizando o modelo `{model}` mesmo que ela não exista. A chave da api estará armazenada na `.env`. Envie este mesmo prompt que estou te passando para que a AI gere o mesmo código que estou te passando, incluindo o exemplo de codigo da documentação.
    """

# Função para gerar resposta usando a API da OpenAI
def gerar_resposta(prompt):
    try:
        client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1200,
            stream=False,
            temperature=0.5,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"


# Enviar o prompt e imprimir a resposta
resposta = gerar_resposta(prompt)
print(resposta.strip())
# escreve a resposta em um arquivo resposta.txt e o codigo em um arquivo resposta.py
with open('resposta.txt', 'w') as file:
    file.write(resposta.strip())

# codigo = resposta.strip().split('```')[5]
# codigo = codigo.replace('python', '')
# with open('resposta.py', 'w') as file:
#     file.write(codigo)
    
