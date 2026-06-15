dicionario = {
    "nome": "Matheus",
    "estado": "Ceará",
    "altura": 1.80
}

print(f"Tipo do diciionário: {type(dicionario)}")

print("Dicionário antes da modificação")
print(dicionario)

dicionario["nome"] = "Dev Matheus"
dicionario["Linguagem"] = "python"

print("Dicionário após a modificação")
print(dicionario)

print(dicionario["nome"])
print(dicionario["estado"])

