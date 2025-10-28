N=int(input('Digite um numero menor ou igual a 50:'))
if N>50:
    print('Numero invalido.')
else:
    valor = N*3
    while valor<250:
     print(valor)
     valor=valor*3