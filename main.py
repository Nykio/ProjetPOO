faiblesse = {"Nature" : "Mana" , 
            "Mana" : "Ombre" , 
            "Ombre" : "Nature"}

def dedans(element , conteneur): #fonction in avec un conteneur
    for a in conteneur :
        if a == element :
            return True
            break
    return False

from random import randint 
from random import choice 

class Attaques:
    def __init__(self, Nom, Degats, Element):
        self.nom = Nom
        self.dgts = Degats
        self.ele = Element

    def utiliser(self):
        if randint(1, 5) == 1:  # coup critique
            return self.dgts * 1.15
        return self.dgts

class Potion :
    def __init__(self,nom:str,Soin:int):
        assert(type(Soin) is int)
        self.soin = Soin
        self.nom = nom
      
class Cartes:
    def __init__(self, nom, pv, vitesse, element):
        self.nom = nom
        self.pv = pv
        self.pvmax = pv
        self.vts = vitesse
        self.ele = element
        self.atq = []
        
    def apprendre_attaque(self,attaque):
        self.atq.append(attaque)
        
    def soigner(self, potion: Potion):
        if self.pv == self.pvmax:
            return "\nLa carte a déjà tous ses points de vie."
        else:
            self.pv += potion.soin
            if self.pv > self.pvmax:
                self.pv = self.pvmax
            return f"\nLa carte est soignée ! Elle a maintenant {self.pv} PV."

    def est_en_vie(self):
        if self.pv > 0 :
            return True
        else:
            return False

    def choix_auto_attaque(self):
        if not self.atq:
            return ("aucune attaque disponible")
        return choice(self.atq)

    def choix_attaque(self):
        print(f"\nAttaques disponibles pour {self.nom} :")
        for i, attaque in enumerate(self.atq):
            print(f"{i} - {attaque.nom} - {attaque.ele} , {attaque.dgts} dégâts")

        while True:
            try:
                choix = int(input())
                if 0 <= choix < len(self.atq):
                    return self.atq[choix]
                else:
                    print("Choix invalide, essayez encore.")
            except ValueError:
                print("Entrée invalide, veuillez entrer un nombre.")

class Joueur:
    def __init__(self,nom , deck, sac):
        self.nom = nom
        self.deck = []
        self.sac = []
        
    def ajout_sac(self, objet):
        self.sac.append(objet)
            
    def ajout_carte(self, carte):
        if len(self.deck) < 3:
            self.deck.append(carte)
        else:
            print("Le deck est plein")

    def sors_carte(self, carte):
        self.deck.remove(carte)

    def affiche_sac(self):
        if self.sac:
            print("Contenue du sac :")
            for objet in self.sac:
                print(objet.nom)
        else:
            print("Le sac est vide :")
    
    def affiche_deck(self):
        if self.deck:
            print("Contenue du deck :")
            for objet in self.deck:
                print(objet.nom)
        else:
            print("Le deck est vide :")

    def choisir_carte(self, nom_carte) :
        for carte in self.deck:
            if carte.nom == nom_carte:
                print (f"La carte choisi est '{nom_carte}'")
                return carte
            
        print (f"La carte '{nom_carte}' n'est pas dans le deck")
        return None

    def choisir_carte_aleatoire(self):
        if self.deck:
            carte_aleatoire = choice(self.deck)
            return carte_aleatoire
        else:
            return None

class Combat:
    def __init__(self, joueur: Joueur, joueur_ennemi: Joueur):
        self.joueur = joueur
        self.joueur_ennemi = joueur_ennemi
        assert(type(joueur) is Joueur and type(joueur_ennemi) is Joueur)

    def joueur_attaque(self, attaquant: Cartes, cible: Cartes , attaque = None ):
        if not attaque :
            attaque = attaquant.choix_attaque()
        degats = attaque.utiliser()

        if faiblesse[attaque.ele] == cible.ele:
            degats *= 2
            print(f"Incroyable! {attaque.nom} inflige {degats} dégâts à {cible.nom}.")

        elif faiblesse[cible.ele] == attaque.ele:
            degats *= 0.5
            print(f"\nCoup peu efficace... {attaque.nom} inflige {degats} dégâts à {cible.nom}.")

        else:
            print(f"\n{attaque.nom} inflige {degats} dégâts à {cible.nom}.")

        cible.pv -= degats

    def round(self):
        Carte2 = self.joueur_ennemi.choisir_carte_aleatoire()

        while True : 
            carte_choisi = str(input("Choisissez une carte de votre deck : "))
            Carte1 = self.joueur.choisir_carte(carte_choisi)
            if type(Carte1) is Cartes :
                break
            else :
                print("\nEntrée invalide , recommencez .")
                continue

        assert(type(Carte1) is Cartes and type(Carte2) is Cartes)

        print(f"\n{Carte1.nom} : {Carte1.ele} ({Carte1.pv} PV) affronte {Carte2.nom} : {Carte2.ele} ({Carte2.pv} PV) !")

        tour_joueur = Carte1.vts > Carte2.vts

        while Carte1.est_en_vie() and Carte2.est_en_vie():

            if tour_joueur:
                print("\nQue souhaitez-vous faire ? 0 - Soigner, 1 - Attaquer")

                while True:
                    try:
                        choix = int(input("Votre choix : "))
                        if choix == 0:  # Soigner
                            potion_trouvee = False
                            for ele in self.joueur.sac :
                                if type(ele) is Potion :
                                    Carte1.soigner(ele)
                                    potion_trouvee = True
                                    self.joueur.sac.remove(ele)
                                    assert(Carte1.pv <= Carte1.pvmax)
                                    break

                            if not potion_trouvee:
                                print("\nVous ne disposez d'aucune potion.")

                        elif choix == 1:  # Attaquer
                            self.joueur_attaque(Carte1, Carte2)

                        else:
                            print("Choix invalide, réessayez.")
                            continue

                        break
                    except ValueError:
                        print("Entrée invalide, veuillez entrer un nombre.")
                        
                tour_joueur = False
            else:
                attaque_ennemi = Carte2.choix_auto_attaque()
                self.joueur_attaque(Carte2, Carte1 , attaque_ennemi)
                tour_joueur = True

            print(f"\n{Carte1.nom} a {Carte1.pv} PV. {Carte2.nom} a {Carte2.pv} PV.")

        if Carte1.est_en_vie():
            print(f"\n{Carte2.nom} est hors jeu !")
            self.joueur_ennemi.sors_carte(Carte2)

        else:
            print(f"\n{Carte1.nom} est hors jeu !")
            self.joueur.sors_carte(Carte1)


    def lancer(self):
        print(f"\nLe combat commence entre {self.joueur.nom} et {self.joueur_ennemi.nom} !")
        while self.joueur.deck and self.joueur_ennemi.deck:
            self.round()

        if not self.joueur.deck:
            assert self.joueur_ennemi.deck 
            print(f"\n{self.joueur.nom} a perdu le combat !")
        else:
            assert not self.joueur_ennemi.deck 
            print(f"\n{self.joueur_ennemi.nom} a perdu le combat !")


#PARTIE RPG 
# Votre joueur

carte_joueur_1 = Cartes(
    nom="Chevalier d'Argent",
    pv=100,
    vitesse=30,
    element="Nature"
)

carte_joueur_1.apprendre_attaque(Attaques("Épée bénite", 25, "Nature"))
carte_joueur_1.apprendre_attaque(Attaques("Bouclier sacré", 15, "Nature"))

carte_joueur_2 = Cartes(
    nom="Mage de Feu",
    pv=80,
    vitesse=20,
    element="Mana"
)

carte_joueur_2.apprendre_attaque(Attaques("Boule de feu", 35, "Mana"))
carte_joueur_2.apprendre_attaque(Attaques("Explosion ardente", 50, "Mana"))

carte_joueur_3 = Cartes(
    nom="Voleur des Ombres",
    pv=90,
    vitesse=40,
    element="Ombre"
)

carte_joueur_3.apprendre_attaque(Attaques("Lame empoisonnée", 30, "Ombre"))
carte_joueur_3.apprendre_attaque(Attaques("Attaque sournoise", 40, "Ombre"))

potion = Potion("Breuvage Moyen" , 30)

joueur = Joueur(nom="Héros de la Lumière", deck=[], sac=[])
joueur.ajout_carte(carte_joueur_1)
joueur.ajout_carte(carte_joueur_2)
joueur.ajout_carte(carte_joueur_3)
joueur.ajout_sac(potion)
joueur.ajout_sac(potion)

# Votre adversaire

carte_adversaire_1 = Cartes(
    nom="Chevalier Noir",
    pv=110,
    vitesse=25,
    element="Ombre"
)

carte_adversaire_1.apprendre_attaque(Attaques("Lame maudite", 30, "Ombre"))
carte_adversaire_1.apprendre_attaque(Attaques("Éruption ténébreuse", 40, "Ombre"))

carte_adversaire_2 = Cartes(
    nom="Invocateur d'Arcanes",
    pv=90,
    vitesse=20,
    element="Mana"
)

carte_adversaire_2.apprendre_attaque(Attaques("Foudre mystique", 35, "Mana"))
carte_adversaire_2.apprendre_attaque(Attaques("Pluie de météores", 50, "Mana"))

carte_adversaire_3 = Cartes(
    nom="Ranger des Bois",
    pv=100,
    vitesse=35,
    element="Nature"
)

carte_adversaire_3.apprendre_attaque(Attaques("Flèche perçante", 25, "Nature"))
carte_adversaire_3.apprendre_attaque(Attaques("Tir en rafale", 30, "Nature"))

adversaire = Joueur(nom="Seigneur Sombre", deck=[], sac=[])
adversaire.ajout_carte(carte_adversaire_1)
adversaire.ajout_carte(carte_adversaire_2)
adversaire.ajout_carte(carte_adversaire_3)

combat = Combat(joueur=joueur, joueur_ennemi=adversaire)
#combat.lancer()


#Tests 

carte = Cartes("Test", 50, 20, "Nature")
carte.soigner(Potion("Potion de soin", 30))
assert carte.pv == 50


carte1 = Cartes("Chevalier", 100, 30, "Nature")
carte2 = Cartes("Dragon", 150, 20, "Mana")
attaque = Attaques("Épée", 25, "Nature")

combattest = Combat(Joueur("Test1", [], []) , Joueur("Test2", [], []))
combattest.joueur_attaque(carte1, carte2, attaque)

# Carte2 est faible face à l'attaque
assert 150 - (25 * 2) <= carte2.pv <= (150 - (25 * 2))*1.15

# Carte2 est résistante face à l'attaque
carte2.pv = carte2.pvmax
attaque.ele = "Mana"
combat.joueur_attaque(carte1, carte2, attaque)
assert 150 - (25 * 0.5) <= carte2.pv <= (150 - (25 * 0.5))*1.15

# Carte2 est neutre face à l'attaque
carte2.pv = carte2.pvmax
attaque.ele = "Ombre"
combat.joueur_attaque(carte1, carte2, attaque)
assert 150 - 25  <= carte2.pv <= ( 150 - 25 )*1.15
