print('Hello player. What is your name?')
playerName = input()
print('Nice to meet you ' + playerName + ', I am thinking of a number between 1 through 10. Guess the number...')
secretNumber = random.randint(1,10)
for guessesTaken in range (1, 4):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Guess is too low, Try Again.')
    elif guess > secretNumber:
        print('Guess is too high, Try Again.')
    else:
        break # This condition is the correct guess. 
if guess == secretNumber: 
    print('Congratulations, ' + playerName + '!, You have guess the correct number in ' + str(guessesTaken) + ' guesses.' )
else: 
    print('I was thinking of ' + str(secretNumber) + ' you lose.')
