import tkinter as tk

_fenetre = None
_widgets = []
_actions = {}

def importer(env):
    def fenetre(titre="Blurp", taille="300x200"):
        global _fenetre
        _fenetre = tk.Tk()
        _fenetre.title(titre)
        _fenetre.geometry(taille)
    def label(texte=""):
        global _fenetre
        lbl = tk.Label(_fenetre, text=texte, width=40, wraplength=300, anchor="w", justify="left")
        lbl.pack(padx=10, pady=10)
        _widgets.append(lbl)
    def bouton(texte="OK", action=None):
        global _fenetre
        def callback():
            if action == "quitter":
                quitter()
            elif action and action in _actions:
                _actions[action]()
        btn = tk.Button(_fenetre, text=texte, command=callback)
        btn.pack(padx=10, pady=5)
        _widgets.append(btn)
    def action(nom, f, *args):
        # Permet d'enregistrer une action avec des arguments supplémentaires
        if args:
            _actions[nom] = lambda: f(*args)
        else:
            _actions[nom] = f
    def quitter():
        global _fenetre
        if _fenetre:
            _fenetre.destroy()
    def afficher():
        global _fenetre
        _fenetre.mainloop()
    def zone_texte(nom="contenu", largeur=40, hauteur=10):
        global _fenetre
        txt = tk.Text(_fenetre, width=largeur, height=hauteur)
        txt.pack(padx=10, pady=10)
        _widgets.append(txt)
        env[nom] = txt
    env["fenetre"] = fenetre
    env["label"] = label
    env["bouton"] = bouton
    env["action"] = action
    env["quitter"] = quitter
    env["afficher"] = afficher
    env["zone_texte"] = zone_texte
