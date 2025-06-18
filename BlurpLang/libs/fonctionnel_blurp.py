def importer(env):
    def map_blurp(f, lst):
        return list(map(env[f], lst)) if isinstance(f, str) else list(map(f, lst))
    def filter_blurp(f, lst):
        return list(filter(env[f], lst)) if isinstance(f, str) else list(filter(f, lst))
    def reduce_blurp(f, lst):
        from functools import reduce
        return reduce(env[f], lst) if isinstance(f, str) else reduce(f, lst)
    def doubler(x):
        return x*2
    def pair(x):
        return x%2==0
    def somme(x, y):
        return x+y
    env["map"] = map_blurp
    env["filter"] = filter_blurp
    env["reduce"] = reduce_blurp
    env["doubler"] = doubler
    env["pair"] = pair
    env["somme"] = somme
