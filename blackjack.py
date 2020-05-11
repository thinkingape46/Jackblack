suitlist = ['♣','♦','♥','♠']
jkq = ['J','K','Q']

numrange = list(range(2,11))
cardvalues = ['A'] + [str(x) for x in numrange]
jkq_values = [10,10,10]

cdhs = [a+b for a in  suitlist for b in cardvalues]
jk = [a+b for a in suitlist for b in jkq]

cdhs_tuples = list(zip(cdhs,cardvalues*10))
jk_tuples = list(zip(jk,jkq_values*4))


from random import shuffle


class TheGame():

    def __init__(self, action = ' ', deckof52 = []):

        self.action = action
        self.deckof52 = deckof52

    def deck(self):

        thegame1.deckof52 = cdhs_tuples + jk_tuples
        shuffle(thegame1.deckof52)

        player1.initialinput()

    def deck2(self):

        thegame1.deckof52 = cdhs_tuples + jk_tuples
        shuffle(thegame1.deckof52)
        shuffle(thegame1.deckof52)

        dealer1.run1()      
            

    def decision(self):

        dec = input("Do you wish to play again? (yes or no): ")

        if dec == 'yes':
            
            dealer1.deck.clear()
            player1.deck.clear()

            dealer1.score = 0
            player1.score = 0
            player1.bet = 0

            player1.bet = int(input("Please enter your bet amount: "))
            player1.balance = player1.balance - player1.bet

            thegame1.deck2()            

        elif dec == 'no':
            print("See you later!")
            exit()

class Cards():

    def score(self, value = 0):

        self.value = value
        
        if thegame1.deckof52[-1][1] == 'A':
            value = 11
        
        else:
            value = int(thegame1.deckof52[-1][1])
            
        return value


class Dealer():

    def __init__(self, name = "Dealer", score = 0, balance = 100, deck = [], tempscore = 0):

        self.name  = name
        self.score = score
        self.balance = balance
        self.deck = deck
        self.tempscore = tempscore
    
    def run1(self):

        card1 = thegame1.deckof52[-1][0]
        self.deck.append(card1)
        cards1.score()
        score1 = cards1.score()        
        thegame1.deckof52.pop()

        card2 = thegame1.deckof52[-1][0]
        self.deck.append(card2)
        cards1.score()
        score2 = cards1.score()        
        thegame1.deckof52.pop()

        self.score = self.score + (score1 + score2)

        print(f"\nDealers deck: {self.deck[0]} **")
        print(f"Dealers score: {score1} + *")

        player1.play()

    def run2(self):

        if self.score == 21 and player1.score == 21:

            print("It's a DRAW!")
            print(f"{self.deck}")

            thegame1.decision()

        elif dealer1.score > 21:

            if 'A' in str(dealer1.deck):

                no_of_aces = []
                                
                for char in str(dealer1.deck):
                
                    if char == 'A':
                        no_of_aces.append(char)
                    else:
                        pass
                
                na = len(no_of_aces)
            
                n = 1
                
                while n < na + 1:

                    dealer1.tempscore = dealer1.score - 10*n
                    
                    if dealer1.tempscore > 21:

                        n += 1

                    else:

                        break
                
                if dealer1.tempscore > 21:

                    dealer1.dealerbusts()

                else:

                    print("\nDEALER HARD HAND")
                    print(f"Dealer deck: {dealer1.deck}")
                    print(f"Dealer score: {min(dealer1.score, dealer1.tempscore)}")

                    dealer1.dealer_ace_run()

            else:
                
                '''Dealer busts here'''
                dealer1.dealerbusts()

        elif dealer1.score > player1.score and dealer1.score < 21:

            '''Dealer wins here'''
            dealer1.dealerwins()

        elif dealer1.score == 21:

            '''Dealer wins here'''
            dealer1.dealerwins()

        else:
            card3 = thegame1.deckof52[-1][0]
            self.deck.append(card3)
            cards1.score()
            score3 = cards1.score() 
            thegame1.deckof52.pop()
            self.score = self.score + score3

            dealer1.run2()

    def dealer_ace_run(self):

        temptotal = min(dealer1.score, dealer1.tempscore)

        card4 = thegame1.deckof52[-1][0]
        self.deck.append(card4)
        cards1.score()
        score3 = cards1.score() 
        thegame1.deckof52.pop()
        
        self.score = self.score + score3

        print(f"\nDealers deck: {self.deck}")
        print(f"Dealers score: {temptotal + score3}")

        dealer1.run2()       

        pass

    def dealerwins(self):

        dealer1.balance = dealer1.balance + player1.bet

        print("\nDEALER WON!")
        print(f"Dealer deck: {dealer1.deck}")
        print(f"Dealer score: {dealer1.score}\n")

        print(f"Your deck: {player1.deck}")
        print(f"Your score: {player1.score}")
        print(f"Your balance: {player1.balance}")

        print(f"\n{len(thegame1.deckof52)}")

        thegame1.decision()

    def dealerbusts(self):

        player1.balance = player1.balance + (2*player1.bet)

        print("\nDEALER BUST!")
        print(f"Dealer deck: {dealer1.deck}")
        print(f"Dealer score: {dealer1.score}\n")

        print(f"Your deck: {player1.deck}")
        print(f"Your score: {player1.score}")
        print(f"Your balance: {player1.balance}")

        print(f"\n{len(thegame1.deckof52)}")

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
        player1.balance = player1.balance - player1.bet

        dealer1.run1()

        pass     

    def play(self):      
    
        card1 = thegame1.deckof52[-1][0]
        self.deck.append(card1)        
        cards1.score()
        score1 = cards1.score()  
        thegame1.deckof52.pop()

        card2 = thegame1.deckof52[-1][0]
        self.deck.append(card2)
        cards1.score()
        score2 = cards1.score() 
        thegame1.deckof52.pop()

        self.score = self.score + (score1 + score2)
        print(f"{self.name}, your deck: {self.deck}")
        print(f"and your score: {self.score}")
        print(f"Your bet: {player1.bet}")

        if self.score == 21:

            dealer1.run2()

        else:

            player1.play2()

    def play2(self):

        playeraction = input(f"\n{self.name}, please choose between HIT or STAY: \n")
                    
        if playeraction == 'hit':

            card3 = thegame1.deckof52[-1][0]
            self.deck.append(card3)
            cards1.score()
            score3 = cards1.score()            
            thegame1.deckof52.pop()

            self.score = self.score + score3
            print(f"You have chosen to HIT, here is your card: \n")
            print(card3)
            print(f"Your deck now: {self.deck}")
            print(f"and your score: {self.score}")

            if self.score > 21:

                if 'A' in str(self.deck):

                    if self.score - 10 > 21:

                        '''Dealer wins here'''
                        dealer1.dealerwins()

                    else:
                        
                        self.score = self.score - 10
                        print("\nYou have a HARD HAND\n")
                        print(f"Your deck now: {self.deck}")
                        print(f"and your score: {self.score}")
                        player1.play2()

                else:
                    
                    '''Dealer wins here'''
                    dealer1.dealerwins()

                pass

            elif self.score == 21:

                player1.play2()
            
            else:
                player1.play2()

        elif playeraction == 'stay':
            dealer1.run2()

player1 = Player()
dealer1 = Dealer()
cards1 = Cards()
thegame1 = TheGame()
thegame1.deck()




