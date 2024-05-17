#Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.

lis1 = [1, 2, 3]
lis2 = [2, 3,13]
rezilta = []
for item in lis1:
    if item not in lis2:
        rezilta.append(item)
for item in lis2:
    if item not in lis1:
        rezilta.append(item)
print(rezilta)  