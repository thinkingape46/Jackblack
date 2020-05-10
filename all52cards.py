'''
This files just prints out all the 52cards in deck as list of tuples.
for (a,b) in the list, a represents the card type and b represents the cardvalue (1 to 10).
Value for ace is set to A, a value of 1 or 11 can be assigned later.
'''

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

print(deckof52)
