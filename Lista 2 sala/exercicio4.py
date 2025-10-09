A=float(input("Digite o lado A do triangulo: "))
B=float(input("Digite o valor do lado B do triangulo: "))
C=float(input("Digite o valor do lado C do triangulo:"))

if A+ B > C and A+C > B and B+C > A:
    if A==B == C:
        print("Equilátero")
    elif A == B or A == C or B == C:
        print('Isósceles')
    else:
        print("Escaleno")
else:
    print("Os lados fornecido nao formam um triangulo.")

    