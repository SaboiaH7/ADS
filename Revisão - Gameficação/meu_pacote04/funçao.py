def filtrar_palavras(entrada, saida):
    with open(entrada, 'r') as arquivo_entrada:
        with open(saida, 'w') as arquivo_saida:
            for linha in arquivo_entrada:
                palavras = linha.split()
                for palavra in palavras:
                    if palavra.lower().startswith('b') and palavra.lower().endswith('o'):
                        arquivo_saida.write(palavra + '\n')

entrada = 'entrada.txt'  
saida = 'saida.txt'      

filtrar_palavras(entrada, saida)