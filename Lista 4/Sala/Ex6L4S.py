A=[]
B=[]
for i in range(8):
    A.append(int(input(f'Digite os valores {i+1} da Lista A: ')))
for i in range(8):
    B.append(A[i]**2)
print(f'Lista B: {B}')