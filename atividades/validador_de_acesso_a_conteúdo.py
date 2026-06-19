ano = int(input("Digite seu ano de nascimento: "))

idade = 2026 - ano

if idade > 16:
    print("Acesso Liberado.")
else : print("Acesso bloqueado: Conteúdo não recomendado para menores de 16 anos.")