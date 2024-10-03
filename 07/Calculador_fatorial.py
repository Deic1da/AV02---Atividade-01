def calculador_fatorial(numero):
    if numero == 0 or numero == 1:
        return numero
    else:
        return numero * calculador_fatorial(numero-1)