# Exercicio 37
# Menu com nome

nome = ""
op = ""

while op != "3":
    print("1 - Digitar o nome")
    print("2 - Mostrar nome")
    print("3 - Sair")

op = input("Escolha: ")

if op == "1":
    nome  = input("Nome: ")

elif op == "2":
    print(nome)
