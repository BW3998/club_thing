from random import randrange
ans = randrange(1,101)
print("Welcome! You have 6 chances to guess my secret number!")
guess = input("What is your first guess? ")
i = 0
while i < 6 and guess != ans:
    guess = input("That's not right, try again!")
if guess == ans:
    print("You got it! Great job!")
else:
    print("Try again next time!")