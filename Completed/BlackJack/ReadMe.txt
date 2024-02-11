This program simulates the game of blackjack(21). Concept: each player will receive cards(in a list) and determine who wins based on the total value of the players hand. 
Hands are represented as a list of cards. Each card is represented by a string.
When adding up a hand's total, cards with numbers count for that many points. 
Facecards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
When determining a hand's total, you should try to count aces in the way that maximizes the hand's total without going over 21. 
e.g. the total of ['A', 'A', '9'] is 21, the total of ['A', 'A', '9', '3'] is 14.
