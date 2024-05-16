import math

print('Gabriel Koiama - RA: 24.123.051-5')
print('João Pedro Peterutto - RA: 24.123.045-7')
print('João Pedro Lopes - RA: 24.123.071-3')
print('Vinicius Duarte - RA: 24.123.073-9\n')
print("O programa em questao foi criado para adquirir as intensidades em um sistema que pode conter ate 3 polarizadores. \nO principal conceito físico utilizado foi a Lei de Malus, determinando a intensidade por diferentes angulos ao longo dos polarizadores.
\nFoi seguido a risca o modelo de entradas e saidas propostos pela Professora Sueli Masunaga. \n")

def menu():
    print("Estudo da polarização da luz com programação \n")
    print("[1] Encerrar programa")
    print("[2] 2 Polarizadores")
    print("[3] 3 Polarizadores\n")
    i = int(input("Selecione a opcao desejada: "))
    print(" ")
    return i

def calc2():
    print("[0] Entrada: θ1, θ2 e I0")
    print("[1] Entrada: θ1, θ2 e I1")
    print("[2] Entrada: θ1, θ2 e I2")
    escolha = int(input("Selecione a opcao desejada: "))

    if escolha == 0:
        theta1 = float(input("Angulo do primeiro polarizador (em graus): "))
        theta2 = float(input("Angulo do segundo polarizador (em graus): "))
        I0 = float(input("Intensidade da luz incidente (em W/cm²): "))

        I1 = I0 / 2
        angulo = abs(theta1 - theta2)
        cossenoAngulo = math.cos(math.radians(angulo))
        I2 = I1 * cossenoAngulo**2

        print(f"\nIntensidade da luz apos o primeiro polarizador (I1): {I1:.2f} W/cm²")
        print(f"Intensidade da luz apos o conjunto de polarizadores (I2): {I2:.2f} W/cm²\n")

    elif escolha == 1:
        theta1 = float(input("Angulo do primeiro polarizador (em graus): "))
        theta2 = float(input("Angulo do segundo polarizador (em graus): "))
        I1 = float(input("Intensidade da luz apos o primeiro polarizador (em W/cm²): "))

        I0 = I1 * 2
        angulo = abs(theta1 - theta2)
        cossenoAngulo = math.cos(math.radians(angulo))
        I2 = I1 * cossenoAngulo**2

        print(f"\nIntensidade da luz incidente (I0): {I0:.2f} W/cm²")
        print(f"Intensidade da luz apos o conjunto de polarizadores (I2): {I2:.2f} W/cm²\n")

    elif escolha == 2:
        theta1 = float(input("Angulo do primeiro polarizador (em graus): "))
        theta2 = float(input("Angulo do segundo polarizador (em graus): "))
        I2 = float(input("Intensidade da luz apos o conjunto de polarizadores (em W/cm²): "))

        angulo = abs(theta1 - theta2)
        cossenoAngulo = math.cos(math.radians(angulo))
        I1 = I2 / cossenoAngulo**2
        I0 = I1 * 2

        print(f"\nIntensidade da luz incidente (I0): {I0:.2f} W/cm²")
        print(f"Intensidade da luz apos o primeiro polarizador (I1): {I1:.2f} W/cm²\n")
    
def calc3():
    print("[0] Entrada: θ1, θ2, θ3 e I0")
    print("[1] Entrada: θ1, θ2, θ3 e I1")
    print("[2] Entrada: θ1, θ2, θ3 e I2")
    print("[3] Entrada: θ1, θ2, θ3 e I3")
    escolha = int(input("Selecione a opcao desejada: "))

    if escolha == 0:
        theta1 = float(input("Angulo do primeiro polarizador (em graus): "))
        theta2 = float(input("Angulo do segundo polarizador (em graus): "))
        theta3 = float(input("Angulo do terceiro polarizador (em graus): "))
        I0 = float(input("Intensidade da luz incidente (em W/cm²): "))

        I1 = I0 / 2
        angulo1 = abs(theta1 - theta2)
        angulo2 = abs(theta2 - theta3)
        cossenoAngulo1 = math.cos(math.radians(angulo1))
        cossenoAngulo2 = math.cos(math.radians(angulo2))
        I2 = I1 * cossenoAngulo1**2
        I3 = I2 * cossenoAngulo2**2

        print(f"\nIntensidade da luz apos o primeiro polarizador (I1): {I1:.2f} W/cm²")
        print(f"Intensidade da luz apos o segundo polarizador (I2): {I2:.2f} W/cm²")
        print(f"Intensidade da luz apos o conjunto de polarizadores (I3): {I3:.2f} W/cm²\n")

    elif escolha == 1:
        theta1 = float(input("Angulo do primeiro polarizador (em graus): "))
        theta2 = float(input("Angulo do segundo polarizador (em graus): "))
        theta3 = float(input("Angulo do terceiro polarizador (em graus): "))
        I1 = float(input("Intensidade da luz apos o primeiro polarizador (em W/cm²): "))

        I0 = I1 * 2
        angulo1 = abs(theta1 - theta2)
        angulo2 = abs(theta2 - theta3)
        cossenoAngulo1 = math.cos(math.radians(angulo1))
        cossenoAngulo2 = math.cos(math.radians(angulo2))
        I2 = I1 * cossenoAngulo1**2
        I3 = I2 * cossenoAngulo2**2

        print(f"\nIntensidade da luz incidente (I0): {I0:.2f} W/cm²")
        print(f"Intensidade da luz apos o segundo polarizador (I2): {I2:.2f} W/cm²")
        print(f"Intensidade da luz apos o conjunto de polarizadores (I3): {I3:.2f} W/cm²\n")

    elif escolha == 2:
        theta1 = float(input("Angulo do primeiro polarizador (em graus): "))
        theta2 = float(input("Angulo do segundo polarizador (em graus): "))
        theta3 = float(input("Angulo do terceiro polarizador (em graus): "))
        I2 = float(input("Intensidade da luz apos o segundo polarizador (em W/cm²): "))

        angulo1 = abs(theta1 - theta2)
        angulo2 = abs(theta2 - theta3)
        cossenoAngulo1 = math.cos(math.radians(angulo1))
        cossenoAngulo2 = math.cos(math.radians(angulo2))
        I1 = I2 / cossenoAngulo1**2
        I0 = I1 * 2
        I3 = I2 * cossenoAngulo2**2

        print(f"\nIntensidade da luz incidente (I0): {I0:.2f} W/cm²")
        print(f"Intensidade da luz apos o primeiro polarizador (I1): {I1:.2f} W/cm²")
        print(f"Intensidade da luz apos o conjunto de polarizadores (I3): {I3:.2f} W/cm²\n")

    elif escolha == 3:
        theta1 = float(input("Angulo do primeiro polarizador (em graus): "))
        theta2 = float(input("Angulo do segundo polarizador (em graus): "))
        theta3 = float(input("Angulo do terceiro polarizador (em graus): "))
        I3 = float(input("Intensidade da luz apos o conjunto de polarizadores (em W/cm²): "))

        angulo1 = abs(theta1 - theta2)
        angulo2 = abs(theta2 - theta3)
        cossenoAngulo1 = math.cos(math.radians(angulo1))
        cossenoAngulo2 = math.cos(math.radians(angulo2))
        I2 = I3 / cossenoAngulo2**2
        I1 = I2 / cossenoAngulo1**2
        I0 = I1 * 2

        print(f"\nIntensidade da luz incidente (I0): {I0:.2f} W/cm²")
        print(f"Intensidade da luz apos o primeiro polarizador (I1): {I1:.2f} W/cm²")
        print(f"Intensidade da luz apos o segundo polarizador (I2): {I2:.2f} W/cm²\n")


while True:
    
    escolhaMenu = menu()

    if escolhaMenu == 1:
        break
    elif escolhaMenu == 2:
        print("Estudo de 2 polarizadores")
        calc2()
    elif escolhaMenu == 3:
        print("Estudo de 3 polarizadores")
        calc3()
    else:
        print("Digite um valor entre 1 e 3")
