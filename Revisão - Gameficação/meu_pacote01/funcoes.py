def verificar_inicio(texto):
    if texto.startswith("Olá"):
        print("A frase começa com 'Olá'.")
    else:
        print("A frase não começa com 'Olá'.")


def criar_arquivo(nome_arquivo, conteudo):
    # Abrindo o arquivo no modo 'w' (write) para escrever no arquivo
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    print(f"Conteúdo foi escrito com sucesso no arquivo {nome_arquivo}.")