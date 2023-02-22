# Define uma matriz vazia de 3x3 para representar o tabuleiro
tabuleiro = [[' ' for j in range(3)] for i in range(3)]

# Define os símbolos para os jogadores
jogador1 = 'X'
jogador2 = 'O'

# Define uma função para imprimir o tabuleiro
def imprimir_tabuleiro():
    for i in range(3):
        print('|'.join(tabuleiro[i]))

# Define uma função para verificar se um jogador ganhou
def verificar_vitoria(jogador):
    for i in range(3):
        # Verifica linhas
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
        # Verifica colunas
        if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
            return True
    # Verifica diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

# Define uma função para verificar se o jogo empatou
def verificar_empate():
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == ' ':
                return False
    return True

# Define uma função para solicitar a jogada do jogador
def solicitar_jogada(jogador):
    print("Vez do jogador " + jogador)
    while True:
        linha = input("Digite a linha (0 a 2) para a sua jogada: ")
        coluna = input("Digite a coluna (0 a 2) para a sua jogada: ")
        if linha.isdigit() and coluna.isdigit():
            linha = int(linha)
            coluna = int(coluna)
            if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
                if tabuleiro[linha][coluna] == ' ':
                    tabuleiro[linha][coluna] = jogador
                    break
                else:
                    print("Jogada inválida. A posição já está ocupada.")
            else:
                print("Jogada inválida. Linha e coluna devem estar entre 0 e 2.")
        else:
            print("Jogada inválida. Digite apenas números.")

# Loop principal do jogo
jogador_atual = jogador1
while True:
    imprimir_tabuleiro()
    solicitar_jogada(jogador_atual)
    if verificar_vitoria(jogador_atual):
        imprimir_tabuleiro()
        print("Jogador " + jogador_atual + " venceu!")
        break
    if verificar_empate():
        imprimir_tabuleiro()
        print("Empate!")
        break
    if jogador_atual == jogador1:
        jogador_atual = jogador2
    else:
        jogador_atual = jogador1
