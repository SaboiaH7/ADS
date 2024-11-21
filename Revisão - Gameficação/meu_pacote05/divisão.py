def dividir(valor, divisor=2):
    try:
        return valor / divisor
    except ZeroDivisionError:
        return "Erro: Divisão por zero não permitida."