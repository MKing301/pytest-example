import requests
from rich import print, pretty


pretty.install()


def get_json(url):
    """Takes a URL, and returns the JSON."""
    r = requests.get(url)
    return r.json()


print(get_json('https://httpbin.org/get'))
