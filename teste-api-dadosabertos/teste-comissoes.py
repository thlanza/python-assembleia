from requests import get, codes, exceptions
import pyuser_agent
import pandas as pd

ua = pyuser_agent.UA()

header = {'User-Agent': ua.random_broswer()}

def retornarlistas(url):
    url = url

    params = {}
    params["formato"] = "json"


    x = get(url,params=params, headers=header)
    return x.json()


def tiposdecomissoes():

    url = "	https://dadosabertos.almg.gov.br/ws/comissoes/tipos"

    retornarlistas(url)

def listadecomissoes():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/lista"

    retornarlistas(url)

def listadecomissoespermanente():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/permanentes"

    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel("comissoes-permanentes.xlsx")


def comissoes_especiais_indicacao():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/especiais_indicacao"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel("comissoes-especiais-indicacao.xlsx")

def comissoes_especiais_estudo():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/especiais_estudo"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel("comissoes-especiais-estudo.xlsx")

def comissoes_especiais_propostas_emendas_constituicao():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/especiais_estudo"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel("comissoes-especiais-propostas-emendas-constituicao.xlsx")

def comissoes_especiais_vetos_governador():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/especiais_vetos_governador"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel("comissoes-especiais-vetos-governador.xlsx")

def lista_cipes():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/cipes"
    response = retornarlistas(url)
    print(response)

def comissoes_extraordinarias():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/extraordinarias"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel("comissoes-extraordinarias.xlsx")



def cpis():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/cpi"
    response = retornarlistas(url)
    print(response)

# //cpis: proibido

def registro_de_comissao():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/1197"
    response = retornarlistas(url)
    df = pd.DataFrame.from_dict(response)
    df.to_excel("registro_de_comissao_1197.xlsx")

def pesquisa_direcionada_comissoes():

    url = "https://dadosabertos.almg.gov.br/ws/comissoes/pesquisa"

    params = {}
    params["formato"] = "json"
    params["ini"] = "20200101"
    params["fim"] = "20220111"
    params["expr"] = "indic"

    x = get(url, params=params, headers=header)
    xjson = x.json()
    array = xjson["list"]
    df = pd.DataFrame.from_dict(array)
    df.to_excel("pesquisa-direcionada.xlsx")

pesquisa_direcionada_comissoes()








