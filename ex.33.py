# Exercicio 33
# Somar numeros ate digitar 0

soma = 0

while True:
    numero = int(input("Digite um numero (0 para sair): "))

    if numero == 0:
        break
    soma = soma + numero

    print("Soma: ", soma)