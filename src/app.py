import requests
import json

# Configurações
service_name = "SEU_SERVICO"
index_name = "coffee-reclamacoes-index"
api_key = "SUA_CHAVE_API"

# Endpoint
url = f"https://{service_name}.search.windows.net/indexes/{index_name}/docs/search?api-version=2021-04-30-Preview"

# Consulta
payload = {
    "search": "café",
    "orderby": "data desc"
}

headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
print(response.json())
