import re


class Validate:

    def validate_cnpj(self, cnpj_param):
        cnpj_param = re.sub("[^0-9]", "", cnpj_param)
        if len(cnpj_param) != 14:
            return False
        primeiro_dv = int(cnpj_param[12])                # primeiro digito verificador
        segundo_dv = int(cnpj_param[13])                 # segundo digito verificador
        pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = 0
        for i in range(12):
            soma += int(cnpj_param[i]) * pesos[i]
        primeiro_dv_calculado = 0 if soma % 11 < 2 else 11 - (soma % 11)
        if primeiro_dv != primeiro_dv_calculado:
            return False
        pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = 0
        for i in range(13):
            soma += int(cnpj_param[i]) * pesos[i]
        segundo_dv_calculado = 0 if soma % 11 < 2 else 11 - (soma % 11)
        if segundo_dv != segundo_dv_calculado:
            return False
        return True
