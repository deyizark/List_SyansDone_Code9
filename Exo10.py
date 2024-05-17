lis1 = [1, 2, 3]
lis2 = [2, 3, 4]
lis3 = [4, 5, 6]
rezilta = []

for item in lis1:
    if item not in rezilta:
        rezilta.append(item)

for item in lis2:
    if item not in rezilta:
        rezilta.append(item)

for item in lis3:
    if item not in rezilta:
        rezilta.append(item)

print(rezilta)  