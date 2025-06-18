import datetime

def importer(env):
    def maintenant():
        return datetime.datetime.now()
    env["maintenant"] = maintenant
