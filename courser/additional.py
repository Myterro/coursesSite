import requests
import json


def generate_country_list():
    countries = []
    try:
        r = requests.get('https://restcountries.eu/rest/v2/all')
        for element in json.loads(r.content):
            countries.append((element['name'], element['name']))
    except requests.exceptions.ConnectionError:
        countries.append(("Poland", "Poland"))
    return countries
