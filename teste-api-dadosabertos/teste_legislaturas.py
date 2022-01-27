from utils import retornarlistas
import pandas as pd

num = 19
Id = 26143
num_anterior = 16
sit = 1

def comissoes_legislatura_anterior():

    url = f'https://dadosabertos.almg.gov.br/ws/legislaturas/{num}/comissoes'
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./legislaturas/comissoes_legislatura_anterior.xlsx')

def registro_legislatura():

    url = "https://dadosabertos.almg.gov.br/ws/legislaturas/atual"
    response = retornarlistas(url)
    list = response['legislatura']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./legislaturas/registro_legislatura.xlsx')

def registro_de_deputado():

    url = f'https://dadosabertos.almg.gov.br/ws/legislaturas/{num}/deputados/{Id}'
    response = retornarlistas(url)
    df = pd.DataFrame.from_dict(response)
    df.to_excel(r'./legislaturas/registro_de_deputado.xlsx')

def pesquisa_deputados_legislatura_anterior():

    url = f'https://dadosabertos.almg.gov.br/ws/legislaturas/{num_anterior}/deputados/situacao/{sit}'
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./legislaturas/pesquisa_deputados_legislatura_anterior.xlsx')

pesquisa_deputados_legislatura_anterior()

