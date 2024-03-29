import random
import time

def randNum():
    num = format((random.random()*10), '.2f')
    return num

def getFirstName():
    itemFirstName = ['Banana ', 'Orange ', "Kellogg's ", "Holy ", "An Oversized Box of ",
                     "Strawberry ", "A 60 oz case of ", "Succulent ", "Jeremy's Famous ",
                     "Great Value ", "Peanut Butter ", "Cookies and Cream ", "Jelly ",
                     "Omega Deluxe ", "REALLY Juicy "]
    firstName = itemFirstName[random.randint(0, 14)]
    return firstName

def getLastName():
    itemLastName = ["Ice Cream", "Peanut Butter", "Flavored Toilet Paper", "Cheetos",
                    "Sprinkles", "Chicken Breast", "Seasoning", "Water", "Flavored Soda",
                    "Donuts", "Bull Testicles", "Flour", "Candy", "Low Sodium Salt",
                    "Brownies that may or may not be laced with various drugs"]
    lastName = itemLastName[random.randint(0, 14)]
    return lastName

def startGame():
    print("Game started!\n")
    time.sleep(1)

    total = 0
    cart = []
    while True:
        price = randNum()
        firstName = getFirstName()
        lastName = getLastName()
        choice = input(f"Would you like to buy {firstName}{lastName} for ${price}?\n> ").lower()
        if choice == "yes":
            cart.append((firstName + lastName))
            total += float(price)
            print(f"Item added to cart: Cart total is now ${format(total, '.2f')}\n")
            time.sleep(1)
        elif choice == "no":
            print("Skipping Item...\n")
            time.sleep(1)
        elif choice == "checkout":
            break
        else:
            print("I'm not sure what that means, I guess you don't want the item then\n")
    print("\nGoing to checkout...\n")
    time.sleep(1)
    print("You've checked out:")
    for item in cart:
        print(item)
        time.sleep(0.25)
    time.sleep(1)
    print(f"\nYour cart total is ${round(total, 2)}!")
    time.sleep(1)
    print("Let's hope you actually have the money to pay for it...")


print("You are at a grocery store looking for items to add to your cart.")
time.sleep(2)
print("You can type yes or no to add an item to your cart,")
time.sleep(2)
print("and at any time if you wish to checkout, type the command: checkout\n")
time.sleep(2)
begin = input("Would you like to begin?\n> ").lower()
if begin != "no":
    startGame()
else:
    print("Exiting Game...")
