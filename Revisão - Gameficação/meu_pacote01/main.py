
from operacoes import somar
from funcoes import verificar_inicio
from funcoes import criar_arquivo

#atividade criar módulo básico pag:2

a = 10
b = 5
resultado = somar(a, b)

print(f"A soma de {a} e {b} é {resultado}")


#atividade criar função veriificar_começo pag:3

texto_usuario = input("Digite uma frase: ")

verificar_inicio(texto_usuario)

#atividade de criar uma função para criar e escrever em um arquivo pag:5

nome_arquivo = input("Digite o nome do arquivo (com .txt): ")
conteudo = input("Digite o conteúdo que deseja escrever no arquivo: ")