### Exercício 1: A Tabuada Automatizada (Básico)
numero = 1

while numero != 0:
    numero = int(input("Digite o numero que voce deseja ver a tabuada"))

    for i in range (1, 11):
        print(f"{numero} x {i} = {numero*i}")