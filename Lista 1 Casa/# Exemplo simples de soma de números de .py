tempo=float(input("Digite o tempo gasto na viajem(em horas):"))
velocidade_media=float(input("Digite a velocidade media da viagem(em metros por segundo): "))

distancia=tempo * velocidade_media
litros=distancia/12

print("Velocidade media:", velocidade_media , "metros por segundo")
print("Distancia:", distancia , "metros")
print("tempo:", tempo , "horas")
print(f'Litros: {litros:.2f} usados')



