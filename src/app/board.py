from random import choice
from typing import *

ALIVE= 1
DEAD= 0

class Board:
    def __init__(self, width: int= None, height: int= None, file:TextIO= None)-> None:
        self.width = width 
        self.height = height 
        self.file = file 
        self.state = None
        if not self.file and not (self.width and  self.height ): raise TypeError("Board can not initialize without width and hight or from a file")
    
    def fill_to_alive(self)-> None:
        self.state = [ [ALIVE for _ in range(self.width)] for _ in range(self.height)]
    
    def fill_to_dead(self)-> None:
        self.state = [ [DEAD for _ in range(self.width)] for _ in range(self.height)]
    
    def fill_random(self)-> None: 
        self.state = [ [choice([ALIVE , DEAD]) for _ in range(self.width)] for _ in range(self.height)]
        
