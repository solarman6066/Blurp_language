import itertools

def importer(env):
    def premiers(n):
        return list(itertools.islice(range(10), n))
    env["premiers"] = premiers
