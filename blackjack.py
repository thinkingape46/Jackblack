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

        print("\nWELCOME TO BLACKJACK!\n")

        player1.initialinput()

    def restart(self):

        thegame1.deckof52 = cdhs_tuples + jk_tuples
        shuffle(thegame1.deckof52)

        dealer1.deck.clear()
        player1.deck.clear()

        dealer1.score = 0
        player1.score = 0
        player1.bet = 0
        player1.balance = 100

        print("\nWELCOME TO BLACKJACK!\n")

        player1.initialinput()

    def deck2(self):

        thegame1.deckof52 = cdhs_tuples + jk_tuples
        shuffle(thegame1.deckof52)
        shuffle(thegame1.deckof52)
        dealer1.deck.clear()
        player1.deck.clear()
        dealer1.score = 0
        player1.score = 0
        player1.bet = 0

        while True:

                try:
                    
                    player1.bet = int(input("Please enter your bet amount: "))

                except:

                    print("\nOnly enter positive integers for a bet!\n")
                    continue

                if player1.bet == 0:

                    print("\nOnly enter positive integers for a bet!\n")
                    continue

                if player1.bet < 0:

                    print("\nOnly enter positive integers for a bet!\n")
                    continue

                if player1.bet > player1.balance:

                    print("\nSorry! no funds, try reducing your bets.\n")
                    continue

                else:

                    break

        player1.balance = player1.balance - player1.bet

        dealer1.run1()            

    def decision(self):

        while True:

            try:

                dec = input("Do you wish to play again? (yes or no): ")

            except:

                print("Please enter only 'yes' or 'no'")
                continue

            if dec == 'yes' or dec == 'no' or dec == 'oui' or dec == 'non':
                
                break

            else:

                print("\nPlease enter only 'yes' or 'no': \n")
                continue

        if dec == 'yes' or dec == "oui":
            
            dealer1.deck.clear()
            player1.deck.clear()

            dealer1.score = 0
            player1.score = 0
            player1.bet = 0
            
            thegame1.restart()            

        elif dec == 'no' or dec == 'non':
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

            thegame1.deck2()        

        elif 'A' in str(dealer1.deck):

            if dealer1.score > 21:

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

                if dealer1.tempscore == 21:

                    dealer1.dealerwins()
                
                elif dealer1.tempscore > 21:

                    dealer1.dealerbusts()

                else:

                    print("\nDEALER HARD HAND")
                    print(f"Dealer deck: {dealer1.deck}")
                    print(f"Dealer score: {min(dealer1.score, dealer1.tempscore)}")

                    dealer1.dealer_ace_run()

            else:                
                dealer1.dealer_ace_run()

        elif dealer1.score > player1.score and dealer1.score < 21:

            '''Dealer wins here'''
            dealer1.dealerwins()

        elif dealer1.score == 21:

            '''Dealer wins here'''
            dealer1.dealerwins()

        elif dealer1.score > 21:

            dealer1.dealerbusts()

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

    def player_crosses_21(self):

        if dealer1.score > 21 and 'A' in str(dealer1.deck):

            dealer1.score = dealer1.score - 10

        else:
            pass

        dealer1.balance = dealer1.balance + player1.bet

        print("\nDEALER WON!")
        print(f"Dealer deck: {dealer1.deck}")
        print(f"Dealer score: {dealer1.score}\n")


        print(f"Your deck: {player1.deck}")
        print(f"Your score: {player1.score}")
        
        print(f"Your balance: {player1.balance}")

        print(f"\n{len(thegame1.deckof52)}")

        print(f"temp scores: {player1.tempscore},{dealer1.tempscore}")

        thegame1.deck2()

    def dealerwins(self):

        dealer1.balance = dealer1.balance + player1.bet

        print("\nDEALER WON!")
        print(f"Dealer deck: {dealer1.deck}")

        if 'A' in str(dealer1.deck) and dealer1.score > 21:
            print(f"Dealer score: {dealer1.tempscore}\n")
        else:
            print(f"Dealer score: {dealer1.score}\n")
        
        print(f"Your deck: {player1.deck}")

        if 'A' in str(player1.deck) and player1.score > 21:
            print(f"Your score: {player1.tempscore}")
        else:
            print(f"Your score: {player1.score}")
        
        print(f"Your balance: {player1.balance}")

        print(f"\n{len(thegame1.deckof52)}")

        print(f"temp scores: {player1.tempscore},{dealer1.tempscore}")
        
        if player1.balance <= 0:
            print("Sorry! No funds, you can't play anymore")
            print("\n")
            print("\nRESTARTING....\n")
            player1.balance = 100
            thegame1.decision()
        
        elif player1.balance > 0:
            thegame1.deck2()

    def dealerbusts(self):

        player1.balance = player1.balance + (2*player1.bet)

        print("\nDEALER BUST!")
        print(f"Dealer deck: {dealer1.deck}")

        if 'A' in str(dealer1.deck) and dealer1.score > 21:
            print(f"Dealer score: {dealer1.tempscore}\n")
        else:
            print(f"Dealer score: {dealer1.score}\n")

        print(f"Your deck: {player1.deck}")

        if 'A' in str(player1.deck) and player1.score > 21:
            print(f"Your score: {player1.tempscore}")
        else:
            print(f"Your score: {player1.score}")

        print(f"Your balance: {player1.balance}")

        print(f"\n{len(thegame1.deckof52)}")

        print(f"temp scores: {player1.tempscore},{dealer1.tempscore}")

        thegame1.deck2()

class Player():
    
    def __init__(self, name = "player", score = 0, bet = 0, balance = 100, deck = [], tempscore = 0):

        self.name  = name
        self.score = score
        self.balance = balance
        self.deck = deck
        self.bet = bet
        self.tempscore = tempscore

    def initialinput(self):

        self.name = input("Please enter you name: ")

        while True:

            try:
                
                player1.bet = int(input("Please enter your bet amount: "))

            except:

                print("\nOnly enter positive integers for a bet!\n")
                continue

            if player1.bet == 0:

                print("\nOnly enter positive integers for a bet!\n")
                continue

            if player1.bet < 0:

                print("\nOnly enter positive integers for a bet!\n")
                continue

            if player1.bet > player1.balance:

                print("\nSorry! no funds, try reducing your bets.\n")
                continue

            else:

                break
        
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

        player1.score = self.score + (score1 + score2)
        print(f"{self.name}, your deck: {self.deck}")
        print(f"and your score: {self.score}")
        print(f"Your bet: {player1.bet}")

        if player1.score == 21:

            dealer1.run2()

        else:

            player1.play2()

    def play2(self):

        while True:

            try:

                playeraction = input(f"\n{self.name}, please enter either hit or stand: \n")
            
            except:

                print("\nPlease enter only 'hit' or 'stand': \n")

            if playeraction == 'hit' or playeraction == 'stand':

                break

            else:

                continue
                    
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

            if 'A' in str(player1.deck):

                if self.score > 21:
                    
                    no_of_aces = []
                                
                    for char in str(player1.deck):

                        if char == 'A':
                            no_of_aces.append(char)

                        else:

                            pass
                
                    na = len(no_of_aces)
            
                    n = 1
                
                    while n < na + 1:

                        player1.tempscore = player1.score - 10*n
                        
                        if player1.tempscore > 21:

                            n += 1

                        else:

                            break

                    if player1.tempscore == 21:

                        player1.player_ace_run()
                
                    if player1.tempscore > 21:

                        dealer1.dealerwins()

                    else:

                        print("\nYou have a HARD HAND!")
                        print(f"You deck: {player1.deck}")
                        print(f"Your score: {min(player1.score, player1.tempscore)}")

                        player1.player_ace_run()

                else:

                    player1.player_ace_run()         

            elif player1.score == 21:

                dealer1.run2()

            elif player1.score > 21:

                dealer1.dealerwins()   
            
            else:
                player1.play2()

        elif playeraction == 'stand':
            dealer1.run2()

    def player_ace_run(self):

        temptotal = min(player1.score, player1.tempscore)

        if temptotal == 0:

            print(f"\nYour deck: {self.deck}")
            print(f"Your score: {player1.score}")

        else:

            print(f"\nYour deck: {self.deck}")
            print(f"Your score: {temptotal}")

        player1.play2()

player1 = Player()
dealer1 = Dealer()
cards1 = Cards()
thegame1 = TheGame()
thegame1.deck()
