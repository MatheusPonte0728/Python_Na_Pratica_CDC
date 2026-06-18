# o código abaixo repete o mesmo cáculo várias vezes.

# Refatore-o, criando uma função que leia as notas do aluno, caucule média, 
# retornea arredondada com uma casa decimal e evite a repetição.

def cacular_media(numero_aluno):
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3
    media = round(media, 1)

    print(f"Média do aluno {numero_aluno}: {media}")

cacular_media(1)
cacular_media(2)
cacular_media(3)
