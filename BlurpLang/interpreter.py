import math
import time
import random
import os
import sys
import datetime
import itertools
import functools
import operator
import collections
import re
import json
import pathlib

class Interpreter:
    def __init__(self):
        self.env = {
            "dire": print,
            "math": math,
            "random": random,
            "time": time,
            "os": os,
            "sys": sys,
            "datetime": datetime,
            "itertools": itertools,
            "functools": functools,
            "operator": operator,
            "collections": collections,
            "re": re,
            "json": json,
            "pathlib": pathlib,
        }

    def evaluer(self, ligne):
        if ligne.startswith("utiliser "):
            nom_lib = ligne[len("utiliser "):].strip()
            self.importer_lib(nom_lib)
        else:
            code = self.traduire_blurp_en_python(ligne)
            try:
                exec(code, {}, self.env)
            except Exception as e_exec:
                try:
                    resultat = eval(code, {}, self.env)
                    if resultat is not None:
                        print(resultat)
                except Exception as e_eval:
                    print("[erreur]", e_exec)

    def importer_lib(self, nom):
        nom_module = f"libs.{nom.lower()}"
        mod = __import__(nom_module, fromlist=["importer"])
        mod.importer(self.env)

    def traduire_blurp_en_python(self, ligne):
        import re
        mots = ligne.strip().split()
        if not mots:
            return ""
        # math racine 16  => math.sqrt(16)
        if mots[0] == "math" and mots[1] == "racine":
            return f"math.sqrt({mots[2]})"
        if mots[0] == "random" and mots[1] == "entier_entre":
            return f"random.randint({mots[2]}, {mots[3]})"
        if mots[0] == "time" and mots[1] == "maintenant":
            return "time.time()"
        if mots[0] == "os" and mots[1] == "nom":
            return "os.name"
        if mots[0] == "sys" and mots[1] == "version":
            return "sys.version"
        if mots[0] == "datetime" and mots[1] == "maintenant":
            return "datetime.datetime.now()"
        if mots[0] == "itertools" and mots[1] == "premiers":
            return f"list(itertools.islice(range(10), {mots[2]}))"
        if mots[0] == "functools" and mots[1] == "somme":
            return "functools.reduce(lambda x, y: x+y, [1,2,3])"
        if mots[0] == "operator" and mots[1] == "ajouter":
            return f"operator.add({mots[2]}, {mots[3]})"
        if mots[0] == "collections" and mots[1] == "compter":
            return 'collections.Counter(["a", "b", "a"])'
        if mots[0] == "re" and mots[1] == "matcher":
            return 're.match("a.", "ab")'
        if mots[0] == "json" and mots[1] == "vers_texte":
            return 'json.dumps({"a": 1})'
        if mots[0] == "pathlib" and mots[1] == "chemin":
            return 'str(pathlib.Path("."))'
        # --- Ajout pour tkinter_blurp ---
        if mots[0] == "fenetre":
            # Utilise des regex pour extraire les valeurs entre guillemets
            titre_match = re.search(r'titre\s+"([^"]+)"', ligne)
            taille_match = re.search(r'taille\s+"([^"]+)"', ligne)
            titre = titre_match.group(1) if titre_match else "Blurp"
            taille = taille_match.group(1) if taille_match else "300x200"
            return f'fenetre(titre="{titre}", taille="{taille}")'
        if mots[0] == "label":
            texte_match = re.search(r'texte\s+"([^"]+)"', ligne)
            texte = texte_match.group(1) if texte_match else ""
            return f'label(texte="{texte}")'
        if mots[0] == "bouton":
            texte_match = re.search(r'texte\s+"([^"]+)"', ligne)
            texte = texte_match.group(1) if texte_match else "OK"
            action_match = re.search(r'action\s+(\w+)', ligne)
            action = action_match.group(1) if action_match else None
            if action:
                return f'bouton(texte="{texte}", action="{action}")'
            else:
                return f'bouton(texte="{texte}")'
        if mots[0] == "afficher":
            return 'afficher()'
        if mots[0] == "action":
            # action nom fonction arg1 arg2 ...
            nom = mots[1]
            fonction = mots[2]
            args = ", ".join(mots[3:]) if len(mots) > 3 else ""
            if args:
                return f'action("{nom}", {fonction}, {args})'
            else:
                return f'action("{nom}", {fonction})'
        if mots[0] == "zone_texte":
            # zone_texte nom "chemin" hauteur 1 largeur 60
            nom_match = re.search(r'nom\s+"([^"]+)"', ligne)
            hauteur_match = re.search(r'hauteur\s+(\d+)', ligne)
            largeur_match = re.search(r'largeur\s+(\d+)', ligne)
            nom = nom_match.group(1) if nom_match else "contenu"
            hauteur = hauteur_match.group(1) if hauteur_match else "10"
            largeur = largeur_match.group(1) if largeur_match else "40"
            return f'zone_texte(nom="{nom}", hauteur={hauteur}, largeur={largeur})'
      
        if mots[0] == "si":
            # si condition alors instruction sinon instruction
            # Ex : si 1 < 2 alors dire("ok") sinon dire("non")
            ligne = ligne.strip()
            import re
            m = re.match(r'si (.+) alors (.+?)( sinon (.+))?$', ligne)
            if m:
                condition = m.group(1)
                instr_vrai = m.group(2)
                instr_faux = m.group(4)
                if instr_faux:
                    return f'({instr_vrai}) if ({condition}) else ({instr_faux})'
                else:
                    return f'({instr_vrai}) if ({condition}) else None'
        # Par défaut, retourne la ligne telle quelle
        return ligne
