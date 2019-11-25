#Card class is a blueprint of the Card object
#parent Class
class Card:

    #initalizer to create the attributes of every class object 
    def __init__(self, cost, name):
        self.cost = cost
        self.name = name
        #Attributes describes the object
        #give the card a cost attribute
        #give the card a name attribute

#Behaviors
    def printCardInfo(self):
        print('The card cost: ' + str(self.cost))
        print('The card name: ' + self.name)
