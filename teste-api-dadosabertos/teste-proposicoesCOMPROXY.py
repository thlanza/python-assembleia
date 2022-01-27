import json
from requests import get, codes, exceptions
import pyuser_agent
import pandas as pd
from math import floor
from utils import retornarlistas
from bs4 import BeautifulSoup
from time import sleep
from datetime import date
from config import user, passw, host


http_proxy = f"http://{user}:{passw}@{host}"

proxyDict = {
              "http": http_proxy,
              "https": http_proxy
            }

ua = pyuser_agent.UA()

header = {'User-Agent': ua.random_broswer()}

def lista_proposicoes():
    url = "https://dadosabertos.almg.gov.br/ws/proposicoes/tipos"
    response = retornarlistas(url)
    lista_resultado = response["list"]
    df = pd.DataFrame.from_dict(lista_resultado)
    df.to_excel(r'./proposicoes/lista_proposicoes.xlsx')



def lista_grupos_tipo_proposicao():
    url = "https://dadosabertos.almg.gov.br/ws/proposicoes/gruposTip"
    response = retornarlistas(url)
    print(response)

def situacaoes_proposicao():
    url = "https://dadosabertos.almg.gov.br/ws/proposicoes/situacoe"
    response = retornarlistas(url)
    print(response)

def registro_proposicao_tipo_numero_ano():
    pass

def pesquisa_direcionada():
    url = "https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada"
    params = {}
    params["formato"] = "json"
    params["ini"] = 20140101
    params["fim"] = 20220117
    params["sitTram"] = 0
    params["obj"] = "true"
    data = get(url, params=params, headers=header).json()
    data_resultado = data["resultado"]
    df = pd.DataFrame.from_dict(data_resultado["listaItem"])
    df.to_excel(r'./proposicoes/pesquisa_direcionada.xlsx')

def pesquisa_avancada():
    url = "https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/avancada"
    params = {}
    params["formato"] = "json"
    params["tp"] = 100
    params["p"] = 1
    params["th"] = "false"
    params["ini"] = 20140101
    params["fim"] = 20220117
    params["ord"] = 2
    params["sit"] = 1
    data = get(url, params=params, headers=header).json()
    print(data)

def busca_textos_proposicoes():
    url = "https://dadosabertos.almg.gov.br/ws/proposicoes/textos"
    params = {}
    params["formato"] = "json"
    params["ini"] = 20200101
    params["fim"] = 20210117
    params["tp"] = 100
    params["p"] = 1

    params2 = {}
    params2["formato"] = "json"
    params2["tp"] = 100
    params2["p"] = 1

    def auxiliar_soupify(df):
        for index, value in df["texto"].items():
            soup = BeautifulSoup(value, features="html.parser")
            texto_parseado = soup.get_text()

            # break into lines and remove leading and trailing space on each
            lines = (line.strip() for line in texto_parseado.splitlines())
            # break multi-headlines into a line each
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            # drop blank lines
            final_text = '\n'.join(chunk for chunk in chunks if chunk)
            df["texto"][index] = final_text
        return df

    ultima_pagina = False
    lista_dfs = []
    data = get(url, params=params, headers=header, proxies=proxyDict).json()
    data_resultado = data['resultado']
    lista_item = data_resultado['listaItem']
    df = pd.DataFrame.from_records(lista_item)
    df_final = auxiliar_soupify(df)
    lista_dfs.append(df_final)
    while not ultima_pagina:
        data = get(url, params=params, headers=header, proxies=proxyDict).json()
        data_resultado = data['resultado']
        numero_documentos = data_resultado["noOcorrencias"]
        tamanho_pagina = data_resultado["tamanhoPagina"]
        num_pagina = data_resultado["numPagina"]
        numero_paginas = floor(float(numero_documentos) / float(tamanho_pagina))
        if num_pagina == numero_paginas:
            ultima_pagina = True
        dataframe = data_resultado["listaItem"]
        df2 = pd.DataFrame.from_records(dataframe)
        df2_final = auxiliar_soupify(df2)
        # for index, value in df2["texto"].items():
        #     soup = BeautifulSoup(value, features="html.parser")
        #     texto_parseado = soup.get_text()
        #
        #     # break into lines and remove leading and trailing space on each
        #     lines = (line.strip() for line in texto_parseado.splitlines())
        #     # break multi-headlines into a line each
        #     chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        #     # drop blank lines
        #     final_text = '\n'.join(chunk for chunk in chunks if chunk)
        #     df2["texto"][index] = final_text
        lista_dfs.append(df2_final)
        params["p"] += 1
        print(num_pagina)
    lista_dfs_concatt = pd.concat(lista_dfs)
    to_drop = ['tipoProjeto', 'siglaTipoProjeto', 'numeroDoc', 'atualizacao', 'horario', 'usuario', 'codigo', 'formatoTexto', 'acompanhamento', 'local', 'edicao']
    lista_dfs_concatt.drop(columns=to_drop, inplace=True)
    series_proposicao = lista_dfs_concatt["proposicao"]
    data_ultima_acao = []
    fase = []
    situacao = []
    tempo_decorrido = []
    ementa = []
    autor = []

    for index, value in series_proposicao.items():
        print(index)
        array_valores = value.split(" ")
        tipo_proposicao = array_valores[0]
        tipo_proposicao_replaced = tipo_proposicao.replace(".", "")
        if tipo_proposicao_replaced in ["PL", "PLC", "PRE", "PEC"]:
            numero_proposicao = array_valores[1]
            ano_proposicao = array_valores[2]
            url2 = f"https://dadosabertos.almg.gov.br/ws/proposicoes/{tipo_proposicao_replaced}/{numero_proposicao}/{ano_proposicao}?formato=json"
            data2 = get(url2, params=params2, headers=header, proxies=proxyDict).json()
            resultado2 = data2["resultado"]
            lista_item_2 = resultado2["listaItem"]
            data_ultima_acao_item = lista_item_2[0]["dataUltimaAcao"]
            data_ultima_acao.append(data_ultima_acao_item)
            fase_item = lista_item_2[0]["listaHistoricoTramitacoes"][0]["historico"]
            fase.append(fase_item)
            situaçao_item = lista_item_2[0]["situacao"]
            situacao.append(situaçao_item)
            tempo_inicial = lista_item_2[0]["listaHistoricoTramitacoes"][-1]["data"]
            [ano_ultima_acao, mes_ultima_acao, dia_ultima_acao] = data_ultima_acao_item.split('-')
            [ano_tempo_inicial, mes_tempo_inicial, dia_tempo_inicial] = tempo_inicial.split('-')
            tempo_inicial = date(day=int(dia_tempo_inicial), month=int(mes_tempo_inicial), year=int(ano_tempo_inicial))
            data_ultima_acao_item = date(day=int(dia_ultima_acao), month=int(mes_ultima_acao), year=int(ano_ultima_acao))
            tempo_decorrido_item = (data_ultima_acao_item - tempo_inicial).days
            tempo_decorrido.append(tempo_decorrido_item)
            autor_item = lista_item_2[0]["autor"]
            autor.append(autor_item)
            ementa_item = lista_item_2[0]["ementa"]
            ementa.append(ementa_item)
        sleep(0.55)
    lista_dfs_concatt['Fase'] = fase
    lista_dfs_concatt['Situação'] = situacao
    lista_dfs_concatt['Data Última Ação'] = data_ultima_acao
    lista_dfs_concatt['Tempo Decorrido'] = tempo_decorrido
    lista_dfs_concatt['Autor'] = autor
    lista_dfs_concatt['Ementa'] = ementa
    lista_dfs_concatt.rename(columns={'texto': 'Ementa'}, inplace=True)
    lista_dfs_concatt.to_excel(r'./proposicoes/busca_textos_proposicoes4.xlsx')
    print("CONCLUÍDO")

busca_textos_proposicoes()







