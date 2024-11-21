def soma_multiplo_de_3(arquivo):
    soma = 0
    try:
        with open(arquivo, 'r') as file:
            for linha in file:
                try:
                    numero = int(linha.strip())  
                    if numero % 3 == 0:  
                        soma += numero
                except ValueError:
                    print(f"Atenção: '{linha.strip()}' não é um número válido e foi ignorado.")
        
        print(f"A soma dos múltiplos de 3 é: {soma}")
    
    except FileNotFoundError:
        print(f"Erro: o arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

arquivo = 'valores.txt'  
soma_multiplo_de_3(arquivo)