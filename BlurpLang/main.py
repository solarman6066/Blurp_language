import sys
from repl import lancer_repl
from interpreter import Interpreter

def lire_bloc_conditionnel(f, premiere_ligne):
    bloc = [premiere_ligne]
    for ligne in f:
        bloc.append(ligne.rstrip("\n"))
        if ligne.strip() == "fin":
            break
    return bloc

def executer_bloc_conditionnel(interp, bloc):
    # bloc[0] = si ... alors
    # Cherche 'sinon' et 'fin'
    condition_ligne = bloc[0]
    condition = condition_ligne[3:condition_ligne.find("alors")].strip()
    bloc_alors = []
    bloc_sinon = []
    dans_alors = True
    for ligne in bloc[1:]:
        if ligne.strip() == "sinon":
            dans_alors = False
            continue
        if ligne.strip() == "fin":
            break
        if dans_alors:
            bloc_alors.append(ligne)
        else:
            bloc_sinon.append(ligne)
    try:
        if eval(condition, {}, interp.env):
            for l in bloc_alors:
                interp.evaluer(l)
        else:
            for l in bloc_sinon:
                interp.evaluer(l)
    except Exception as e:
        print("[erreur condition]", e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Exécution d'un fichier Blurp
        chemin = sys.argv[1]
        interp = Interpreter()
        with open(chemin, encoding="utf-8") as f:
            f = iter(f)
            for ligne in f:
                ligne = ligne.strip()
                if not ligne or ligne.startswith("#"):
                    continue
                if ligne.startswith("si ") and "alors" in ligne:
                    bloc = lire_bloc_conditionnel(f, ligne)
                    executer_bloc_conditionnel(interp, bloc)
                else:
                    try:
                        interp.evaluer(ligne)
                    except Exception as e:
                        print("[erreur]", e)
    else:
        lancer_repl()
