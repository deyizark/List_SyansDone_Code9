#Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.

lis1 = [1, 3]
lis2 = [2, 3, 4]
rezilta = []
for n in lis1:
    if n in lis2 and n not in rezilta:
        rezilta.append(n)
print(rezilta)  