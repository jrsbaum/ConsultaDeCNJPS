# ConsultaDeCNJPS
### Descrição: Consulta CNPJS em duas APIs, compara qual melhor resultado e insere ele no banco de dados.

## Documentação

```
get_cnpj(cnpj_param)
```
##### Esta função é responsável por obter as informações do CNPJ a partir da API, armazená-las em um dicionário e inserí-las no banco de dados. Se a API retorna uma mensagem de erro, a função retorna "None".

```
get_res_api(cnpj)
```

##### Esta função é usada para obter informações sobre um CNPJ de uma API. 
##### Começa definindo a variável `url1` concatenando a variável `api1` e o `CNPJ` passado como parâmetro para a função. Em seguida, ele usa a biblioteca `requests` para enviar uma solicitação `GET` à API usando a variável `url1`. A resposta é armazenada na variável `resp`. 

```
get_res_api(cnpj)
```

#### Esta função é usada para inserir informações de um CNPJ em um banco de dados MongoDB.
#### Ela começa criando uma conexão com o banco de dados usando a chave `mongo_client_key` fornecida e cria uma referência à coleção de `CNPJS` no banco de dados.
#### Em seguida, tenta inserir as informações do `CNPJ` passado como parâmetro na coleção usando o método `insert_one(cnpj)`.

___

### Para o código funcionar, precisa de um arquivo cfg.py que não foi versionado.

### O arquivo contém o seguinte código:

```
mongo_client_key = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]"
api1 = "https://url_de_exemplo.com.br/"
```

#### Substitua o valor de `mongo_cliente_key` pela sua chave no MongoDB.
#### Substitua o valor de `api1` pela api que será usada.