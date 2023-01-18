from api import get_data
from db import insert_to_db
from validate import validate_cnpj

def get_cnpj(cnpj_param):
    if not validate_cnpj(cnpj_param):
        print("CNPJ inválido. Por favor, tente novamente.\n")
        return None
    data_list = get_data(cnpj_param)
    for data in data_list:
        if "status" in data and data["status"] == "invalid":
            print(f"Erro: {data['erro']}")
            return None
        insert_to_db(data)
    return data_list


cnpj_param = input("Por favor, digite um CNJP ou digite 'sair' para sair: ")
while cnpj_param != 'sair':
    data_list = get_cnpj(cnpj_param)
    if data_list is not None:
        for data in data_list:
            for key, value in data.items():
                print(f"{key.capitalize()}: {value}")
            print("\n")
        print(f"CNPJ {cnpj_param} registrado no sistema com sucesso.\n")

    cnpj_param = input("Por favor, digite um CNJP ou digite 'sair' para sair: ")
