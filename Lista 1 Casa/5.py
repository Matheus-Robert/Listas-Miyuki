Valor=float(input("Digite o valor que deve:"))
taxa=float(input("Digite a taxa:"))
tempo=float(input("Digite o tempo que deve:"))

PRESTAÇÃO= Valor + (Valor * (taxa / 100) * tempo)

print(f'A prestação equivale a: {PRESTAÇÃO}')
