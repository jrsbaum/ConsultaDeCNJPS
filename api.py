import requests
from cfg import api1, api2


class ApiHandle:
    def get_data(self, cnpj):
        data_list = []
        for url in [api1, api2]:
            try:
                response = requests.get(f"{url}{cnpj}")
                if response.status_code == 200:
                    data_list.append(response.json())
                else:
                    raise ValueError(response.json()["erro"])
            except ValueError as e:
                data_list.append({"status": "invalid", "erro": e})
        return data_list

