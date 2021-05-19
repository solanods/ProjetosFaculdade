# importação das bibliotecas.
import pandas as pd
from pandas.io.sql import to_sql
from sqlalchemy import create_engine, types
import json
import requests
from itertools import chain
import plotly.express as px

# URL para fazer a requisição da API.
url = "https://covid-api.mmediagroup.fr/v1/cases"
# Faz a chamada da API com o método request da bilbioteca requests.
# OBS.: Estamos passando o método GET na chamada da API, isso indica que estamos solicitando somente um retorno de informação.
retorno = requests.request("GET", url)
# Do retorno que foi recebido e jogado em memória dento da variável retorno queremos somente o valor em texto, por isso passamos o parâmetro ".text".
dados = retorno.text
# Carregamos e transformamos o texto para o formato Json com a função loads() da biblioteca json.
dados = json.loads(dados)
# descompactando os valores do dict 'dados.values()' com a função chain do módulo itertools
df = pd.DataFrame(chain.from_iterable(map(lambda sec: sec.values(), dados.values())))
# remover as colunas que não usaremos
df = df.drop(columns=['sq_km_area', 'life_expectancy', 'elevation_in_meters','continent', 'abbreviation', 'iso', 'capital_city'])
#remover as linhas Nan do campo country
df = df.dropna(subset=['country'])
# formatar o campos updated para o YYYY-MM-DD HH:MM:SS
df['updated'] = pd.to_datetime(df['updated'])
# converter coluna "population" to int64 dtype
df = df.astype({"population": int})

# falta fazer!!!
# tratar valores ausentes
# fazer as métricas
# talvez agrupar por location
# após limpos e tratados mandar para o banco

