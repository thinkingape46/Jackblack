''' This funtion creates a deck of 52 cards for blackjack game'''
from random import shuffle
def numtostr_range():

    numrange = list(range(1,14))
    cardvalues = [str(x) for x in numrange]
    suitlist = ['♣','♦','♥','♠']
    
    allcards = [a+b for a in cardvalues for b in suitlist]
    '''allcards is a list of 52 strings equivalent to deck of 52 cards, these cards are in a order.'''

    shuffle(allcards)
    '''shuffles the list of cards'''

    print(allcards)

def printcards():

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

    shuffle(deckof52)
    '''shuffles the list of cards'''

    '''This while loop runs as long as 'allcards' is not empty'''
    while len(allcards) > 0:
        print(f"your card is {allcards[-1]}")
        allcards.pop()
        print(f"The strength of current deck is {len(allcards)}")

class Deck():

    numrange = list(range(1,14))
    cardvalues = [str(x) for x in numrange]
    suitlist = ['♣','♦','♥','♠']


    '''allcards is a list of 52 strings equivalent to deck of 52 cards, these cards are in a order.'''

    '''shuffles the list of cards'''
    
    def __init__(self,name):

        self.name = name        
        print(f"Your name is {name}.")        

    def pocker(self,cash = 100):
        self.cash = cash
    
    def initial(self):
        clubs = [self.suitlist[0]+a for a in self.cardvalues]
        clubs2 = list(zip(clubs,self.numrange))
        diamonds = [self.suitlist[1]+a for a in self.cardvalues]
        diamonds2 = list(zip(diamonds,self.numrange))
        hearts = [self.suitlist[2]+a for a in self.cardvalues]
        hearts2 = list(zip(hearts,self.numrange))
        spades = [self.suitlist[3]+a for a in self.cardvalues]
        spades2 = list(zip(spades,self.numrange))
        deckof52 = (clubs2 + diamonds2+ hearts2 + spades2)
        shuffle(deckof52)
        print("Your cards are: ")
        print(f"{deckof52[-1]},{deckof52[-2]}")
    
class Dealer(Deck):

    def __init__(self,balance,score = 0):

        self.balance = balance
        self.score = score

        print(self.deckof52)



class Player(Deck):

    def __init__(self):
        pass



name = input("Hello, please enter your name:")

dealer1 = Dealer(100,score = 1)

dealer1()

