num1=int(input("Digite o primeiro valor:"))
num2=int(input("Digite o segundo valor:"))
num3=int(input("Digite o terceiro valor:"))
lista=[]
if num1%6==0:
    lista.append(num1)
if num2%6==0:
    lista.append(num2)
if num3%6==0:
    lista.append(num3)
print(f"Os numeros que são divisíveis por 2 e 3 são: {lista}")
