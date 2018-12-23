class Board(object):
    size = 10
    tabuleiro = []

    def __init__(self, nome):
        self.nome = nome
        #self.defineBoard()

    def getSize(self):
        return self.size

    def defineBoard(self):
        for n in range(self.size):
            self.tabuleiro.append(['_'] * self.size)

    def printBoard(self):
        for row in self.tabuleiro:
            print("\t", " ".join(row))

    def set_mark_on_board(self, row, col, mark):
        self.tabuleiro[row][col] = mark

    def eraseMark(self, mark):
        for posX in range(1,self.size):
            for posY in range(1,self.size):
                if self.tabuleiro[posX][posY] == mark:
                    self.set_mark_on_board(posX, posY, "_")