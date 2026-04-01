# Exercicio 34
# Contar quantos numeros foram digitados

contador = 0
while True:
    numero = int(input("Digite um numero (0 para sair): "))

    if numero == 0:
        break
    contador = contador + 1

    print("Quantidade:", contador)
