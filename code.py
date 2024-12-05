class Attaques :
	def __init__(self,Nom,Degats):
		self.nom = Nom
		self.dgts = Degats

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
