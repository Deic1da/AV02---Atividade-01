import Calculador_fatorial

while(True):
    try:
        numero = int(input("Digite um número: "))

        if numero < 0:
            raise ValueError("Numero negativo!")

        resultado = Calculador_fatorial.calculador_fatorial(numero)

        print(resultado)

    except ValueError as erro:
        print(f"Erro: {erro}")
