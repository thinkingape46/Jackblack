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

    def __init__(self,playername='Player'):

        self.playername = playername

        pass
    
    def player(self):

        self.playername = input("Please enter your name: ")

        pass
    
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
    
    def __init__(self, score = 0, bet = 0, balance = 100, deck = []):

        self.score = score
        self.balance = balance
        self.deck = deck
        self.bet = bet

        self.bet = int(input("Please enter your bet amount: "))

        pass     

    def play(self):      
    
        card1 = deckof52[-1][0]
        score1 = deckof52[-1][1]
        self.deck.append(card1)
        deckof52.pop()
        card2 = deckof52[-1][0]
        score2 = deckof52[-1][1]
        self.deck.append(card2)
        deckof52.pop()
        self.score = self.score + (score1 + score2)
        print(f"{deck1.playername} deck: {self.deck}")
        print(f"{deck1.playername} score: {self.score}")

        pass

    def play2(self):

        playeraction = input(f"\n{deck1.playername}, please choose between HIT or STAY: \n")
                    
        if playeraction == 'hit':
            card2 = deckof52[-1][0]
            score2 = deckof52[-1][1]
            self.deck.append(card2)
            deckof52.pop()

            self.score = self.score + score2
            print(f"\n{deck1.playername}, you have chosen to HIT, here is your card: \n")
            print(card2)
            print(f"{deck1.playername}, your deck: {self.deck}")
            print(f"and your score: {self.score}")

            if self.score > 21:

                balance2 = self.balance - self.bet    

                print("Dealer has won!")
                print(f"Your balance now is ₹{balance2}")

                pass
            else:
                player1.play2()

        elif playeraction == 'stay':
            pass




deck1 = Deck()
deck1.player()
dealer1 = Dealer()
player1 = Player()
dealer1
player1
player1.play()
player1.play2()

