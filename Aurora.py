import requests

def main():
    url = "http://localhost:11434/api/generate"
    dados ={

        "model": "llama3.2",
        "prompt": "Olá, tudo bem?",
        "stream": False

      }

    resposta = requests.post(url, json=dados)
    if resposta.status_code == 200:
        dados_resposta = resposta.json()
        print(dados_resposta["response"])

if __name__ == "__main__":
    main()