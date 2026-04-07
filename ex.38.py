# execrcicio 38
# verificar par ou impar

numero = 0
op =  ""

while op != "3":
    print("1 - Digitar numero")
    print("2 - verificar")
    print("3 - sair")

op = input("escolha: ")

if op == "1":
    numero = int(input("Numero: "))

elif op == "2":
    if numero %2 == 0:
        print ("par")
    else:
        print("Impar")