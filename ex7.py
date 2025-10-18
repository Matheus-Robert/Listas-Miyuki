cod=int(input('Digite o codigo de acesso (entre 0 e 5): '))
if cod<1 or cod>5:
    print('Numero invalido')
else:
    match cod:
        case 1:
            print("Engenharia")
        case 2:
            print("Edificacoes")
        case 3:
            print("Sistemas eletricos")
        case 4:
            print("Turismo")
        case 5:
            print("Analise de sistemas")
        