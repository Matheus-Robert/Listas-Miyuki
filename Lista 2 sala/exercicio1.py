nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota"))
media=(nota1+nota2+nota3)/3
if media>=6.0:
    print(f"parabens voce passou com média {media}.")
else:
    print(f"Infelizmente voce nao passou com média {media}")
    