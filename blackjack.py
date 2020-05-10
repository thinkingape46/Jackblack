suitlist = ['♣','♦','♥','♠']
jkq = ['J','K','Q']

numrange = list(range(2,11))
cardvalues = ['A'] + [str(x) for x in numrange]
jkq_values = [10,10,10]

cdhs = [a+b for a in  suitlist for b in cardvalues]
jk = [a+b for a in suitlist for b in jkq]

cdhs_tuples = list(zip(cdhs,cardvalues*10))
jk_tuples = list(zip(jk,jkq_values*4))
deckof52 = cdhs_tuples + jk_tuples

from random import shuffle
shuffle(deckof52)
shuffle(deckof52)

class TheGame():

    def __init__(self, action = ' '):

        self.action = action

    def decision(self):

        dec = input("Do you wish to play again? (yes or no)")

        if dec == 'yes':
            
            dealer1.deck.clear()
            player1.deck.clear()

            dealer1.score = 0
            player1.score = 0

            player1.bet = int(input("Please enter your bet amount: "))

            dealer1.run1()            

        elif dec == 'no':
            print("See you later!")

class Cards():

    def score(self, value = 0):

        self.value = value
        
        if deckof52[-1][1] == 'A':
            value = 11
        
        else:
            value = int(deckof52[-1][1])
            
        return value


class Dealer():

    def __init__(self, name = "Dealer", score = 0, balance = 100, deck = []):

        self.name  = name
        self.score = score
        self.balance = balance
        self.deck = deck
    
    def run1(self):

        card1 = deckof52[-1][0]
        self.deck.append(card1)
        cards1.score()
        score1 = cards1.score()        
        deckof52.pop()

        card2 = deckof52[-1][0]
        self.deck.append(card2)
        cards1.score()
        score2 = cards1.score()        
        deckof52.pop()

        self.score = self.score + (score1 + score2)

        print(f"\nDealers deck: {self.deck[0]} **")
        print(f"Dealers score: {score1} + *")

        player1.play()

    def run2(self):

        if self.score == 21 and player1.score == 21:

            print("It's a DRAW!")
            print(f"{self.deck}")

            thegame1.decision()

        elif self.score > 21:

            player1.balance = player1.balance + player1.bet
            print("\nDealer BUST!")
            print(f"{self.deck}")
            print(f"You won the bet!, your balance now: {player1.balance}")

            thegame1.decision()

        elif self.score > player1.score and self.score < 21:

            print("Dealer has won!")
            print(f"{self.deck}")
            player1.balance = player1.balance - player1.bet
            print(f"Your balance now: {player1.balance}")

            thegame1.decision()

        else:
            card3 = deckof52[-1][0]
            self.deck.append(card3)
            cards1.score()
            score3 = cards1.score() 
            deckof52.pop()
            self.score = self.score + score3

            print(f"\nDealers deck: {self.deck}")
            print(f"Dealers score: {self.score}")

            if self.score < 21:

                dealer1.run2()

            elif self.score == 21 and player1.score == 21:

                print("It's a DRAW!")
                print(f"{self.deck}")

                thegame1.decision()

            elif self.score > 21:

                player1.balance = player1.balance + player1.bet
                print("\nDealer BUST!")
                print(f"{self.deck}")
                print(f"You won the bet!, your balance now: {player1.balance}")

                thegame1.decision()       

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
        self.deck.append(card1)        
        cards1.score()
        score1 = cards1.score()  
        deckof52.pop()

        card2 = deckof52[-1][0]
        self.deck.append(card2)
        cards1.score()
        score2 = cards1.score() 
        deckof52.pop()

        self.score = self.score + (score1 + score2)
        print(f"{self.name}, your deck: {self.deck}")
        print(f"and your score: {self.score}")
        print(f"Your bet: {self.bet}")

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

            card3 = deckof52[-1][0]
            self.deck.append(card3)
            cards1.score()
            score3 = cards1.score()            
            deckof52.pop()

            self.score = self.score + score3
            print(f"You have chosen to HIT, here is your card: \n")
            print(card3)
            print(f"Your deck now: {self.deck}")
            print(f"and your score: {self.score}")

            if self.score > 21:

                if 'A' in str(self.deck):

                    if self.score - 10 > 21:

                        balance2 = self.balance - self.bet 
                        print("Dealer has won!")
                        print(f"Your balance now is ₹{balance2}\n")
                        print(f"Dealer deck: {dealer1.deck}")
                        print(f"Dealer score: {dealer1.score}")

                        thegame1.decision()

                    else:
                        
                        self.score = self.score + 10
                        print("\nHARD HAND\n")
                        player1.play2()

                else:
                    balance2 = self.balance - self.bet    

                    print("Dealer has won!")
                    print(f"Your balance now is ₹{balance2}\n")
                    print(f"Dealer deck: {dealer1.deck}")
                    print(f"Dealer score: {dealer1.score}")

                    thegame1.decision()

                pass
            
            else:
                player1.play2()

        elif playeraction == 'stay':
            dealer1.run2()

player1 = Player()
dealer1 = Dealer()
cards1 = Cards()
thegame1 = TheGame()
player1.initialinput()




