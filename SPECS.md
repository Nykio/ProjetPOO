# SPECS

## Rappel : Règles des Combats
- **Dégâts Critiques** : Une attaque a 20% de chance d'infliger 15% de dégât  en plus .
- **Avantage Élémentaire** :
  - Nature subit 2x plus de degats face Mana , inversement le Mana reçoit 0.5x moins de degats .
  - Mana subit 2x plus de degats face au Ombre , inversement l'Ombre reçoit 0.5x moins de degats .
  - Ombre subit 2x plus de degats face au Nature , inversement la Nature reçoit 0.5x moins de degats .
- **Sélection des Cartes et Attaques** :
  - Les joueurs choisissent premièrement une carte dans leur deck.
  - Le joueur lance soit une attaque parmi celles de sa carte (l'adversaire choisit aléatoirement une attaque) soit il sacrifit un round pour soigner sa carte.
- **Conditions de Victoire** :
  - Si toutes les cartes d'un joueur sont éliminées, l'autre joueur gagne.

---

## Classes, Attributs et Méthodes

### Classe `Attaques`
Représente une attaque pouvant être utilisée par une carte.
- **Attributs** :
  - `nom` (str) : Nom de l'attaque.
  - `dgts` (int) : Dégâts infligés.
  - `ele` (str) : Élément de l'attaque parmi Nature , Mana , Ombre .
- **Méthodes** :
  - `self.utiliser()` : Renvoie les dégâts de l'attaque avec une chance de coup critique.

---

### Classe `Potion` ( Pour des raisons de fluidité de code et de gameplay cette capacité a été retirée )
Représente un objet de soin.
- **Attributs** :
  - `soin` (int) : Les points de vie que la potion restaure .

---

### Classe `Cartes`
Représente une carte utilisée en combat.
- **Attributs** :
  - `nom` (str) : Nom de la carte.
  - `pv` (int) : Points de vie actuels .
  - `pvmax` (int) : Points de vie maximum ( utile à savoir lors de l'application d'une potion ).
  - `vts` (int) : Vitesse de la carte .
  - `ele` (str) : Élément de la carte .
  - `atq` (List[Attaques]) : Liste des attaques apprises par la carte .
- **Méthodes** :
  - `self.apprendre_attaque(attaque)` : Ajoute une attaque à la carte.
  - `self.soigner(potion)` : Soigne la carte avec une potion.
  - `self.est_en_vie()` : Renvoie `True` si la carte est en vie.
  - `self.choisir_attaque()` : Renvoie une attaque aléatoire.
  - `self.choix_attaque()` : Permet de choisir une attaque parmi celles disponibles.

---

### Classe `Joueur`
Représente un joueur participant au combat.
- **Attributs** :
  - `nom` (str) : Nom du joueur.
  - `deck` (List[Cartes]) : Liste des cartes dans le deck du joueur.
  - `sac` (List) : Liste des objets dans le sac du joueur.
- **Méthodes** :
  - `self.ajout_carte(carte)` : Ajoute une carte au deck.
  - `self.sors_carte(carte)` : Retire une carte du deck.
  - `self.affiche_deck()` : Affiche le contenu du deck.
  - `self.choisir_carte(nom_carte)` : Renvoie une carte choisie par nom.
  - `self.choisir_carte_aleatoire()` : Renvoie une carte aléatoire du deck.

---

### Classe `Combat`
Gère les combats entre deux joueurs.
- **Attributs** :
  - `joueur` (Joueur) : Joueur principal.
  - `joueur_ennemi` (Joueur) : Adversaire.
- **Méthodes** :
  - `self.joueur_attaque(attaquant, cible)` : Gère l'attaque d'une carte sur une autre.
  - `self.round()` : Gère un round de combat.
  - `self.lancer()` : Démarre le combat complet.

---
