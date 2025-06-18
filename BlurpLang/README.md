# Blurp : Mini-langage de script simple

## Présentation
Blurp est un langage de script ultra-simple, orienté fonctions, qui permet d'utiliser des bibliothèques Python via une syntaxe lisible et accessible.

## Syntaxe de base
- Chaque ligne est une instruction.
- On appelle des fonctions avec des arguments séparés par des virgules ou des parenthèses.
- Les variables sont limitées, on privilégie l'appel direct de fonctions.

### Exemples d'instructions :
```
dire("Bonjour !")
utiliser math_blurp
racine(16)
```

## Utilisation des bibliothèques
Pour utiliser une bibliothèque, il faut l'importer :
```
utiliser math_blurp
utiliser aleatoire_blurp
```

Ensuite, tu peux appeler les fonctions simples exposées :
```
dire(racine(25))
dire(entier_entre(1, 10))
```

## Fonctions réseau
```
utiliser reseau_blurp
utiliser requests_blurp
dire(nom_machine())
dire(requete_http("https://httpbin.org/get"))
```

## Programmation fonctionnelle
```
utiliser fonctionnel_blurp
dire(map(doubler, [1,2,3,4]))
dire(filter(pair, [1,2,3,4,5,6]))
dire(reduce(somme, [1,2,3,4]))
```

## Interface graphique simple
```
utiliser tkinter_blurp
fenetre titre "Ma fenêtre" taille "300x200"
label texte "Bonjour !"
bouton texte "Fermer" action quitter
afficher
```

## Bonnes pratiques
- Utilise toujours des fonctions simples (pas de blocs Python, pas de if/else, pas de def dans le script).
- Pour des traitements complexes, crée une fonction dans une lib Python et appelle-la depuis Blurp.
- Les noms de fonctions Blurp sont en français et explicites.

## Installer une nouvelle bibliothèque
Utilise le Blurp Package Manager (bpm) :
```
python bpm.py install nom_de_la_lib
utiliser nom_de_la_lib_blurp
```
Le bpm ne fontionne que pour des lib python tres simple.

## Pour aller plus loin
- Consulte les fichiers du dossier `libs/` pour voir les fonctions disponibles.
- Inspire-toi des exemples dans `test.blurp`.

---
Amuse-toi bien avec Blurp !
