import random

class Card: 
    def  __init__(self, name, type):
        self.name = name
        self.type = type

class Deck:
    def __init__ (self):
        self.card = []

    def add_card(self, card):
        self.card.append(card)

    def show_cards(self):
        print (self.card)

    def draw_card(self):
        return self.card.pop(0)
    
    def shuffle(self):
        for i in range(len(self.card) -1,0,-1):
            r = random.randint(0,i)
            self.card[i], self.card[r] = self.card[r], self.card[i]

class Player:
    def __init__(self):
        self.hand = []

    def draw(self, Deck):
        try:
            self.hand.append(Deck.draw_card())
            return self.hand
        except:
            print ("Não é possível comprar mais carta")

    def draw_initial(self, Deck):
        for i in range(0, 3): 
            self.hand.append(Deck.draw_card())
        return self.hand

    def discard(self):
        try:
            return self.hand.pop(0)
        except:
            print ("ERRO DISCARD")

    def showHand(self):
        return self.hand

class Zone:
    def __init__ (self):
        self.card = []

    def putcard_field(self, Player):
        try:
            self.card.append(Player.discard())
            return self.card
        except:
            print ("Erro!")
        

c1 = Card("c1","1")
c2 = Card("c2","1")
c3 = Card("c3","1")
c4 = Card("c4","1")
c5 = Card("c5","1")

d1 = Deck()

d1.add_card(c2.name)
d1.add_card(c3.name)
d1.add_card(c1.name)
d1.add_card(c4.name)
d1.add_card(c5.name)
d1.shuffle()


p = Player()
print('initial: ',p.draw_initial(d1))

z = Zone()


continua = 1

while (continua == 1):
    options = int(input('(1) - Draw Card \n(2) - PutOnField \n(3) - Discard\n(4) - Show Hand\n(5) - Exit\n'))
    if (options == 1):
        print("Draw")
        print("Card drawned: ", p.draw(d1))
    elif (options == 2):
        print("Zone: ", z.putcard_field(p))
    elif (options == 3):
        print ("Discard: ", p.discard())
    elif (options == 4):
        print ("Hand: ", p.showHand())
    elif (options == 5):
        continua = 0