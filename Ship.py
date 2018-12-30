from random import randint
from Board import *

class Ship(object):
    __bottom_row = 0
    __bottom_col = 0

    def __init__(self, size, orientation, mark, name):
        self.__size = size
        self.__orientation = orientation
        self.__mark = mark              # define a letra que sera usada para marcar o navio no tabuleiro
        self.__name = name
        self.__life = size
        self.definePosition()

    def definePosition(self):
        # se a orientacao eh horizontal, entao a 1st posicao do navio na coluna, deve ser sizeBoard-sizeNavio+1
        boardGame = Board("ship")
        if self.__orientation == 'h':
            self.__bottom_row = randint(1, boardGame.size)
            self.__bottom_col = randint(1, boardGame.size-self.__size+1)
        # se a orientacao eh vertical, entao a 1st posicao do navio na linha, deve ser sizeBoard-sizeNavio+1
        elif self.__orientation == 'v':
            self.__bottom_row = randint(1, boardGame.size-self.__size+1)
            self.__bottom_col = randint(1, boardGame.size)

    def hitTaken(self):
        self.__life -= 1

    ###   Metodos Get   ###
    @property
    def row(self):
        return self.__bottom_row

    @property
    def col(self):
        return self.__bottom_col

    @property
    def mark(self):
        return self.__mark

    @property
    def orientation(self):
        return self.__orientation

    @property
    def size(self):
        return self.__size

    @property
    def name(self):
        return self.__name

    @property
    def getLife(self):
        return self.__life
