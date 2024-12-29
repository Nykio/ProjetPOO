faiblesse = {"Nature" : "Mana" , 
            "Mana" : "Ombre" , 
            "Ombre" : "Nature"}

def dedans(element , conteneur):
    for a in conteneur :
        if a == element :
            return True
            break
    return False

from random import randint 

class Attaques:
    def __init__(self, Nom, Degats, Element):
        self.nom = Nom
        self.dgts = Degats
        self.ele = Element

    def utiliser(self) :
        aleatoire = randint(1,5) #va nous permettre de faire des coups critiques
        if aleatoire == 1 :
            return self.dgts*1.15
        else :
            return self.dgts

class Potion :
    def __init__(self,Soin):
        self.soin = Soin
      
class Cartes :
    def __init__(self , PV , Vitesse):
        self.pv = PV
        self.vts = Vitesse
        self.atq = []
        self.pvmax = PV
        
    def apprendre_attaque(self,attaque):
        self.atq.append(attaque)
        
    def soigner(self,potion:Potion):
        if self.pv == self.pvmax :
            print("la carte a déjà tous ses points de vies \n")
        else:
            self.pv += potion.soin
        if self.pv > self.pvmax :
            self.pv = self.pvmax

    def est_en_vie(self):
        pass 

    def choix_auto(self) :
        pass

    def choix_attaque(self) :
        possibilité = [] #va nous permettre de vérifier que la demande du joueur est possible
        print("Entrez le numéro de l'attaque que vous voulez utiliser :  \n")
        for i , attaque in enumerate(self.atq) :
            possibilité.append(i)
            print(f"{i} - {attaque.nom}")
        entree = int(input())
        for i , attaque in enumerate(self.atq) :
            if i == entree :
                return attaque
            else :
                print("Choix non reconnu veuillez recommencer . \n")
        return self.choix_attaque()

class Joueur:
    def __init__(self,nom , deck, sac):
        self.nom = nom
        self.deck = []
        self.sac = []
        
    def ajout_sac(self, objet):
        self.sac.append(objet)
            
    def ajout_carte(self, carte):
        self.deck.append(carte)

    def sors_carte(self, carte):
        self.deck.remove(carte)

    def choisir_carte(self) :
        pass

    def choisir_carte_aleatoire(self) :
        pass

class Combat:
    def __init__(self, joueur: Joueur, joueur_ennemi: Joueur):
        self.joueur = joueur
        self.joueur_ennemi = joueur_ennemi

    def joueur_attaque(self, attaquant: Cartes, cible: Cartes):
        attaque = attaquant.choix_attaque()
        degats = attaque.utiliser()

        if faiblesse[attaque.ele] == cible.ele:
            degats *= 2
            print(f"\nCoup critique ! {attaque.nom} inflige {degats} dégâts à {cible.nom}.")

        elif faiblesse[cible.ele] == attaque.ele:
            degats *= 0.5
            print(f"\nCoup peu efficace... {attaque.nom} inflige {degats} dégâts à {cible.nom}.")

        else:
            print(f"\n{attaque.nom} inflige {degats} dégâts à {cible.nom}.")

        cible.pv -= degats

    def round(self):
        Carte1 = self.joueur.choisir_carte()
        Carte2 = self.joueur_ennemi.choisir_carte_aleatoire()

        print(f"\n{Carte1.nom} - {Carte1.pv} affronte {Carte2.nom} - {Carte2.pv} !")

        tour_joueur = False
        if Carte1.vts > Carte2.vts :
            tour_joueur = True

        while Carte1.est_en_vie() and Carte2.est_en_vie():
            if tour_joueur :
                self.joueur_attaque(Carte1, Carte2)
                tour_joueur = False
            else:
                self.joueur_attaque(Carte2, Carte1)
                tour_joueur = True

            print(f"\n{Carte1.nom} a {Carte1.pv} PV , {Carte2.nom} a {Carte2.pv} PV")


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
            print(f"\n{self.joueur.nom} a perdu le combat !")
        else:
            print(f"\n{self.joueur_ennemi.nom} a perdu le combat !")
