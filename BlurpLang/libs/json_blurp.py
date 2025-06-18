import json

def importer(env):
    def vers_texte(obj):
        return json.dumps(obj)
    def depuis_texte(txt):
        return json.loads(txt)
    env["vers_texte"] = vers_texte
    env["depuis_texte"] = depuis_texte
