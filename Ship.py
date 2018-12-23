from random import randint
from Board import *

class Ship(object):
    bottom_row = 0
    bottom_col = 0

    def __init__(self, size, orientation, mark, name):
        self.size = size
        self.orientat = orientation
        self.mark = mark                # define a letra que sera usada para marcar o navio no tabuleiro
        self.name = name
        self.life = size
        self.definePosition()

    def definePosition(self):
        # se a orientacao eh horizontal, entao a 1st posicao do navio na coluna, deve ser boardLength-self.size+1
        boardGame = Board("ship")
        if self.orientat == 'h':
            self.bottom_row = randint(1, boardGame.getSize())
            self.bottom_col = randint(1, boardGame.getSize()-self.size+1)
        # se a orientacao eh vertical, entao a 1st posicao do navio na linha, deve ser boardLength-self.size+1
        elif self.orientat == 'v':
            self.bottom_row = randint(1, boardGame.getSize()-self.size+1)
            self.bottom_col = randint(1, boardGame.getSize())

    def hitTaken(self):
        self.life -= 1;

    ###   Metodos Get   ###
    def getRow(self):
        return self.bottom_row

    def getCol(self):
        return self.bottom_col

    def getMark(self):
        return self.mark

    def getOrientation(self):
        return self.orientat

    def getSize(self):
        return self.size

    def getName(self):
        return self.name

    def getLife(self):
        return self.life