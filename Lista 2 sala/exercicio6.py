import math
a=float(input("Digite o valor de A: "))
b=float(input("Digite o valor de B: "))
c=float(input("Digite o valor de C: "))

delta=b**2-4*a*c
if delta<0:
    print("Raiz sem solução real.")
elif delta==0:
    x1=(-b+math.sqrt(delta))/(2*a)
    print(f"Raizes reais iguais {x1}")
else:
    x1=(-b+math.sqrt(delta))/(2*a)
    x2=(-b-math.sqrt(delta))/(2*a)
    print(f"As raizes equivalem a: {x1} e {x2}")
