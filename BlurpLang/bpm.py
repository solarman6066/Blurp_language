import sys
import subprocess
import os

LIBS_DIR = "libs"

def install(lib):
    # Installe la lib Python via pip
    subprocess.run([sys.executable, "-m", "pip", "install", lib])
    # Crée un wrapper Blurp
    wrapper = f'''
import {lib}

def importer(env):
    env["{lib}"] = {lib}
'''
    with open(os.path.join(LIBS_DIR, f"{lib}_blurp.py"), "w", encoding="utf-8") as f:
        f.write(wrapper)
    print(f"Librairie {lib} installée et wrapper Blurp créé.")

def list_libs():
    for f in os.listdir(LIBS_DIR):
        if f.endswith("_blurp.py"):
            print(f[:-9])

def remove(lib):
    path = os.path.join(LIBS_DIR, f"{lib}_blurp.py")
    if os.path.exists(path):
        os.remove(path)
        print(f"Librairie {lib} supprimée.")
    else:
        print("Librairie non trouvée.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: bpm install/list/remove nom_lib")
    elif sys.argv[1] == "install":
        install(sys.argv[2])
    elif sys.argv[1] == "list":
        list_libs()
    elif sys.argv[1] == "remove":
        remove(sys.argv[2])
