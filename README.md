# Blurp

Blurp est un mini-langage de script simple et accessible, conçu pour apprendre la programmation, automatiser des tâches ou prototyper rapidement des idées.

## Fonctionnalités principales
- Syntaxe ultra-simple, orientée fonctions
- Accès à de nombreuses bibliothèques Python via des modules Blurp
- Programmation fonctionnelle de base (map, filter, reduce)
- Possibilité de créer des interfaces graphiques simples
- Outils réseau, manipulation de JSON, mathématiques, etc.

## Exemple rapide
```blurp
utiliser math_blurp
dire(racine(25))
utiliser aleatoire_blurp
dire(entier_entre(1, 10))
```

## Lancer Blurp
- En mode interactif :
  ```
  blurp
  ```
- Pour exécuter un script :
  ```
  blurp monscript.blurp
  ```

## Installer une bibliothèque Python pour Blurp
Utilise le gestionnaire de paquets :
```
python bpm.py install nom_de_la_lib
```
Le bpm fonctionne juste pour des librairie python tres simple.

## Structure du projet
- `main.py`, `repl.py`, `interpreter.py` : cœur de Blurp
- `libs/` : modules Blurp (math, réseau, etc.)
- `bpm.py` : gestionnaire de paquets Blurp
- `test.blurp` : exemples de scripts

## Pour en savoir plus
- Consulte les exemples dans `test.blurp`
- Explore le dossier `libs/` pour voir les modules disponibles

---
Blurp : la programmation, tout simplement.
