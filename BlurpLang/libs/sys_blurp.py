import sys

def importer(env):
    def version_python():
        return sys.version
    env["version_python"] = version_python
