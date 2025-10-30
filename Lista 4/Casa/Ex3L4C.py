A=[]
B=[]
for i in range(9):
    A.append(int(input(f'Digite o valor {i+1} do RA:  ')))
B = A
B[0],B[1],B[7],B[8] = B[1],B[0],B[8],B[7]
print(f'Lista B: {B}')