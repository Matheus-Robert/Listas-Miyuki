nota=(float(input("Digite sua nota:")))
inteira=int(nota)
resto=(nota-inteira)

if resto>0.5:
    notaf=inteira+1
else:
    notaf=(nota-resto)
    
print(f"A nota arrendondada resulta em {notaf}")