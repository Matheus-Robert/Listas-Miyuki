nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
media=(nota1+nota2)/2
if media>=6.0:
    print(f"parabens, voce passou com media {media}")
else:
    nota_exame=float(input("Digite a nota do exame")) #alt f5
    media_f=(media+nota_exame)/2
    if nota_exame>=5.0:
        print(f"Voce passou com media {media_f}")
    else:
        print(f"Voce nao passou com media {media_f}")