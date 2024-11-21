def palavras_com_m_e_a(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:

            texto = arquivo.read()
            
            palavras = texto.split()
            
            resultado = [palavra for palavra in palavras if palavra.lower().startswith('m') and palavra.lower().endswith('a')]

            if resultado:
                print("Palavras que começam com 'M' e terminam com 'A':")
                for palavra in resultado:
                    print(palavra)
            else:
                print("Nenhuma palavra encontrada que comece com 'M' e termine com 'A'.")
                
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

nome_arquivo = 'exemplo.txt'
palavras_com_m_e_a(nome_arquivo)