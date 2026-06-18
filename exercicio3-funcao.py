# Crie uma função chamada notas_aprovadas que receba uma lista de notas(lista de floats) 
# e retorne uma lista apenas com as notas maiores ou iguais a sete

def notas_aprovadas(lista_notas):
    lista_aprovadas = []

    for nota in lista_notas:
        if nota >= 7.0:
            lista_aprovadas.append(nota)
    
    return lista_aprovadas

lista_notas_alunos = [10.0, 4.5, 7.5, 7.0,  9.0]
lista_resultante = notas_aprovadas(lista_notas_alunos)

print("Notas aprovadas")
print(lista_resultante)
