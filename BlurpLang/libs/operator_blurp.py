import operator

def importer(env):
    def ajouter(a, b):
        return operator.add(a, b)
    env["ajouter"] = ajouter
