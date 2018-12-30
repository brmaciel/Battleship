class Board(object):
    __size = 10

    def __init__(self, nome):
        self.nome = nome
        self.__tabuleiro = []
        self.__defineBoard()

    def __defineBoard(self):
        for n in range(self.__size):
            self.__tabuleiro.append(['_'] * self.__size)

    def printBoard(self):
        for rows in self.__tabuleiro:
            print("\t", " ".join(rows))
        print("\n")

    def setMark_on_board(self, row, col, mark):
        self.__tabuleiro[row][col] = mark

    def eraseMark(self, mark):
        for posX in range(1, self.__size):
            for posY in range(1, self.__size):
                if self.__tabuleiro[posX - 1][posY - 1] == mark:
                    self.setMark_on_board(posX - 1, posY - 1, "_")

    ###    Metodos Get   ###
    @property
    def size(self):
        return self.__size

    def getBoardPosition(self, row, col):
        return self.__tabuleiro[row][col]
