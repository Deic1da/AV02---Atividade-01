from utils.calculador import *

print("As equações são:\nSoma (+)\nSubtração (-)\nDivisão (/)\nMultiplicação (*)")
print("EX: 9+7*8-5/3 = 63.333333333333336")
equacao = input("Digite aqui: ")

equacao = Calculador(equacao)

print(f"Resultado = {equacao}")