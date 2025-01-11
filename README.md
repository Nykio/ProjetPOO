# PROJET POO , Mélaine , Maîna et Toine 

## Description du Programme
Ce programme simule un jeu de combat de cartes dans un univers médiéval-fantasy. Chaque joueur dispose d'un deck de cartes représentant des personnages ou créatures, chacun ayant des caractéristiques spécifiques (nom, points de vie, vitesse, élément, attaques). Les joueurs s'affrontent au tour par tour en utilisant les cartes de leur deck. Le but du jeu est de vaincre toutes les cartes adverses.

---

## Fonctionnement Général
1. **Joueurs et Cartes** : 
   Chaque joueur dispose d'un deck de cartes qu'il peut utiliser en combat.Les cartes et Attaques appartiennent à un Element ( type ) qui auront des avantages en combat , les Elements sont les suivants :
     
      **A. Nature 🌿** : La force brute de la flore et de la faune. Ce type représente la résilience et l’équilibre de la vie. Les pouvoirs de Nature incluent la croissance rapide, le contrôle des plantes et la communion avec les créatures sauvages. Cependant, il est vulnérable à la manipulation magique.
     
      **B. Mana ✨** : L’essence pure de la magie, source de tout pouvoir arcanique. Ce type incarne les sorts, les rituels et les portails mystiques. Les adeptes du Mana utilisent leur énergie pour créer des miracles, mais ils doivent se méfier de l’imprévisibilité des forces des ténèbres .
     
      **C. Ombre 🌑** : Furtivité et tromperie incarnées. Ombre représente les illusions, la peur et le pouvoir des ténèbres insaisissables. Les utilisateurs de ce type frappent dans l'obscurité et manipulent la perception, mais leur force diminue face aux pouvoirs bruts de la nature .  
   
3. **Système d'Attaques** : 
   Chaque carte peut apprendre des attaques avec des dégâts et un élément (Nature, Mana ou Ombre). Les interactions élémentaires suivent des règles de faiblesses :
   - **Nature** > **Mana**
   - **Mana** > **Ombre**
   - **Ombre** > **Nature**
   De plus il y a une chance sur cinq que l'attaque soit un coup critique .

4. **Système de Combat** : 
   Les joueurs choisissent une carte de leur deck et affrontent une carte du deck de l'adversaire. Le combat continue jusqu'à ce qu'un joueur n'ait plus de cartes en vie dans son deck .

---

## Entrées et Sorties

### Entrées
**Interaction utilisateur** :
   - Le joueur choisit manuellement une carte pour le combat , l'entrée du joueur doit parfaitement correspondre au nom de la carte .
   - Le joueur sélectionne les attaques à utiliser en utilisant soit 0 soit 1 .

### Sorties
- Messages dans la console indiquant :
  - L'état des cartes (PV restants, attaques effectuées).
  - Les résultats des combats (cartes vaincues, joueur gagnant ou perdant).

---

## Comment Exécuter le Programme
1. Une fois le programme télécharger il est préférable de l'utiliser sur VS Code car la fenetre d'entrée du joueur cause des problèmes ailleurs .
2. Vous n'avez qu'à utiliser la commande "combat.lancer()" dans le terminale et profiter du jeu !
3. Le joueur préconfiguré que vous allez incarner , Héros de la lumière , possède le deck suivant :  

# 🛡️ **Chevalier d'Argent**  
- **Points de vie (PV)** : 100  
- **Vitesse** : 30  
- **Élément** : Nature 🌿  
- **Attaques** :  
  - **Épée bénite** : Puissance 25 (Nature 🌿)  
  - **Bouclier sacré** : Puissance 15 (Nature 🌿)  

# 🔥 **Mage de Feu**  
- **Points de vie (PV)** : 80  
- **Vitesse** : 20  
- **Élément** : Mana ✨  
- **Attaques** :  
  - **Boule de feu** : Puissance 35 (Mana ✨)  
  - **Explosion ardente** : Puissance 50 (Mana ✨)  

# 🗡️ **Voleur des Ombres**  
- **Points de vie (PV)** : 90  
- **Vitesse** : 40  
- **Élément** : Ombre 🌑  
- **Attaques** :  
  - **Lame empoisonnée** : Puissance 30 (Ombre 🌑)  
  - **Attaque sournoise** : Puissance 40 (Ombre 🌑)


*Certaine Carte ont été généré par IA*
