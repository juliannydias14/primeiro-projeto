salario = float(input("Digite seu salário bruto: "))

parcela = int(input("Qual o valor da parcela do seu empréstimo? "))

limite = salario *0.30

if parcela <= limite :
    print("Crédito Aprovado! ")

else :
    print("Crédito Não Aprovado!")



