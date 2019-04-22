# Uppgift 8.2
import requests

def get(url):
    r = requests.get(url)
    response_dictionary = r.json()
    return response_dictionary

