a=float(input("Digite o primeiro numero"))
b=float(input("Digite o segundo numero"))
c=float(input("Digite o terceiro numero"))

val=sorted([a, b, c])

print(f'O maior numero e o numero {val[2]}')
print(f'O menor numero e o numero {val[0]}')
print(f'O numero do meio e o numero {val[1]}')