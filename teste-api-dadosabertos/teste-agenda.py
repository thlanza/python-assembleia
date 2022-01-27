from utils import retornarlistas
import pandas as pd

def lista_secoes():

    url = "https://dadosabertos.almg.gov.br/ws/agenda/secoes"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./agenda/lista_secoes.xlsx')

def lista_categorias():

    url = "https://dadosabertos.almg.gov.br/ws/agenda/categorias"
    response = retornarlistas(url)
    print(response)

lista_categorias()