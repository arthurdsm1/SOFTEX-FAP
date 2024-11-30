import requests

def obter_cotacao():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        cotacao_brl = dados['rates']['BRL']
        print(f"A cotação do dólar para o real é: R${cotacao_brl}")
    else:
        print("Erro ao acessar a API!")

obter_cotacao()
