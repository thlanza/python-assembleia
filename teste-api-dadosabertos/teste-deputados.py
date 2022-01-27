from utils import retornarlistas
import pandas as pd

id = 26143
ano = 2021

def pesquisa_deputados_legislatura_atual():

    url = "https://dadosabertos.almg.gov.br/ws/deputados/situacao/1"

    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./deputados/pesquisa_deputados_legislatura_atual.xlsx')

def registro_deputado():

    url = f'https://dadosabertos.almg.gov.br/ws/deputados/{id}'
    response = retornarlistas(url)
    df = pd.DataFrame.from_dict(response)
    df.to_excel(r'./deputados/registro_deputado.xlsx')

def partido_deputado_ano():
    # Partido da Andréia de Jesus em 2021
    url = f'https://dadosabertos.almg.gov.br/ws/deputados/{id}/partidos/{ano}'
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./deputados/partido_deputado_ano.xlsx')

def lista_deputados_em_exercicio():

    url = "https://dadosabertos.almg.gov.br/ws/deputados/em_exercicio"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./deputados/lista_deputados_em_exercicio.xlsx')

def lista_deputados_renunciaram():

    url = "https://dadosabertos.almg.gov.br/ws/deputados/que_renunciaram"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./deputados/que_renunciaram.xlsx')

def lista_deputados_afastaram():
    # retorna vazio
    url = "https://dadosabertos.almg.gov.br/ws/deputados/que_se_afastaram"
    response = retornarlistas(url)
    print(response)

def lista_deputados_perderam_mandato():
    # retorna vazio
    url = "https://dadosabertos.almg.gov.br/ws/deputados/que_perderam_mandato"
    response = retornarlistas(url)
    print(response)

def lista_telefonica_deputados():

    url = "https://dadosabertos.almg.gov.br/ws/deputados/lista_telefonica"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./deputados/lista_telefonica_deputados.xlsx')

def lista_participacoes_comissoes_legislatura_atual():

    url = f'https://dadosabertos.almg.gov.br/ws/deputados/{id}/participacoes_comissoes'
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./deputados/lista_participacoes_comissoes_legislatura_atual.xlsx')

def lista_deputados_quantitativo_proposicoes():

    url = "https://dadosabertos.almg.gov.br/ws/deputados/proposicoes/sumario"
    response = retornarlistas(url)
    list = response['list']
    df = pd.DataFrame.from_dict(list)
    df.to_excel(r'./deputados/lista_deputados_quantitativo_proposicoes.xlsx')

lista_deputados_quantitativo_proposicoes()


