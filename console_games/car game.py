import time
name = input("Please enter your name to get started: ")
print(f"\nAlright! Hello Player {name}!")
time.sleep(1)
print("Welcome to the RACING GAME!!!\n")
time.sleep(1)
print("Here are the commands that are available to you:")
time.sleep(1)
list = "help - shows all available commands\nstart - starts the car\nstop - stops the car\nquit - exit the game"
print(list)

response = input("> ").lower()
while response != "quit":
    if response == "help":
        print(list)
    elif response == "start":
        print("Car has started!")
    elif response == "stop":
        print("Car has stopped!")
    else:
        print("Unknown Input")
    response = input("> ").lower()
print("Stopping the game")
