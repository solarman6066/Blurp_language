import time

def importer(env):
    env["attendre"] = lambda s: time.sleep(s)
    env["maintenant"] = lambda: time.time()
