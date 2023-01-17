# ConsultaDeCNJPS
### Descrição: Consulta CNPJS em duas APIs, compara qual melhor resultado e insere ele no banco de dados.

## Documentação

```
get_cnpj()
```
##### A função `get_cnpj` é usada para buscar e salvar informações de um CNPJ. Ela usa o parâmetro cnpj_param para fazer uma chamada para outra função chamada `get_data`.
##### A função `get_cnpj` então verifica se esses dados contêm um erro, e se sim, imprime uma mensagem e retorna None. Se não houver erro, a função então insere os dados recuperados no banco de dados MongoDB e retorna a lista de objetos de dados.

-----
```
get_data()
```
##### A função `get_data` é usada para buscar informações de um `CNPJ`. Ela usa o parâmetro `cnpj` para fazer uma chamada para duas diferentes `URLs`, `api1` e `api2`. Ela então tenta recuperar a resposta dessas chamadas usando o método `requests.get()`.
##### Se a resposta for bem-sucedida e o status da resposta for `200`, os dados são adicionados à lista de dados. Se ocorrer algum erro ou o status da resposta for diferente de `200`, uma exceção será gerada e uma mensagem de erro será adicionada à lista de dados. A função retorna a lista de dados contendo as informações recuperadas.


---
```
insert_to_db()
```
##### A função `insert_to_db` é usada para inserir dados em um banco de dados. Ela usa o parâmetro `cnpj` como o dado a ser inserido
##### Primeiro, ela tenta criar uma conexão com o banco de dados usando a `chave de cliente` fornecida. Em seguida, ela seleciona a coleção de CNPJs e insere o dado passado como parâmetro. Se ocorrer algum erro ao tentar inserir os dados, uma exceção será gerada e uma mensagem de erro será exibida.

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