#Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif

n = 8
result = []
for i in range(n + 1):
    if i % 2 == 0:
        result.append(i)
print(result)  