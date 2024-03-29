list = [0,1,6,2,1,6,4,2,9,1]
for item in list:
    count = list.count(item)
    if count > 1:
        list.remove(item)
print(list)