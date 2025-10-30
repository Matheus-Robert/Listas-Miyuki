A=[]
B=[]
for i in range(9):
    A.append(int(input(f'Digite o valor {i+1} do RA:  ')))
B = A
B[5],B[6],B[7],B[8] = B[8],B[7],B[6],B[5]
print(f'Lista B: {B}')