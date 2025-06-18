import functools

def importer(env):
    def somme(liste):
        return functools.reduce(lambda x, y: x+y, liste)
    env["somme"] = somme
