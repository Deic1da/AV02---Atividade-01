from calcular import somar,subrair,multiplicar,dividir

print ("1 - Somar\n2 - Subtrair\n3 - Multiplicar\n4 - Dividir\n")

escolha = int(input("Escolha um opção: "))
numero1 = float(input("Digite o primerio número: "))
numero2 = float(input("Digite o segundo número: "))

if escolha == 1:
    print(f"O resultado é {somar(numero1,numero2)}")
elif escolha == 2:
    print(f"O resultado é {subrair(numero1,numero2)}")
elif escolha == 3:
    print(f"O resultado é {multiplicar(numero1,numero2)}")
elif escolha == 4:
    print(f"O resultado é {dividir(numero1,numero2)}")