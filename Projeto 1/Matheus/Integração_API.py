# A integração dessa API está servindo somente de teste para conexão ao banco.

# importação das bibliotecas.
import pandas as pd
from pandas.io.sql import to_sql
from sqlalchemy import create_engine, types
import json
import requests

# URL para fazer a requisição da API.
url = "https://covid-api.mmediagroup.fr/v1/cases"

# Cabeçalhos de autenticação, nesse caso essa API não exige uma autenticação, portanto estão vazias.
payload={}
headers = {}

# Faz a chamada da API com o método request da bilbioteca requests.
# OBS.: Estamos passando o método GET na chamada da API, isso indica que estamos solicitando somente um retorno de informação.
retorno = requests.request("GET", url, headers=headers, data=payload)

# Do retorno que foi recebido e jogado em memória dento da variável retorno queremos somente o valor em texto, por isso passamos o parâmetro ".text".
dados = retorno.text

# Carregamos e transformamos o texto para o formato Json com a função loads() da biblioteca json.
dados = json.loads(dados)

# Criamos uma lista vazia para armazenamento da primeira posição do JSON
lista = []

# Aberto o laço de repetição "for" para transitar em todos os registros do JSON e popular a lista que criamos acima.
for i in dados:
    lista.append(i) # A função append concatena os registros já existentes com o registro novo de cada iteração no loop.  

data_frame = pd.DataFrame(lista) # Criamos um DataFrame com base na lista que criamos.

# Cria a engine/método de conexão para conectar ao mysql instalado localmente
conn = create_engine('mysql+mysqlconnector://root:12345@localhost/staging', connect_args={'auth_plugin': 'mysql_native_password'})

# Método to_sql transforma o DataFrame em um insert automaticamente, passando a engine criada acima para conectar ao banco
to_sql(data_frame, 'PAIS', conn, schema='staging', if_exists='append')




