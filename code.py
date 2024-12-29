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
        
    def soigner(self,potion):
        if self.pv == self.pvmax :
            print("la carte a déjà tous ses points de vies")
        else:
            self.pv += potion.soin
        if self.pv > self.pvmax :
            self.pv = self.pvmax

    def choix_attaque(self) :
        possibilité = [] #va nous permettre de vérifier que la demande du joueur est possible
        print("Entrez le numéro de l'attaque que vous voulez utiliser : ")
        for i , attaque in enumerate(self.atq) :
            possibilité.append(i)
            print(f"{i} - {attaque.nom}")
        entree = int(input())
        for i , attaque in enumerate(self.atq) :
            if i == entree :
                return attaque
            else :
                print("Choix non reconnu veuillez recommencer .")
        return self.choix_attaque()

class Joueur:
    def __init__(self, deck, sac):
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

class Combat :
    def __init__(self , joueur:Joueur , joueur_ennemi:Joueur):
        pass

    def lancer() :
        Carte1 = joueur.choisir_carte()
        Carte2 = jouer_ennemi.choisir_carte_aleatoire()

