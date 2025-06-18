import sys
from repl import lancer_repl
from interpreter import Interpreter

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Exécution d'un fichier Blurp
        chemin = sys.argv[1]
        interp = Interpreter()
        with open(chemin, encoding="utf-8") as f:
            for ligne in f:
                ligne = ligne.strip()
                if ligne and not ligne.startswith("#"):
                    try:
                        interp.evaluer(ligne)
                    except Exception as e:
                        print("[erreur]", e)
    else:
        lancer_repl()
