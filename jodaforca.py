import random

# função para escolher a palavra aleatória
def escolher_palavra():
    palavras = ["abacaxi", "banana", "caju", "damasco", "figo", "goiaba", "laranja", "manga", "pera", "uva"]
    return random.choice(palavras)

# função para exibir o estado atual da forca
def exibir_forca(vidas):
    if vidas == 6:
        print("  _______")
        print(" |/      |")
        print(" |")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 5:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 4:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |       |")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 3:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \_|")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 2:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \|_")
        print(" |")
        print(" |")
        print("_|___")
    elif vidas == 1:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \|/")
        print(" |")
        print(" |")
        print("_|___")
    else:
        print("  _______")
        print(" |/      |")
        print(" |      (_)")
        print(" |      \|/")
        print(" |       |")
        print(" |      / ")
        print("_|___")

# função para exibir a palavra atual com as letras adivinhadas
def exibir_palavra(palavra, letras_adivinhadas):
    for letra in palavra:
        if letra in letras_adivinhadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

# função para verificar se a letra está na palavra
def verificar_letra(letra, palavra):
    return letra in palavra

# função principal do jogo
def jogar_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = []
    vidas = 6

    while True:
        exibir_forca(vidas)
        exibir_palavra(palavra, letras_adivinhadas)

        if set(letras_adivinhadas) == set(palavra):
            print("Parabéns, você ganhou!")
            break

        if vidas == 0:
            print("Infelizmente, você perdeu. A palavra era", palavra)
            break

        letra = input("Digite uma letra: ")
        if letra in letras_adivinhadas:
            print("Você já tentou essa letra. Tente outra.")
        elif verificar_letra(letra, palavra):
            letras_adivinhadas.append(letra)
        else:
            vidas -= 1

# chamar a função
jogar_forca()
