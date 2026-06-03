# Exercício 3
# Monte um programa que, para um determinado número informado pelo usuário (limite), 
# exiba o dobro de cada npuermo de 1 até esse limite.

limite = int(input("Informe o limite: "))


for i in range (1, limite + 1):
    print(f"o dobro de {i} é: {i * 2}")
