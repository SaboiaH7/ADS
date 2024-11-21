from pacote_divisao.divisao import dividir

def ler_valores_do_arquivo(arquivo):
    """
    Função para ler valores do arquivo e retornar como lista de inteiros.
    """
    try:
        with open(arquivo, 'r') as file:
            valores = [int(linha.strip()) for linha in file.readlines()]
        return valores
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
        return []
    except ValueError:
        print("Erro: O arquivo contém valores inválidos.")
        return []

def main():
    valores = ler_valores_do_arquivo('valores.txt')
    
    if not valores:
        return
    
    for valor in valores:
        resultado = dividir(valor)
        print(f'{valor} dividido por 2 é: {resultado}')

if __name__ == "__main__":
    main()