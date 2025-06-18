import math

def importer(env):
    def racine(x):
        return math.sqrt(x)
    def puissance(a, b):
        return math.pow(a, b)
    def valeur_absolue(x):
        return abs(x)
    def cosinus(x):
        return math.cos(x)
    def sinus(x):
        return math.sin(x)
    env["racine"] = racine
    env["puissance"] = puissance
    env["valeur_absolue"] = valeur_absolue
    env["cosinus"] = cosinus
    env["sinus"] = sinus
