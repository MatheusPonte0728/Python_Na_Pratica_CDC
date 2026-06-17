# Exercício 2
# Monte um programa que, para um determinado número informado pelo usuário(limite), 
# exiba o produtório dos números de 1 até esse limite.

# produtorio = 1

# for i in range (1, 6):
#    print(f"Os números são: {i}")
#    produtorio = produtorio * i

#print(f"O produtório dos números são: {produtorio}")


# Solução do professor

limite = int(input("Informe o limite: "))
produtorio = 1

for i in range (1, limite + 1):
    print(f"Os números são: {i}")
    produtorio = produtorio * i

print(f"O produtório dos números são: {produtorio}")
