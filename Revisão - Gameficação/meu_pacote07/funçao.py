palavras = [input(f"Digite a palavra {i+1}: ") for i in range(10)]

with open("palavras_a.txt", "w") as file_a, open("demais_palavras.txt", "w") as file_b:
    for palavra in palavras:

        if palavra.lower().startswith("a"):
            file_a.write(palavra + "\n")
        else:
            file_b.write(palavra + "\n")

print("Palavras salvas nos arquivos palavras_a.txt e demais_palavras.txt")