import random, os

class Card: 
    def  __init__(self, name, type):
        self.name = name
        self.type = type

    def typecard(self):
        return self.type

class Deck:
    def __init__ (self):
        self.card = []

    def add_card(self, Card):
        self.card.append(Card)

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

    def discard(self, position):
        try:
            return self.hand.pop(position)
        except:
            print ("ERRO DISCARD")

    def showHand(self):
        return self.hand

class Zone:
    def __init__ (self):
        self.card = []

    def putcard_field(self, Player, position):
        try:
            if (len(self.card) == 0):
                self.card.append(Player.discard(position))
            else:
                self.card.pop(0)
                self.card.append(Player.discard(position))
            return self.card[0]
        except:
            print ("Erro!")

    def show_zone(self):
        return self.card

true = 0

c1 = Card("c1",2)
c2 = Card("c2",2)
c3 = Card("c3",3)
c4 = Card("c4",2)
c5 = Card("c5",3)

d1 = Deck()

d1.add_card(c2.name)
d1.add_card(c3.name)
d1.add_card(c1.name)
d1.add_card(c4.name)
d1.add_card(c5.name)
d1.shuffle()

d2 = Deck()

d2.add_card(c2.name)
d2.add_card(c3.name)
d2.add_card(c1.name)
d2.add_card(c4.name)
d2.add_card(c5.name)
d2.shuffle()

p1 = Player()
p2 = Player()
print('initial: ',p1.draw_initial(d1))
p2.draw_initial(d2)

z1 = Zone()
z2 = Zone()


while (true == 0):

    for carta in p1.showHand():
        print ("HAND: ",  str(p1.showHand().index(carta)) + ' - ' + carta )


    posicao = int(input("\nDigite um número...\n"))
    posicao_enemy = random.randint(0,2)
    while (posicao >= len(p1.showHand()) -1 or posicao < len(p1.showHand()) - 1):
        posicao = int(input("\nDigite um número...\n"))
        
    z1.putcard_field(p1, posicao)
    z2.putcard_field(p2, posicao_enemy)

    os.system('cls')
    print("ZONE: ", z1.show_zone(), "\nZONE_ENEMY: ", z2.show_zone())

    for carta in (z1.show_zone()):
        if (carta == c1.name):
            valor = c1.type
        if (carta == c2.name):
            valor = c2.type
        if (carta == c3.name):
            valor = c3.type
        if (carta == c4.name):
            valor = c4.type
        if (carta == c5.name):
            valor = c5.type

    for carta in (z2.show_zone()):
        if (carta == c1.name):
            valor_inimigo = c1.type
        if (carta == c2.name):
            valor_inimigo = c2.type
        if (carta == c3.name):
            valor_inimigo = c3.type
        if (carta == c4.name):
            valor_inimigo = c4.type
        if (carta == c5.name):
            valor_inimigo = c5.type

    print("\nSeu valor: {}\nValor inimigo: {}".format(valor, valor_inimigo))
    if (valor > valor_inimigo):
        print("\n\nVocê Venceu!")
    elif (valor < valor_inimigo):
        print ("\n\nVocê Perdeu!")
    else:
        print ("\n\nEmpate!")

    p1.draw(d1)
    p2.draw(d2)

    if (len(p1.showHand()) and len(p2.showHand()) == 0):
        print ("FIM")
        true = 1