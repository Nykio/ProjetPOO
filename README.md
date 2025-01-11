# README

## Description du programme

Ce programme implémente un jeu de cartes dans un univers médiéval fantastique. Chaque joueur dispose d'un deck de cartes qui représentent des personnages avec des points de vie (PV), de la vitesse et des attaques élémentaires (Nature, Mana ou Ombre). Les joueurs s'affrontent en utilisant stratégiquement leurs cartes et leurs attaques.

Le système de combat prend en compte les faiblesses élémentaires, les coups critiques, ainsi que la vitesse pour déterminer l'ordre des tours.

## Fonctionnement du programme

### 1. Classes principales

- **`Attaques`** : Représente une attaque avec un nom, des dégâts et un élément (Nature, Mana ou Ombre).
- **`Potion`** : Objet permettant de soigner une carte.
- **`Cartes`** : Représente une carte avec des points de vie, une vitesse, un élément, et une liste d'attaques.
- **`Joueur`** : Représente un joueur avec un nom, un deck de cartes et un sac d'objets.
- **`Combat`** : Gère les rounds entre deux joueurs jusqu'à ce qu'un des decks soit vide.

### 2. Mécanismes principaux

- Chaque joueur dispose d'un deck composé de 3 cartes préconfigurées.
- Avant chaque round, le joueur choisit une carte pour combattre. L'adversaire choisit une carte aléatoirement.
- Les cartes attaquent à tour de rôle selon leur vitesse. Les faiblesses élémentaires et les coups critiques influencent les dégâts.
- Le combat se termine lorsqu'un des deux joueurs n'a plus de cartes dans son deck.

## Instructions d'exécution

### Prérequis

- Python 3.x doit être installé sur votre système.

### Installation

1. Téléchargez ou clonez le dépôt contenant ce programme.
2. Assurez-vous que le fichier principal s'appelle `main.py`.
3. Lancez le programme via un terminal ou un interpréteur Python.

### Exécution du programme

#### Commande de base

```bash
python main.py
```

#### Entrées utilisateur

- Lorsqu'on vous demande de **choisir une carte**, entrez le **nom exact** d'une carte présente dans votre deck.
  Exemple :
  ```
  Choisissez une carte de votre deck : Chevalier d'Argent
  ```
- Lorsqu'on vous demande de **choisir une attaque**, entrez le numéro associé à l'attaque affichée.
  Exemple :
  ```
  Attaques disponibles pour Chevalier d'Argent :
  0 - Épée bénite - Nature, 25 dégâts
  1 - Bouclier sacré - Nature, 15 dégâts
  Choisissez une attaque : 0
  ```

### Sorties utilisateur

- Le programme affiche des messages détaillés sur l'état du combat, y compris :
  - Les cartes choisies pour le combat.
  - Les dégâts infligés par chaque attaque.
  - Les points de vie restants pour chaque carte.
  - Les cartes hors jeu.
  - Le joueur qui remporte le combat.

Exemple de sortie :

```
Le combat commence entre Héros de la Lumière et Seigneur Sombre !

Chevalier d'Argent - 100 PV affronte Chevalier Noir - 110 PV !

Épée bénite inflige 25 dégâts à Chevalier Noir.
Chevalier Noir a 85 PV.
...
Seigneur Sombre a perdu le combat !
```

## Limitations

- Les noms des cartes doivent être saisis exactement comme ils apparaissent dans le deck.
- Le programme fonctionne uniquement en mode interactif (pas d'API ou d'arguments en ligne de commande pour le moment).

## Améliorations futures

- Ajout d'une interface graphique ou textuelle plus intuitive.
- Implémentation d'une API REST pour jouer via des requêtes HTTP.
- Ajout de nouvelles cartes, attaques et effets spéciaux.
- Mode multijoueur en ligne.


