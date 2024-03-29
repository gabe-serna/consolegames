import random
x = random.randint(1,10)
def incorrectGuess(i):
    if i > 1:
        print("You guessed incorrectly, try again.")
        i -= 1
        return i
    elif i == 1:
        print("You have failed to guess the number correctly.")
        print(f"The correct number was {x}")
        i -= 1
        return i

i = 3
print("Guess a number between 1 and 10!")
while i >= 1:
    guess = int(input(f"({i} guesses remaining) Guess: "))
    if guess == x:
        print("You guessed correctly!")
        print(f"The number was {x}")
        break
    else:
        i = incorrectGuess(i)
