import requests

def importer(env):
    def requete_http(url):
        return requests.get(url).status_code
    env["requete_http"] = requete_http
