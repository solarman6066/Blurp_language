from interpreter import Interpreter

def lancer_repl():
    print("🌀 Blurp v0.1")
    interp = Interpreter()
    while True:
        try:
            ligne = input("> ")
            if ligne.strip() in ("exit", "quit"):
                break
            interp.evaluer(ligne)
        except Exception as e:
            print("[erreur]", e)
