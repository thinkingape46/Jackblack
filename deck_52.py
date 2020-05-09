numrange = list(range(1,14))
cardvalues = [str(x) for x in numrange]
suitlist = ['♣','♦','♥','♠']
clubs = [suitlist[0]+a for a in cardvalues]
clubs2 = list(zip(clubs,numrange))
diamonds = [suitlist[1]+a for a in cardvalues]
diamonds2 = list(zip(diamonds,numrange))
hearts = [suitlist[2]+a for a in cardvalues]
hearts2 = list(zip(hearts,numrange))
spades = [suitlist[3]+a for a in cardvalues]
spades2 = list(zip(spades,numrange))
deckof52 = (clubs2 + diamonds2+ hearts2 + spades2)

from random import shuffle
shuffle(deckof52)
'''shuffles the list of cards'''

'''This while loop runs as long as 'allcards' is not empty'''
'''   while len(allcards) > 0:
        print(f"your card is {allcards[-1]}")
        allcards.pop()
        print(f"The strength of current deck is {len(allcards)}")
'''
class Deck():

    def __init__(self,name):

        self.name = name        
        print(f"Your name is {name}.")        

    def pocker(self,cash = 100):
        self.cash = cash
    
    def initial(self):

        print("Your cards are: ")
        print(f"{deckof52[-1]},{deckof52[-2]}")
    
class Dealer():
    def __init__(self,score=0,balance=100):

        self.score = score
        self.balance = balance

        deck = []
        card1 = deckof52[-1][0]
        score1 = deckof52[-1][1]
        deck.append(card1)
        deckof52.pop()
        card2 = deckof52[-1][0]
        score2 = deckof52[-1][1]
        deck.append(card2)
        deckof52.pop()
        newscore = score + (score1 + score2)
        print(f"Dealers deck: {deck}")
        print(f"Dealers score: {newscore}")

class Player():
    
    def __init__(self,score=10,balance=100):

        self.score = score
        self.balance = balance
    
        deck = []
        card1 = deckof52[-1][0]
        score1 = deckof52[-1][1]
        deck.append(card1)
        deckof52.pop()
        card2 = deckof52[-1][0]
        score2 = deckof52[-1][1]
        deck.append(card2)
        deckof52.pop()
        newscore = score + (score1 + score2)
        print(f"{name} deck: {deck}")
        print(f"{name} score: {newscore}")

name = input("Please enter your name:")        

dealer1 = Dealer()
player1 = Player()
dealer1
player1

