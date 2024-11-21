def exibir_palavras_terminadas_com_a(arquivo):
    try:
        with open(arquivo, 'r') as file:
            conteudo = file.read()
            palavras = conteudo.split()
            palavras_terminadas_com_a = [palavra for palavra in palavras if palavra.endswith('a')]

            if palavras_terminadas_com_a:
                print("Palavras que terminam com 'a':")
                for palavra in palavras_terminadas_com_a:
                    print(palavra)
            else:
                print("Não há palavras que terminam com 'a'.")
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

arquivo = 'arquivo.txt'

exibir_palavras_terminadas_com_a(arquivo)