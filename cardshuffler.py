# This program will 'shuffle' a deck of cards and return a
# random combination of five cards

# Writtem by Gage Wooldridge

# import modules
import itertools
import random

# create deck list, itertools.product is equivalent to a nested
# for loop to create the deck with less code
deck = list(itertools.product(range(1,14),['Hearts', 'Clubs', 'Spades', 'Diamonds']

# shuffle deck with random.shuffle and call the deck
random.shuffle(deck)

# output five random cards
print("You got:")
for i in range(5):
    if int(deck[i][0]) < 10:	
        print(deck[i][0], "of", deck[i][1])
	elif int(deck[i][0]) = 11:
		print("Jack of", deck[i][1])
	elif int(deck[i][0]) = 12:
		print("Queem of", deck[i][1])
	elif int(deck[i][0]) = 13:
		print("King of", deck[i][1])
