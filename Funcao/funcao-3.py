def produto(x, y):
    resultado = x * y
    return resultado

def soma(x, y):
    resultado = x + y
    return resultado

multiplicacao = produto(4, 8)
sum = soma(42, 4)

print(f"O resultado de 4 vezes 8 é: {multiplicacao}")
print(f"O resultado de 42 mais 4 é: {sum}")

diferenca = sum - multiplicacao

print(f"A diferença entre elas é: {diferenca}")
