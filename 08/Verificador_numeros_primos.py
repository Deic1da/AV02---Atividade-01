def verificador_numeros_primos(numero):
    contador = 0
    for i in range (1,numero):
        if numero % i == 0:
            contador += 1
    if contador > 2:
        contador = False
    else:
        contador = True
    return contador