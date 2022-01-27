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
