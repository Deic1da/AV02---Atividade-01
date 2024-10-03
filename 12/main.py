import Conversor

print ("1 - Celsius > Fahrenheit\n2 - Fahrenheit > Celsius")
escolha = int(input("Escolha a conversão desejada: "))
temperatura = float(input("Digite a temperatura: "))

conversao = Conversor.conversor(escolha, temperatura)

print(conversao)