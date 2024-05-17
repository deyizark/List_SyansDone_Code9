#Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.

lis = [1, 1, 2, 3, 2, 4, 5]
lis_san_doublon = []
for i in lis:
    if i not in lis_san_doublon:
        lis_san_doublon.append(i)
print(lis_san_doublon)