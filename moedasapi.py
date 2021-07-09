import requests
import json


def dolar():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL"
    respostas = requests.get(url)
    dicionario = respostas.json()
    valusdbrl = dicionario['USDBRL']
    valordodolar = valusdbrl['bid']
    valordodolar = float(valordodolar)
    return valordodolar


def euro():
    url = "https://economia.awesomeapi.com.br/last/EUR-BRL"
    respostas = requests.get(url)
    dicionario = respostas.json()
    valeurbrl = dicionario['EURBRL']
    valordoeuro = valeurbrl['bid']
    valordoeuro = float(valordoeuro)
    return valordoeuro
