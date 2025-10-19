sal=float(input('Digite seu salario: '))
hr=(int(input('Digite as horas trabalhadas: ')))



if sal<800:
        des=0
elif sal>=800 and sal<=1600:
        des=sal*0.13
else:
        des=sal*0.22

if hr>160:
    he=hr-160
    vh=(sal/160)
    add=he*vh*0.5

liq=sal-des+add

print(f'O salario liquido equivale a: {liq:.2f} reais')
        

        
    