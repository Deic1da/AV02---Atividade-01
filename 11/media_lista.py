def media(lista):
    soma = 0
    quantidade = 0
    for i in range (len(lista)):
        soma += lista[i]
        quantidade += 1
    return soma/quantidade