# ConsultaDeCNJPS
#### Descrição: Consulta CNPJS em duas APIs, imprime os resultados e insere eles no banco de dados. Obs.: Este programa usa 2 APIs públicas grátis que tem limite de 3 consultas por minuto.
____

## Documentação

```
InputOptions
```
##### Essa classe gerencia as opções de entrada do usuário. Ele solicita que o usuário selecione a opção 1 ou 2 e, em seguida, chama o método `get_cnpj` da classe 

```
GetCnpj
```
##### Essa classe é responsável por obter os dados do CNPJ a partir de uma ou mais APIs e inseri-los no banco de dados. Ele chama os métodos `validate_cnpj` da classe `Validate`, `get_data` da classe `ApiHandle` e `insert_to_db` da classe `Db` para realizar essas tarefas.

-----
```
Validate
```
##### Essa classe é responsável por validar o CNPJ fornecido pelo usuário. Ele verifica se o CNPJ tem 14 dígitos e se os dígitos verificadores estão corretos.

---
```
ApiHandle
```
##### Essa classe é responsável por lidar com as chamadas à API e retornar os dados do CNPJ.


```
Db
```
##### Essa classe é responsável por lidar com as operações no banco de dados, como inserir os dados do CNPJ

___

### Para o código funcionar, precisa de um arquivo cfg.py que não foi versionado.

### O arquivo contém o seguinte código:

```
mongo_client_key = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]"
api1 = "https://url_de_exemplo.com.br/"
api2 = "https://url_de_exemplo.com.br/"
```

#### Substitua o valor de `mongo_cliente_key` pela sua chave no MongoDB.
#### Substitua o valor de `api1` ou `api2` pela api que será usada.