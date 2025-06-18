import time

def importer(env):
    def maintenant():
        return time.time()
    def attendre(s):
        time.sleep(s)
    env["maintenant"] = maintenant
    env["attendre"] = attendre
