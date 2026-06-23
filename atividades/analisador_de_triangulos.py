retaA = float(input("Digite o comprimento da reta A: "))
retaB = float(input("Digite o comprimento da reta B: "))
retaC = float(input("Digite o comprimento da reta C: "))

if retaA + retaB < retaC or retaA + retaC < retaB or retaB + retaC < retaA:
    print("Triângulo Inválido.")
else:
    if retaA == retaB and retaA == retaC and retaC == retaB:
        print("Triângulo Equilátero.")
    elif retaA != retaB and retaB != retaC and retaA != retaC :
        print("Triângulo Escaleno.")
    else:
        print("Triângulo Isósceles.")








