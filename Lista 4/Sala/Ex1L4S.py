A=[0]*5
b=[0]*5
for i in range(5):
    A[i]=int(input(f'Escolha o {i+1} elemento da sua lista: '))
for i in range(5):
    b[i]=A[i]*3

print(f'A lista B criada com base na primeira lista é: {b}')
