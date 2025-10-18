mes=int(input('Digite o numero de um mes do ano (entre 1 e 12): '))
if mes<1 or mes>12:
    print('Numero invalido')
else:
    match mes:
        case 1:
            print("Janeiro")
        case 2:
            print("Fevereiro")
        case 3:
            print("Marco")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7:
            print("Julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")
            