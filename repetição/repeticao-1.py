# Exercício 1
# Monte um programa que peça, um de cada vez, vários númeroos para o usuário 
# até que ele digite zero. Ao fim , mostre a soma de todos esses números que ele digitou.

num = int(input("Digite um número: "))
somatorio = 0

while num != 0:
    somatorio = somatorio + num
    num = int(input("Digite um número: "))

print(f"a soma total é: {somatorio} ")
