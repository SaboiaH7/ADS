from meu_pacote import soma, subtracao, divisao, multiplicacao
from meu_pacote.avancados import quadrado, cubo

a = 10
b = 5

print(f"Soma: {soma(a, b)}")
print(f"Subtração: {subtracao(a, b)}")
print(f"Divisão: {divisao(a, b)}")
print(f"Multiplicação: {multiplicacao(a, b)}")

print(f"{a} ao quadrado: {quadrado(a)}")
print(f"{a} ao cubo: {cubo(a)}")