# Exercício 1(lista) - Crie uma lista chamada países com alguns nomes de países dentro dela. Em seguida:  
# - Adicione um novo país ao fim da lista 
# - Adicione um novoo país logo antes da posição 1 
# - Remova uma país pelo nome 
# - Remova um país pelo indice 
# - Mostre o total de países na lista.

paises = ["Brasil", "Argentina", "Portugal", "França" ]
print(paises)

paises.append("Espanha")
print(paises)

paises.insert(1, "Haiti")
print(paises)

paises.remove("Haiti")
print(paises)

paises.pop(4)
print(paises)

tam = len(paises)
print(f"Tamnho da lista: {tam}")
