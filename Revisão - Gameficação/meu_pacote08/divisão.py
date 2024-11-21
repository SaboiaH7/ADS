def fazer_divisao():
    while True:
        try:
            N1 = float(input("Digite o primeiro número (N1): "))
            N2 = float(input("Digite o segundo número (N2): "))
            
            if N2 == 0:
                raise ValueError("Não é possível dividir por zero. Tente novamente.")
            
            resultado = N1 / N2
            return resultado
        except ValueError as e:

            print(f"Erro: {e}. Tente novamente.")
        except Exception as e:

            print(f"Erro inesperado: {e}. Tente novamente.")

with open("divisao.txt", "w") as arquivo:
    for i in range(10):
        print(f"\nTentativa {i + 1}:")
        resultado_divisao = fazer_divisao()
        
        arquivo.write(f"Resultado da divisão {i + 1}: {resultado_divisao}\n")
        print(f"Resultado da divisão {i + 1}: {resultado_divisao}")
        
print("Os resultados das divisões foram salvos em 'divisao.txt'.")