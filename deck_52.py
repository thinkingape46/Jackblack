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
shuffle(deckof52)
'''shuffles the list of cards'''

'''This while loop runs as long as 'allcards' is not empty'''
'''   while len(allcards) > 0:
        print(f"your card is {allcards[-1]}")
        allcards.pop()
        print(f"The strength of current deck is {len(allcards)}")
'''
'''
class Deck():

    def __init__(self,playername='Player'):

        self.playername = playername

        pass
    
    def player(self):

        self.playername = input("Please enter your name: ")

        pass
'''
    
class Dealer():

    def __init__(self, name = "Dealer", score = 0, bet = 0, balance = 100, deck = []):

        self.name  = name
        self.score = score
        self.balance = balance
        self.deck = deck
        self.bet = bet
    
    def run1(self):

        card1 = deckof52[-1][0]
        score1 = deckof52[-1][1]
        self.deck.append(card1)
        deckof52.pop()
        card2 = deckof52[-1][0]
        score2 = deckof52[-1][1]
        self.deck.append(card2)
        deckof52.pop()
        self.score = self.score + (score1 + score2)

        print(f"Dealers deck: {self.deck[0]} **")
        print(f"Dealers score: {score1} + *")

        player1.play()

    def run2(self):

        if self.score == player1.score == 21:

            print("It's a DRAW!")

        elif self.score > 21:

            player1.balance = player1.balance + player1.bet
            print("Dealer BUST!")
            print(f"You won the bet!, your balance now: {player1.balance}")

        elif self.score > player1.score:

            print("Dealer has won!")
            print(f"{self.deck}")

        else:
            card3 = deckof52[-1][0]
            score3 = deckof52[-1][1]
            self.deck.append(card3)
            deckof52.pop()
            self.score = self.score + score3

            print(f"Dealers deck: {self.deck}")
            print(f"Dealers score: {self.score}")

            if self.score < 21:

                dealer1.run2()

            elif self.score > 21:

                player1.balance = player1.balance + player1.bet
                print("Dealer BUST!")
                print(f"You won the bet!, your balance now: {player1.balance}")


        

class Player():
    
    def __init__(self, name = "player", score = 0, bet = 0, balance = 100, deck = []):

        self.name  = name
        self.score = score
        self.balance = balance
        self.deck = deck
        self.bet = bet

    def initialinput(self):

        self.name = input("Please enter you name: ")
        self.bet = int(input("Please enter your bet amount: "))

        dealer1.run1()

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
        print(f"{self.name}, your deck: {self.deck}")
        print(f"and your score: {self.score}")

        if self.score > 21:
            
            balance2 = self.balance - self.bet    

            print("Dealer has won!")
            print(f"Your balance now is ₹{balance2}\n")
            print(f"Dealer deck: {dealer1.deck}")

        else:

            player1.play2()

    def play2(self):

        playeraction = input(f"\n{self.name}, please choose between HIT or STAY: \n")
                    
        if playeraction == 'hit':
            card2 = deckof52[-1][0]
            score2 = deckof52[-1][1]
            self.deck.append(card2)
            deckof52.pop()

            self.score = self.score + score2
            print(f"You have chosen to HIT, here is your card: \n")
            print(card2)
            print(f"Your deck now: {self.deck}")
            print(f"and your score: {self.score}")

            if self.score > 21:

                balance2 = self.balance - self.bet    

                print("Dealer has won!")
                print(f"Your balance now is ₹{balance2}\n")
                print(f"Dealer deck: {dealer1.deck}")

                pass
            else:
                player1.play2()

        elif playeraction == 'stay':
            dealer1.run2()

player1 = Player()
dealer1 = Dealer()
player1.initialinput()



