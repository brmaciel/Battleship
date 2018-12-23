from random import randint
from Board import *

class Ship(object):
    bottom_row = 0
    bottom_col = 0

    def __init__(self, size, orientation, mark):
        self.size = size
        self.orientat = orientation
        self.mark = mark                # define a letra que sera usada para marcar o navio no tabuleiro

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

    def getOrientation(self):
        return self.orientat

    def getSize(self):
        return self.size