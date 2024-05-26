class JogoDaVelha():
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.jogador_atual = "X"

    def exibirTabuleiro(self):
        for linha in self.tabuleiro:
            print("|".join(linha))
            print("-" * 5)

    def verificarVencedor(self):
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != ' ':
                return linha[0]

        for col in range(3):
            if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] != " ":
                return self.tabuleiro[0][col]

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != " ":
            return self.tabuleiro[0][0]
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != " ":
            return self.tabuleiro[0][2]

        return None

    def verificarEmpate(self):
        for linha in self.tabuleiro:
            if " " in linha:
                return False
        return True

    def fazerJogada(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == " ":
            self.tabuleiro[linha][coluna] = self.jogador_atual
            if self.jogador_atual == "X":
                self.jogador_atual = "O"
            else:
                self.jogador_atual = "X"
            return True
        return False

    def jogar(self):
        while True:
            self.exibirTabuleiro()
            linha = int(input(f"Jogador {self.jogador_atual}, escolha a linha (0, 1, 2): "))
            coluna = int(input(f"Jogador {self.jogador_atual}, escolha a coluna (0, 1, 2): "))

            if self.fazerJogada(linha, coluna):
                vencedor = self.verificarVencedor()
                if vencedor:
                    self.exibirTabuleiro()
                    print(f"Jogador {vencedor} venceu!")
                    break
                elif self.verificarEmpate():
                    self.exibirTabuleiro()
                    print("Empate!")
                    break
            else:
                print("Movimento inválido. Tente novamente.")

