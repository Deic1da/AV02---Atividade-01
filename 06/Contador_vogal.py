def contador_vogal(entrada):
    vogais = "aeiou"
    quantidade = 0

    for i in range (len(entrada)):
        if entrada[i] in vogais:
            quantidade += 1
            
    return quantidade