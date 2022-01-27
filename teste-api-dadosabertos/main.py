from requests import get, codes, exceptions
from time import sleep
from tqdm import tqdm
import pandas as pd

from requests import get, codes, exceptions
import pyuser_agent

ua = pyuser_agent.UA()

header = {'User-Agent': ua.random_broswer()}

def retry(url: str, params: dict, n: int = 3, wait: int = 1):
    """Retorna requisição à `url` com parametros `params`, repetindo a
    requisição por no máximo `n` vezes em caso de falha.
    Args:
        url (str): URL principal a ser requisitada.
        params (dict): Parâmetros da requisição.
        n (int, optional): Número de máximo de tentativas em caso de falha.
        Defaults to 3.
    Returns:
        [type]: [description]
    """

    not_ok = True
    trial = 1
    while not_ok:
        if trial > 1:
            print(f"Requisição falhou. Tentativa {trial-1}, código {x.status_code}.")
            print(f"Aguardando {wait} segundos.")
        try:
            if trial > n:
                break
            sleep(wait)
            x = get(url, params, headers=header)
            not_ok = x.status_code not in [codes.ok] + [500]
            wait += 15 * trial
            trial += 1
        except exceptions.RequestException as err:
            print(
                f"""
            Erro na requisição. Status {x.status_code} após {trial} tentativas.
            Erro: {err}
            """
            )
    return x

def obter_proposicoes_atualizadas(x, last_update: str):
    """Função auxiliar para `consulta_proposicoes_atualizadas`
    Args:
        x: Resposta de um request.get
        last_update (str): Data de referência no formato YYYY-MM-DD
    Returns:
        tuple: (, lista de proposicoes atualizadas)
    """
    from dateutil.parser import parse

    xdata = x.json().get("resultado").get("listaItem")
    datas_ultima_acao = [x.get("atualizacao") for x in xdata]
    atualizar = [parse(x) >= last_update for x in datas_ultima_acao]
    atualizar_todas = all(atualizar)

    if atualizar_todas:
        return xdata, atualizar_todas

    if not atualizar_todas and any(atualizar):
        proposicoes_atualizadas = [x for (x, s) in zip(xdata, atualizar) if s]
        return proposicoes_atualizadas, atualizar_todas

    if not any(atualizar):
        return [], atualizar_todas

def consulta_proposicoes_atualizadas(params: dict, last_update: str):
    """Retorna JSON com dados de proposições atualizadas desde `last_update`.
    Args:
        params (dict): Dicionário com parâmetros de busca para
        https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada
        last_update (str): Data de referência no formato YYYY-MM-DD
    Returns:
        list: Lista com proposições atualizadas
    """

    from dateutil.parser import parse

    url = "https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada"
    params["formato"] = "json"
    params["tp"] = 100
    params["p"] = 1
    params["ord"] = 3

    x = retry(url, params)
    last_update = parse(last_update)
    dados, nextPage = obter_proposicoes_atualizadas(x, last_update)

    while nextPage:
        params["p"] += 1
        res = retry(url, params)
        props, nextPage = obter_proposicoes_atualizadas(res, last_update)
        for p in props:
            dados.append(p)

    return dados

params = {
    "tp": 100,
    "p": 1,
    "ini": "20191201",
    "fim": "20220101"
}

response = consulta_proposicoes_atualizadas(params, "2021-12-31")
df = pd.DataFrame.from_dict(response)
df.to_excel("resposta_api.xlsx")


