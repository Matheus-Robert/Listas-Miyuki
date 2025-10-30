A=[]
B=[]
for i in range(10):
    A.append(int(input(f'Digite os valores {i+1} da Lista A: ')))
for i in range(9, -1, -1):
    B.append(A[i])
print(f'Lista B: {B}')