import random


class Jogador:
    def __init__(self, nome, idade, fichas=100):
        self.__nome = nome
        self.__idade = idade
        self.__fichas = fichas
        self.mao = []

    def get_nome(self):
        return self.__nome

    def get_fichas(self):
        return self.__fichas

    def set_fichas(self, valor):
        self.__fichas = valor

    def calcular_pontos(self):
        pontos = 0
        ases = 0

        for carta in self.mao:
            if carta in ['Q', 'J', 'K']:
                pontos += 10
            elif carta == 'A':
                pontos += 11
                ases += 1
            else:
                pontos += int(carta)

        while pontos > 21 and ases:
            pontos -= 10
            ases -= 1

        return pontos

    def fazer_aposta(self, valor):
        if valor <= self.__fichas:
            self.__fichas -= valor
            return valor
        else:
            return 0

    def __str__(self):
        return f"{self.__nome} (Idade: {self.__idade}, Fichas: {self.__fichas})"


class JogoBaralho:
    def __init__(self):
        self.cartas = ["Az", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q", "J", "K"]

    def distribuir_carta(self, deck, jogador):
        carta = random.choice(deck)
        jogador.mao.append(carta)
        deck.remove(carta)

    def valor_carta(self, carta):
        if carta in ["Q", "J", "K"]:
            return 10
        elif carta in ["Az"]:
            return 1
        else:
            return int(carta)


def main():
    while True:
        print("-" * 30)
        print("Bem Vindo ao jogo 21")
        print("-" * 30)
        nome1 = input("Digite o nome do jogador 1: ")
        idade1 = int(input("Digite a idade do jogador 1: "))
        fichas1 = int(input(f"Digite a quantidade de fichas para {nome1}: "))
        jogador1 = Jogador(nome1, idade1, fichas1)

        nome2 = input("Digite o nome do jogador 2: ")
        idade2 = int(input("Digite a idade do jogador 2: "))
        fichas2 = int(input(f"Digite a quantidade de fichas para {nome2}: "))
        jogador2 = Jogador(nome2, idade2, fichas2)
        jogo = JogoBaralho()

        while jogador1.get_fichas() > 0 and jogador2.get_fichas() > 0:
            deck = jogo.cartas.copy()
            random.shuffle(deck)

            jogador1.mao.clear()
            jogador2.mao.clear()

            for _ in range(2):
                jogo.distribuir_carta(deck, jogador1)
                jogo.distribuir_carta(deck, jogador2)

            print(f"{jogador1.get_nome()}, sua mão: {jogador1.mao}, pontos: {jogador1.calcular_pontos()}")
            print(f"{jogador2.get_nome()}, sua mão: ['{jogador2.mao[0]}', '?'], pontos: ?")

            while True:
                opcao = input("Deseja 'pedir' ou 'parar'? ").lower()

                if opcao == 'pedir':
                    jogo.distribuir_carta(deck, jogador1)
                    print(f"{jogador1.get_nome()}, sua mão: {jogador1.mao}, pontos: {jogador1.calcular_pontos()}")

                    if jogador1.calcular_pontos() > 21:
                        print(f"{jogador1.get_nome()} estourou! {jogador2.get_nome()} ganha.")
                        break
                elif opcao == 'parar':
                    break

            while jogador1.calcular_pontos() <= 21:
                while jogador2.calcular_pontos() < 17:
                    jogo.distribuir_carta(deck, jogador2)

                print(f"{jogador2.get_nome()}, sua mão: {jogador2.mao}, pontos: {jogador2.calcular_pontos()}")

                if jogador2.calcular_pontos() > 21:
                    print(f"{jogador2.get_nome()} estourou! {jogador1.get_nome()} ganha.")
                elif jogador1.calcular_pontos() > jogador2.calcular_pontos():
                    print(f"{jogador1.get_nome()} ganha!")
                elif jogador1.calcular_pontos() < jogador2.calcular_pontos():
                    print(f"{jogador2.get_nome()} ganha.")
                else:
                    print("Empate!")

                break

            novo_jogo = input("Deseja jogar novamente? (sim/não): ").lower()
            if novo_jogo != 'sim':
                break


if __name__ == "__main__":
    main()