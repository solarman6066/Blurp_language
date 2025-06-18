import socket
import urllib.request
import http.client

def importer(env):
    def nom_machine():
        return socket.gethostname()
    def classe_https():
        return str(http.client.HTTPSConnection)
    def url_ouvrir(url):
        return urllib.request.urlopen(url).read().decode("utf-8")
    env["nom_machine"] = nom_machine
    env["classe_https"] = classe_https
    env["url_ouvrir"] = url_ouvrir
