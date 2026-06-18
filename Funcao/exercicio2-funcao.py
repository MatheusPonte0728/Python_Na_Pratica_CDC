# Exercício 2
# Crie uma função chamada calcular_velocidade_media que receba a distancia percorrida (em km) 
# e o tempo gasto para o edslocamento em (horas).

# A função deve calcular a velocidade media e devolvê-la arredondada com duas casa decimais.

def calcular_velocidade_media(distancia, tempo):
    resultado = distancia / tempo
    resultado = round(resultado, 2)

    return resultado

dist = int(input("Infomre a distancia (km): "))
tempo = int(input("Informe o tempo (h): "))

vel_media = calcular_velocidade_media(dist, tempo)

print(f"Velocidade média: {vel_media} km/h")
