import requests

def obter_usuarios():
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            print(f"Nome: {usuario['name']}, Email: {usuario['email']}")
    else:
        print("Erro ao obter dados")

obter_usuarios()
