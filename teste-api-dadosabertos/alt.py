from requests import get, codes, exceptions
import pyuser_agent

ua = pyuser_agent.UA()

header = {'User-Agent': ua.random_broswer()}

def scrap():


    params = {}
    params["ano"]= "2021"
    params["tipo"]= "RQN"
    params["num"] = "10212"
    url = "https://dadosabertos.almg.gov.br/ws/proposicoes/pesquisa/direcionada?ano=2021&tipo=RQN&num=10212"

    x = get(url, params, headers=header)
    print(x.json())


scrap()