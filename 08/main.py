import Verificador_numeros_primos

numero = int(input("Digite um número: "))

contador = Verificador_numeros_primos.verificador_numeros_primos(numero)

print(f"É {contador} que o número {numero} é primo")