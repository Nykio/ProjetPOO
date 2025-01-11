
---

### Fichier `SPECS.md`

```markdown
# Spécifications Techniques du Programme

## Règles des Combats
- **Dégâts Critiques** : Une attaque a 20% de chance d'infliger 1.15 fois ses dégâts de base.
- **Avantage Élémentaire** :
  - Nature bat Mana.
  - Mana bat Ombre.
  - Ombre bat Nature.
- **Sélection des Cartes et Attaques** :
  - Les joueurs choisissent une carte dans leur deck.
  - Une attaque est choisie par le joueur (ou aléatoirement pour l'adversaire).
- **Conditions de Victoire** :
  - Si toutes les cartes d'un joueur sont éliminées, l'autre joueur gagne.

---

## Classes, Attributs et Méthodes

### Classe `Attaques`
Représente une attaque pouvant être utilisée par une carte.
- **Attributs** :
  - `nom` (str) : Nom de l'attaque.
  - `dgts` (int) : Dégâts infligés.
  - `ele` (str) : Élément de l'attaque (Nature, Mana, Ombre).
- **Méthodes** :
  - `utiliser()` : Renvoie les dégâts infligés, avec une chance de coup critique.

---

### Classe `Potion`
Représente un objet de soin.
- **Attributs** :
  - `soin` (int) : Points de vie restaurés.

---

### Classe `Cartes`
Représente une carte utilisée en combat.
- **Attributs** :
  - `nom` (str) : Nom de la carte.
  - `pv` (int) : Points de vie actuels.
  - `pvmax` (int) : Points de vie maximum.
  - `vts` (int) : Vitesse de la carte.
  - `ele` (str) : Élément de la carte.
  - `atq` (list[Attaques]) : Liste des attaques apprises.
- **Méthodes** :
  - `apprendre_attaque(attaque)` : Ajoute une attaque à la carte.
  - `soigner(potion)` : Soigne la carte avec une potion.
  - `est_en_vie()` : Renvoie `True` si la carte est en vie.
  - `choisir_attaque()` : Renvoie une attaque aléatoire.
  - `choix_attaque()` : Permet de choisir une attaque parmi celles disponibles.

---

### Classe `Joueur`
Représente un joueur participant au combat.
- **Attributs** :
  - `nom` (str) : Nom du joueur.
  - `deck` (list[Cartes]) : Liste des cartes dans le deck du joueur.
  - `sac` (list) : Liste des objets dans le sac du joueur.
- **Méthodes** :
  - `ajout_carte(carte)` : Ajoute une carte au deck.
  - `sors_carte(carte)` : Retire une carte du deck.
  - `affiche_deck()` : Affiche le contenu du deck.
  - `choisir_carte(nom_carte)` : Renvoie une carte choisie par nom.
  - `choisir_carte_aleatoire()` : Renvoie une carte aléatoire du deck.

---

### Classe `Combat`
Gère les combats entre deux joueurs.
- **Attributs** :
  - `joueur` (Joueur) : Joueur principal.
  - `joueur_ennemi` (Joueur) : Adversaire.
- **Méthodes** :
  - `joueur_attaque(attaquant, cible)` : Gère l'attaque d'une carte sur une autre.
  - `round()` : Gère un round de combat.
  - `lancer()` : Démarre le combat complet.

---
