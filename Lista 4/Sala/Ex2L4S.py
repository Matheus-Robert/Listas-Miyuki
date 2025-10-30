import math
A=[]
B=[]
for i in range(6):
    A.append(int(input(f'Digite os valores {i+1} da Lista A: ')))
for i in range(6):
    B.append(math.factorial(A[i]))

print(B)