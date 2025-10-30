A=[]
B=[]
C=[]
for i in range(5):
    A.append(int(input(f'Digite os valores {i+1} da Lista A: ')))
for i in range(5):
    B.append(int(input(f'Digite os valores {i+1} da lista B: ')))
C.append((A+ B))
print(f'Lista C: {C}')