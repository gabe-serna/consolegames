numbers = [62,12,14,16,2,53,20,123,14,77,11,5,169,92,39]

# basic ass searching algo
reference = 0
firstIndex = numbers[0]
i = 0
while i < len(numbers)-1:
    if numbers[i+1] > numbers[i]:
        reference = numbers[i+1]
    i += 1

if reference > firstIndex:
    print(f"Highest Number in the list is {reference}")
else:
    print(f"Highest Number in the list is {firstIndex}")
print("----------------------")

numbers2 = [62,12,14,16,2,53,20,123,14,77,11,5,169,92,39]

max = numbers2[0]
for number in numbers:
    if number > max:
        max = number
print(max)