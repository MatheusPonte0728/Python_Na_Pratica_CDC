# Exercício 3
# Peça ao usuário para digitar um username e uma senha. 
# Considere queop usuário correto é "admin" e que a senha correta é python2025. 
# Se as credenciais estiverem corretasm exiba "login bem sucedido!". 
# Do contrário, exiba que as crednciais estão incorretas.

# username = input("Digite seu username! ")
# senha = input("Digite sua senha! ")

# if (username == "admin") and (senha == "python2025"):
# print("Login bem sucedido!")
# else:    print("Credenciais incorretas!")

# Outra forma de fazer

username_correto = "admin"
senha_correta = "python2025"

username_entrada = input ("username: ")
senha_entrada = input ("senha: ")

if (username_entrada == username_correto) and (senha_entrada == senha_correta):
    print("Login bem sucedido!")
else:    print("Credenciais incorretas!")
