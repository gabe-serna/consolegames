import random
import sys

from colorama import Fore,init
init(autoreset=True)

board = [
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
    ["_","_","_","_","_"],
]
words = [
    "apple", "water", "table", "chair", "house", "mouse", "light", "night",
    "right", "drive", "cream", "dream", "plant", "green", "brown", "black",
    "white", "watch", "clock", "heart", "music", "beach", "peace", "happy",
    "smile", "child", "adult", "round", "cheap", "clean", "sharp", "young",
    "sweet", "quick", "sharp", "earth", "floor", "cloud", "sound", "radio",
    "money", "power", "train", "river", "honey", "chair", "shelf", "glass",
    "brush", "knife"
]
counter = 0
word = words[random.randint(0,49)].upper()
color_reference = {
    'Fore.GREEN': Fore.GREEN,
    'Fore.YELLOW': Fore.YELLOW
}

def start_game():
    print_board()
    guess_function()

def print_board():
    for row in range(0,5):
        for column in range(0,5):
            letter = board[row][column]
            end = "\n" if (column == 4) else ""
            if letter in word:
                color = "Fore.GREEN" if letter == word[column] else "Fore.YELLOW"
                print(color_reference[color] + letter, end=end)
            else:
                print(letter,end=end)

def guess_function():
    global counter
    while counter <= 4:
        guess = input("Guess a word: ").upper()
        print("\n")
        if len(guess) == 5:
            add_guess_to_board(guess)
        else:
            print("Guess must be 5 letters!")
            print_board()
            guess_function()
        if guess == word:
            if counter == 1:
                print(f"You have guessed the word in {counter + 1} guess!")
            else:
                print(f"You have guessed the word in {counter + 1} guesses!")
            sys.exit()
        counter += 1
    print(f"You have failed to guess the word! The word was {word}")

def add_guess_to_board(guess):
    x = 0
    for letter in guess:
        board[counter][x] = letter
        x += 1
    print_board()


start_game()
