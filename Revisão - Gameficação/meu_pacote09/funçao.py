def solicitar_entrada():
    """Solicita um número ao usuário e trata exceções para entradas inválidas."""
    while True:
        try:
            numero = float(input("Digite um número: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def main():
    with open("multiplicados.txt", "w") as arquivo:
        for i in range(10):
            print(f"\nIteração {i + 1}:")
            
            N1 = solicitar_entrada()
            N2 = solicitar_entrada()
            
            resultado = N1 * N2
            
            arquivo.write(f"{N1} * {N2} = {resultado}\n")
            print(f"Resultado da multiplicação: {resultado}")
    
    print("\nTodos os resultados foram salvos em 'multiplicados.txt'.")

if __name__ == "__main__":
    main()