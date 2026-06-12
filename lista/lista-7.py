# len (onde verificamos o tamnho da nossa lista)

lista = [2.4, False, "caneta"]
print(f"Tipode lista: {type(lista)}")

print("Lista antes do pop")
print(lista)
tam = len(lista)
print(f"Tamnho da lista: {tam}")

lista.pop(1)

print("Lista após o pop")
print(lista)
tam = len(lista)
print(f"Tamnho da lista: {tam}")
