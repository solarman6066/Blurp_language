import os

def importer(env):
    def nom_os():
        return os.name
    def dossier_courant():
        return os.getcwd()
    env["nom_os"] = nom_os
    env["dossier_courant"] = dossier_courant
