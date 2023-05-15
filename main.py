grau = int(input("Digite qual o grau da equação, só pode ser do primeiro e do segundo grau"))
if grau == 1:
    print("A equação é do primeiro grau")
    valorA = float(input("Digite o valor de a"))
    if valorA == 0:
        print("Valor de a inválido")
    elif valorA != 0:
        valorB = float(input("Digite o valor de b"))
        print(f"a raiz da equação '{valorA} * x + {valorB} = 0' é {-valorB/valorA:.2f}")
elif grau == 2:
    print("A equação é do segundo grau")
    valorA = float(input("Digite o valor de a"))
    if valorA == 0:
        print("Valor de a inválido")
    elif valorA != 0:
        valorB = float(input("Digite o valor de b"))
        valorC = float(input("Digite o valor de c"))
        delta = valorB**2 - 4*valorA*valorC
        if delta < 0:
            print("A equação não possui raízes reais")
        elif delta == 0:
            print("A equação possui uma raiz real")
            print(f"o valor da raiz é {-valorB/(2*valorA):.2f}")
        elif delta > 0:
            print("A equação possui duas raízes reais")
            resposta = delta
            resposta = resposta**0.5
            resposta2 = (-valorB + resposta)/(2*valorA)
            resposta3 = (-valorB - resposta)/(2*valorA)
            print(f"o valor de x1 é {resposta2:.2f}")
            print(f"o valor de x2 é {resposta3:.2f}")
else:
    print("Grau inválido")
