response = input("Please input your weight: ")
unit = input("Please selected which unit to convert to: \nlbs (L)\nkg (K)\n")
if unit.upper() == "L":
    outputLbs = int(response) * 2.205
    print(f"Your weight is {str(round(outputLbs, 2))} lbs")
elif unit.upper() == "K":
    outputKg = int(response) * 0.453
    print(f"Your WEIGHT is {str(round(outputKg,2))} kg")
