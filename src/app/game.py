from typing import *
from board import Board
from pydantic import BaseModel 
import os
import time


class Settings(BaseModel):
    from_file: bool
    file : Optional[str]
    width: Optional[int]
    height: Optional[int]
    ending_round: float
    
    
class Game:
    def __init__(self, settings: Settings)-> None:
        if settings.from_file:
            with open(settings.file) as file:
                self.board =Board(file = file)
                self.board.fill_from_file()
        else : 
            self.board = Board(width=settings.width, height=settings.height)
            self.board.fill_random()
        self.current_round = 0
        self.ending_round = settings.ending_round
    
    def update_state(self):
        self.board.update_state()
        
    def start(self)-> None:
        first_round_flag = True
        while self.ending_round:
            time.sleep(0.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            self.ending_round-=1
            if first_round_flag:
                first_round_flag = False
                print(self)
                continue
            self.update_state()
            print(self)
    
    def __str__(self)-> str:
        return self.board.__str__()
    
    def __repr__(self)-> str:
        return self.board.__repr__()