def contrario(string):
    palavra = ''
    for i in range(len(string) - 1, -1, -1):
        palavra += string[i]
    return palavra

texto = input("Digite uma palavra para ser invertida: ")
palavra_invertida = contrario(texto)
print("Palavra invertida:", palavra_invertida)
