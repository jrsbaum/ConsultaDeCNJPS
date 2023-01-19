from api import ApiHandle
from db import Db
from validate import Validate


class GetCnpj:
    def get_cnpj(self, cnpj_param):
        validate_cnpj = Validate().validate_cnpj
        get_data = ApiHandle().get_data
        insert_to_db = Db().insert_to_db
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
