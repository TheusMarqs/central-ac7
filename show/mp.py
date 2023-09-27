import requests


url = 'https://api.mercadopago.com'

#Chave de autenticação
payload = {}
headers = {
    'Authorization': 'TEST-67bae85d-2d4d-4843-8483-beb6dc42385a'
}

#Recuperando as informações
response = requests.request("GET", url, headers=headers, data=payload)

#Bruto recuperado em string
print(response.text)
a = response.text.split(',')