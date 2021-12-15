import random as rd
class Forca():

    def __init__(self):

        self.iniciaJogo()

    def iniciaJogo(self):

        self.chances = 6

        self.letrasErradas = []

        self.letrasCorretas = []

        with open('palavras.txt', 'r') as arquivo:
            self.palavra = rd.choices(arquivo.read().split('\n'))[0]
            self.palavra = [x for x in self.palavra]

        self.palavraJogador = ['_' for x in range(len(self.palavra))]

        print("\n>>>>>>>>>>Hangman<<<<<<<<<<\n")

        self.forcaController()

    def forcaController(self):

        self.desenhaForca()

        self.desenhaPalavra()

        self.desenhaErros()

        self.desenhaAcertos()

        if self.ganhou() or self.perdeu():
            self.acabaJogo()
        else:
            self.pedeLetra()

    def desenhaForca(self):

        if self.chances == 6:
            print('''
            +---+
            |   |
                |
                |
                |
                |
            =========''')
        elif self.chances == 5:
            print('''
            +---+
            |   |
            O   |
                |
                |
                |
            =========''')
        elif self.chances == 4:
            print('''
            +---+
            |   |
            O   |
            |   |
                |
                |
            =========''')
        elif self.chances == 3:
            print('''
             +---+
             |   |
             O   |
            /|   |
                 |
                 |
            ==========''')
        elif self.chances == 2:
            print('''
             +---+
             |   |
             O   |
            /|\  |
                 |
                 |
            ==========''')
        elif self.chances == 1:
            print('''
             +---+
             |   |
             O   |
            /|\  |
            /    |
                 |
            ==========''')
        else:
            print('''
             +---+
             |   |
             O   |
            /|\  |
            / \  |
                 |
            ==========''')

    def desenhaPalavra(self):

        print("\nPalavra: ", end="")

        for letraJogador in self.palavraJogador:
            print(letraJogador, end="")

        print("\n\n")

    def desenhaErros(self):

        print("\nLetras erradas:")

        for letraErrada in self.letrasErradas:
            print(letraErrada)

        print("\n")

    def desenhaAcertos(self):

        print("\nLetras corretas:")

        for letraCorreta in self.letrasCorretas:
            print(letraCorreta)

        print("\n")

    def pedeLetra(self):

        letraJogador = input("Digite uma letra: ")

        if letraJogador in self.palavra:
            self.letrasCorretas.append(letraJogador)
            for index, letra in enumerate(self.palavra):
                if letra == letraJogador:
                    self.palavraJogador[index] = letra
        else:
            self.letrasErradas.append(letraJogador)
            self.chances = self.chances - 1

        self.forcaController()

    def ganhou(self):

        if self.palavra == self.palavraJogador:
            print("\nParabéns! Você venceu!!\n")
            return True
        else:
            return False

    def perdeu(self):

        if self.chances == 0:
            print("\nGame over! Você perdeu.\n")
            return True
        else:
            return False

    def acabaJogo(self):

        print("\nFoi bom jogar com você! Agora vá estudar!\n")

forca = Forca()