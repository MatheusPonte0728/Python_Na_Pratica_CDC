# Exercício 1
# Peça ao usuário para digitar a temperatura atual em Celsius. 
# Se for maior ou igual a 30, exiba "está muito quente!". 
# Se estiver acima ou igual a 20 e abaixo de 30, exiba "es´ta agradável!". 
# Se tiver abaixo de 20 exiba "está muito frio!".

temperatura = float(input("Digite temperatura em Celsius: "))

if temperatura >=30:
    print("Está muito quente!")
elif (temperatura >=20) and (temperatura <30):
    print("Está agradável!")
else:    print("Está muito frio!")
