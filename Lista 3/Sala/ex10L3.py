soma=0
numero=1
for numero in range(1, 501):
    if numero%2==0:
        soma+=numero
    numero+=1
print(f'A soma dos numeros pares de 1 a 500 equivale a:{soma}')