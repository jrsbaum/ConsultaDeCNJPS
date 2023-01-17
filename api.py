import requests
from cfg import api1


# from cfg import api2

def get_res_api(cnpj):
    url1 = f"{api1}{cnpj}"
    # url2 = f"{api2}{cnpj}/json"

    resp = requests.get(url1)

    if resp.status_code == 200:
        data = resp.json()
        return data

    else:
        return {"erro": "Não foi possível obter as informações do CNPJ"}


