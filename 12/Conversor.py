def conversor(escolha,temperatura):

    if escolha == 1:
        Celsius = temperatura
        Fahrenheit = Celsius * (9/5) + 32
        return f"{Celsius}°C = {Fahrenheit}°F"
    elif escolha == 2:
        Fahrenheit = temperatura
        Celsius = (Fahrenheit - 32) * 5/9
        return f"{Fahrenheit}°F = {Celsius}°C "