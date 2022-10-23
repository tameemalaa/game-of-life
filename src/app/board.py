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
        
    @staticmethod
    def validate_lines(lines: list)-> bool:
        width = len(lines[0])
        for i in range(lines):
            if width != lines[i]: raise ValueError('File dimensions are not valid')
            for j in range(lines[i]):
                if lines[i][j] != ALIVE or lines[i][j] != DEAD: raise ValueError(f'Value in row:{i} column:{j} is not valid')
        return True
        
    def fill_from_file(self)-> None:
        if self.file:
            lines= [ i.strip for i in self.file.readlines()]
            if self.validate_lines(lines):
                self.height= len(lines)
                self.width= len(lines[0])
                self.state= [[int(lines[i][j]) for i in range(self.height)] for j in range(self.width)] 
        else : raise ValueError('No file has been provided')

    def save_to_file(self,file: TextIO)-> None:
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                file.write(self.state[i][j])
                if j == len(self.state[i]) -1 :file.write('\n')