# Exercício 2
# Peça ao usuário para digitar a idade de uma pessoa. 
# Com base nessa idade, informe o valor da tarifa de trnsporte que terá que ser paga. 
# Se a idade for menos de 6 anos, tarifa será gratuita. 
# Se for acima ou igual a 6 anos e abaixo de 18 anos, meia tarifa ($5). 
# Se for a partir de 18 anos e abaixo de 60 anos, tarifa interia ($10). 
# Se for idoso (acima de 60 anos), tarifa gratuia.

# idade = int(input("Digite a idade: "))

# if idade <6:
#    print("Tarifa gratuita!")
# elif (idade >=6) and (idade <18):
#    print("Meia tarifa $5,00")
# elif (idade >=18) and (idade <60):
#    print("Tarifa interira $10,00")
# else:    
#    print("Tarifa gratuita para idosos!")

# Outra maneira de fazer

idade = int(input("Digite a idade: "))

if idade <6:
    tarifa = 0.00
elif (idade >=6) and (idade <18):
    tarifa = 5.00
elif (idade >=18) and (idade <60):
    tarifa = 10.00
else:
    tarifa = 0.00

print(f"Tarifa a ser paga: R${tarifa:.2f}")