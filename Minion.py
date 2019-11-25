#This class needs to inherit the attributes and behaviors of the card class 
#A minion object is a card
#Child Class
from Card import Card
class Minion(Card):
    def __init__(self, cost, name, damage, life):
        Card.__init__(self, cost, name)
        #assign parameters to the object
        self.damage = damage
        self.life = life

    def printMinionInfo(self):
        print('The card cost: ' + str(self.cost)
        print('The card name: ' + self.name)
        print('Damage: ' + str(self.damage))
        print('Life: ' + str(self.life))