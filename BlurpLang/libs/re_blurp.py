import re

def importer(env):
    def matcher(expr, texte):
        return re.match(expr, texte)
    env["matcher"] = matcher
