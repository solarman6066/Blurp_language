import importlib
import inspect
import keyword
import os
import sys
import subprocess

LIBS_DIR = "libs"
PYLIBS_DIR = "lib_python"
os.makedirs(LIBS_DIR, exist_ok=True)
os.makedirs(PYLIBS_DIR, exist_ok=True)

TRADUCTIONS = {
    "sqrt": "racine",
    "sum": "somme",
    "len": "longueur",
    "print": "dire",
    "random": "aleatoire",
    "randint": "entier_entre",
    "choice": "choisir",
    "mean": "moyenne",
    "median": "mediane",
    "mode": "mode",
    "update": "mettre_a_jour"
}

def est_fonction_simple(f):
    if not inspect.isfunction(f) and not inspect.ismethod(f):
        return False
    try:
        sig = inspect.signature(f)
        for param in sig.parameters.values():
            if param.kind in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
                return False
        return True
    except Exception:
        return False

def traduit_nom(nom):
    base = TRADUCTIONS.get(nom, nom)
    base = base.replace('.', '_')
    if keyword.iskeyword(base) or not base.isidentifier():
        base = f"{base}_blurp"
    return base

def ajouter_docstring(fct):
    doc = inspect.getdoc(fct)
    if doc:
        lignes = doc.split("\n")
        return f'    """{lignes[0]}"""\n'
    return ""

def explorer_classes(module):
    fonctions = {}
    for nom_classe, cls in inspect.getmembers(module, inspect.isclass):
        if cls.__module__ != module.__name__:
            continue
        for nom, methode in inspect.getmembers(cls, inspect.isfunction):
            if est_fonction_simple(methode):
                nom_complet = f"{nom_classe}_{nom}"
                fonctions[nom_complet] = (cls, methode)
    return fonctions

def generer_wrapper_blurp(nom_lib, inclure_classes=True, verbose=False):
    try:
        module = importlib.import_module(nom_lib)
    except Exception as e:
        print(f"❌ Erreur d'import : {e}")
        return

    fonctions = {
        nom: f for nom, f in inspect.getmembers(module, inspect.isfunction)
        if est_fonction_simple(f) and not nom.startswith("__")
    }

    if inclure_classes:
        fonctions_classe = explorer_classes(module)
        for nom, (cls, fct) in fonctions_classe.items():
            if nom not in fonctions:
                fonctions[nom] = fct

    if not fonctions:
        print(f"⚠️ Aucune fonction simple détectée dans {nom_lib}.")
        return

    noms_deja_utilises = set()
    nom_fichier = os.path.join(LIBS_DIR, f"{nom_lib}_blurp.py")
    with open(nom_fichier, "w", encoding="utf-8") as f:
        f.write(f"# Passerelle Blurp générée automatiquement pour {nom_lib}\n")
        f.write(f"import {nom_lib}\n\n")
        f.write("def importer(env):\n")
        for nom, fct in fonctions.items():
            nom_blurp = traduit_nom(nom)
            compteur = 2
            while nom_blurp in noms_deja_utilises:
                nom_blurp = f"{traduit_nom(nom)}_{compteur}"
                compteur += 1
            noms_deja_utilises.add(nom_blurp)
            sig = inspect.signature(fct)
            args = []
            args_with_defaults = []
            for param in sig.parameters.values():
                if param.default is not inspect.Parameter.empty:
                    args.append(f"{param.name}={repr(param.default)}")
                    args_with_defaults.append(param.name)
                else:
                    args.append(param.name)
            args_str = ", ".join(args)
            call_args = ", ".join(sig.parameters.keys())
            doc = inspect.getdoc(fct)
            f.write(f"    def {nom_blurp}({args_str}):\n")
            if doc:
                doc_ligne = doc.split("\n")[0].replace('"', "'")
                f.write(f'        """{doc_ligne}"""\n')
            f.write(f"        return {nom_lib}.{nom}({call_args})\n")
            f.write(f"    env['{nom_blurp}'] = {nom_blurp}\n\n")
            if verbose:
                print(f"✔️  Généré : {nom_blurp}({args_str})")
    print(f"✅ Passerelle générée dans : {nom_fichier}")

def generer_importer(nom_module, fonctions):
    code = [f"import {nom_module}", "", "def importer(env):"]
    for nom_blurp, nom_py in fonctions.items():
        code.append(f"    env['{nom_blurp}'] = {nom_module}.{nom_py}")
    return "\n".join(code)

def installer_lib_python(lib):
    # Installe la lib Python dans le dossier lib_python
    subprocess.run([
        sys.executable, "-m", "pip", "install", lib, "--target", PYLIBS_DIR
    ])
    print(f"Librairie Python {lib} installée dans {PYLIBS_DIR}.")

# Exemple d'utilisation
if __name__ == "__main__":
    nom = input("Nom du module Python à convertir pour Blurp : ")
    generer_wrapper_blurp(nom, inclure_classes=True, verbose=True)
