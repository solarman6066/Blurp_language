import collections

def importer(env):
    def compter(liste):
        return collections.Counter(liste)
    env["compter"] = compter
