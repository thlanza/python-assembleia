import json

from utils import retornarlistas
from requests import get, codes, exceptions
import pyuser_agent
import pandas as pd
import ast

ua = pyuser_agent.UA()

header = {'User-Agent': ua.random_broswer()}

letra = 'A'
id = 25411

def lista_fornecedores():

    url = "https://dadosabertos.almg.gov.br/ws/prestacao_contas/contratos/fornecedores/indexados"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./contratos/lista_fornecedores.xlsx')

def fornecedores_por_letra():

    url = f'https://dadosabertos.almg.gov.br/ws/prestacao_contas/contratos/fornecedores/{letra}'
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./contratos/fornecedores_por_letra.xlsx')

def lista_contratos_indexados():

    url = "https://dadosabertos.almg.gov.br/ws/prestacao_contas/contratos/indexados"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./contratos/lista_contratos_indexados.xlsx')

def registro_contratos():

    url = f'https://dadosabertos.almg.gov.br/ws/prestacao_contas/contratos/{id}'
    params = {}
    params["formato"] = "json"

    data = get(url, params=params, headers=header).text
    data = data.replace(",00", ".00")
    data = json.loads(data)
    list = data['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./contratos/registro_contratos.xlsx')

def pesquisa_direcionada_de_contratos():

    url = "https://dadosabertos.almg.gov.br/ws/prestacao_contas/contratos/pesquisa"
    params = {}
    params["formato"] = "json"
    params["ano"] = 2021
    params["obj"] = "computadores"
    params["tipo"] = "contrato"
    response = get(url, params=params, headers=header)
    x = response.json()
    list = x['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./contratos/pesquisa_direcionada_contratos.xlsx')

pesquisa_direcionada_de_contratos()

