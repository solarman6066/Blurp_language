import random

def importer(env):
    def entier_entre(a, b):
        return random.randint(a, b)
    def choisir(lst):
        return random.choice(lst)
    def melanger(lst):
        random.shuffle(lst)
        return lst
    env["entier_entre"] = entier_entre
    env["choisir"] = choisir
    env["melanger"] = melanger
