import pathlib

def importer(env):
    def chemin_courant():
        return str(pathlib.Path("."))
    env["chemin_courant"] = chemin_courant
