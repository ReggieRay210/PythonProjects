# Blackjack game
h1 = list(input("Player1 - Give me your cards:"))
h2 = list(input("Player2 - Give me your cards:"))
def blackjack_counter(hand):
  face_cards = ["j",'k', 'q']
  total_count = 0
  number_of_aces_in_hand = 0
  for card in hand: 
    if card.lower() in face_cards: 
      total_count = total_count + 10
    elif card.lower() == "a":
      number_of_aces_in_hand = number_of_aces_in_hand + 1 
    else: 
      total_count = total_count + int(card)
  total_count = total_count + number_of_aces_in_hand
  while total_count + 10 <= 21 and number_of_aces_in_hand > 0:
    total_count = total_count + 10 
    number_of_aces_in_hand = number_of_aces_in_hand -1  
  return total_count

def blackjack_winner(hand1, hand2):
  player1_total = blackjack_counter(hand1)
  player2_total = blackjack_counter(hand2)
  if player1_total <= 21 and (player1_total > player2_total or player2_total > 21):
    return "Player 1 win with {} and Player 2 with {}.".format(player1_total, player2_total)
  else:
    return "Player 2 win with {} and Player 1 with {}.".format(player2_total, player1_total)
blackjack_winner(h1, h2)
