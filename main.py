from api import get_res_api
from db import insert_to_mongodb


def get_cnpj(cnpj_param):
    data = get_res_api(cnpj_param)

    if "erro" in data:
        return None

    cnpj = {}
    for key in data:
        cnpj[key] = data[key]

    insert_to_mongodb(cnpj)
    return cnpj


cnpj_param = input("Por favor, digite um CNJP (somente números) ou digite 'sair' para sair: ")
while cnpj_param != 'sair':
    endereco = get_cnpj(cnpj_param)
    if endereco is None:
        print("CNPJ inválido. Por favor, tente novamente.\n")
    else:
        for key, value in endereco.items():
            print(f"{key.capitalize()}: {value}")
        print(f"\nCNPJ {cnpj_param} registrado no sistema com sucesso.\n")
    cnpj_param = input("Por favor, digite um CNJP (somente números) ou digite 'sair' para sair: ")


