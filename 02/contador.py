def contador(numero):
    retirar = "+-"
    
    for i in retirar:
        numero = numero.replace(i,f"")
    
    quantidade = len(numero)
    return quantidade