from random import choice
from typing import *
from copy import deepcopy

ALIVE= 1
DEAD= 0
ALIVE_UTF8= u"\u2588" 
DEAD_UTF8 = u"\u0020" 

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
        for i in range(len(lines)):
            if width != len(lines[i]): raise ValueError('File dimensions are not valid')
            for j in range(len(lines[i])):
                if int(lines[i][j]) != ALIVE and int(lines[i][j]) != DEAD: raise ValueError(f'Value in row:{i} column:{j} is not valid')
        return True
        
    def fill_from_file(self)-> None:
        if self.file:
            lines= [ i.strip() for i in self.file.readlines()]
            if self.validate_lines(lines):
                self.height= len(lines)
                self.width= len(lines[0])
                self.state= [[int(lines[i][j]) for j in range(self.width)] for i in range(self.height)] 
        else : raise ValueError('No file has been provided')

    def save_to_file(self,file: TextIO)-> None:
        for i in range(len(self.state)):
            for j in range(len(self.state[i])):
                file.write(self.state[i][j])
                if j == len(self.state[i]) -1 :file.write('\n')

    def update_state(self)-> None:
            new_state = deepcopy(self.state)
            for i in range(len(new_state)):
                for j in range(len(new_state[i])):
                    neighbors = -self.state[i][j] 
                    for x in range(i-1,i+2):
                        for y in range(j-1,j+2):
                            if x >= 0 and y >= 0 and x < self.height and y < self.width :
                                neighbors += self.state[x][y] 
                    if self.state[i][j]:
                        if neighbors <= 1* ALIVE or neighbors > 3* ALIVE : new_state[i][j] = 0
                    else:
                        if neighbors == 3* ALIVE: new_state[i][j] = 1
            self.state = deepcopy(new_state)
            
    def __str__(self)-> str:
            to_print = ""
            for row in self.state:
                line = ""
                for i in row:
                    line+= ALIVE_UTF8 if i == ALIVE else DEAD_UTF8
                to_print += line + '\n'
            return to_print
        
    def __repr__(self)-> str:
            return self.state
        
    
