from get_cnpj_api import GetCnpj


class InputOptions:
    def inputoptions(self):
        opcao = input("Digite 1 se você quer consultar um CNPJ no nosso banco de dados\n"
                      "ou 2 para consultar um CNPJ em duas APIs e inseri-lás em nosso banco de dados: ")
        while opcao != '1' and opcao != '2':
            opcao = input("Por favor, escolha 1 ou 2: ")

        if opcao == "1":
            print("Feature em desenvolvimento..")

        elif opcao == "2":
            cnpj_param = input("Por favor, digite um CNPJ ou digite 'sair' para sair: ")
            while cnpj_param != 'sair':
                data_list = GetCnpj().get_cnpj(cnpj_param)
                if data_list is not None:
                    for data in data_list:
                        for key, value in data.items():
                            print(f"{key.capitalize()}: {value}")
                        print("\n")
                    print(f"CNPJ {cnpj_param} registrado no sistema com sucesso.\n")

                cnpj_param = input("Por favor, digite um CNPJ ou digite 'sair' para sair: ")
