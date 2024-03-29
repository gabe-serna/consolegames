import random
import sys
import time

name_list = [
    "apple", "banana", "orange", "strawberry", "grape", "watermelon", "kiwi",
    "pineapple", "peach", "pear", "mango", "blueberry", "avocado", "lemon",
    "tomato", "potato", "carrot", "lettuce", "broccoli", "cucumber", "onion",
    "garlic", "eggplant", "pepper", "cherry", "plum", "apricot", "grapefruit",
    "raspberry", "papaya", "melon", "pomegranate", "fig", "coconut", "lime",
    "bread", "cheese", "milk", "butter", "eggs", "yogurt", "cereal", "rice",
    "pasta", "salt", "pepper", "sugar", "coffee", "tea", "juice", "water",
    "toaster", "microwave", "blender", "refrigerator", "oven", "stove", "dishwasher",
    "mixer", "kettle", "grill", "food processor", "coffee maker", "slow cooker",
    "air fryer", "waffle iron", "rice cooker", "pressure cooker", "can opener",
    "cutting board", "knife", "spoon", "fork", "plate", "bowl", "cup", "glass",
    "mug", "napkin", "tablecloth", "chair", "sofa", "bed", "lamp", "clock",
    "picture frame", "mirror", "vase", "book", "television", "computer", "phone",
    "tablet", "headphones", "speaker", "remote", "keyboard", "mouse", "charger"
] # there are 114 items so indexes 0 - 113

def check_if_completed(word,hidden_word,guessed_words):
    if word != hidden_word:
        print(f"\n{hidden_word}\nYour guess was correct! {12 - len(guessed_words)} guesses remaining.")
    else:
        print(f"\n{hidden_word}\nYour guess was correct! You have correctly guessed the word!")
        time.sleep(1)
        sys.exit()

def is_guess_repeat(guess,guessed_words):
    for word in guessed_words:
        if word == guess:
            return True
    return False

def guessing(guess,word,hidden_word,guessed_words,is_repeated):
    if guess in word and not is_repeated:
        hidden_word = reveal_guessed_letters(guess, word, hidden_word)
        check_if_completed(word,hidden_word,guessed_words)
        return hidden_word
    elif guess not in word and not is_repeated:
        print(f"Incorrect guess. {12 - len(guessed_words)} guesses remaining.")
        return hidden_word
    else:
        print(f"You have already guessed {guess}. {12 - len(guessed_words)} guesses remaining.")
        return hidden_word

def reveal_guessed_letters(guess,word,hidden_word):
    i = 0
    while i < len(word):
        if word[i] == guess:
            array = list(hidden_word)
            array[i] = guess
            hidden_word = ''.join(map(str, array))
            i += 1
        else:
            i += 1
    return hidden_word


def guess_loop(word,hidden_word):
    guessed_words = []
    while len(guessed_words) <= 11:
        guess = input("Guess a letter: ").lower()
        is_repeated = is_guess_repeat(guess,guessed_words)
        guessed_words.append(guess)
        hidden_word = guessing(guess,word,hidden_word,guessed_words,is_repeated)
    print(f"\nYou have failed to guess the word! The word was {word}.")
    time.sleep(1)
    sys.exit()

def start_game():
    hidden_word = ""
    word = name_list[random.randint(0,112)]
    for letter in word:
        if letter != " ":
            hidden_word += "_"
        else:
            hidden_word += " "
    print(f"Guessing Game Begin!\n{hidden_word}\nThe word is {len(hidden_word)} letters long!")
    guess_loop(word,hidden_word)


start = input("Would you like to start the word guessing game? y/n\n>").lower()
if start == "y":
    print("Game Starting...\n")
    time.sleep(1)
    start_game()
else:
    time.sleep(1)
    print("Closing Game...")
