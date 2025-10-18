numchave=20

num=float(input('Digite Um numero entre 0 e 100: '))
if num<0 or num>100:
    print('Numero invalido.')
else:
    dist= abs(numchave-num)
    print(f'A distancia entre o numero chave e o numero {num} equivale a: {dist}')
