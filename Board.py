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
        print("\n")

    def setMark_on_board(self, row, col, mark):
        self.tabuleiro[row][col] = mark

    def eraseMark(self, mark):
        for posX in range(1,self.size):
            for posY in range(1,self.size):
                if self.tabuleiro[posX-1][posY-1] == mark:
                    self.setMark_on_board(posX-1, posY-1, "_")