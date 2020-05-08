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

numtostr_range()