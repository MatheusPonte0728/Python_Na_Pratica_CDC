# Crie uma lista com números repetidos, e através da conversão desta para um conjunto, 
# elemine os valores duplicados.

lista = [1, 4, 3, 1, 6, 5, 3]

print(f"Tipo de lista: {type(lista)}")
print(lista)

conjunto_convertido = set(lista)

print(f"Tipo do conjunto convertido: {type(conjunto_convertido)}")
print(conjunto_convertido)

lista_convertida = list(conjunto_convertido)
print(f"Tipo da lista convertida: {type(lista_convertida)}")
print(lista_convertida)
