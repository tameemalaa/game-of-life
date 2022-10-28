from tkinter import *
from tkinter import filedialog
from src.app.game import Game, Settings

BUTTON_BOARDER_WIDTH = 0
BIG_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
FONT_FAMILY = 'Arial'
BACKGROUND_COLOR = '#001d3d'
BUTTON_COLOR = '#003566'
FONT_COLOR = '#ffc300'
ALIVE_COLOR = '#ffd60a'
DEAD_COLOR = '#000814'
WINDOW_TITLE = 'Game Of Life'
WINDOW_SIZE = "500x500"

class View():
    def __init__(self):
        self.starting_mode = None
        
    def initialize_base_screen(self):
        self.current_screen = Tk()
        self.current_screen.title(WINDOW_TITLE)
        self.current_screen.geometry(WINDOW_SIZE)
        self.current_screen.resizable(False,False)
        self.current_screen.configure(bg =BACKGROUND_COLOR)
        
    def initialize_welcome_screen(self) -> None:
        self.initialize_base_screen()
        next_screen = IntVar(self.current_screen, 1)
        Radiobutton(self.current_screen, text = "Import File", variable = next_screen,value = 1,width = 8, height = 1, bg = BUTTON_COLOR, fg = FONT_COLOR, borderwidth = BUTTON_BOARDER_WIDTH,
        font=(FONT_FAMILY,SMALL_FONT_SIZE), activebackground = FONT_COLOR).place(relx = 0.25, rely = 0.6, anchor = CENTER)
        Radiobutton(self.current_screen, text = "Create Radom Grid" , variable = next_screen,value = 0,width = 15, height = 1, bg = BUTTON_COLOR, fg = FONT_COLOR, borderwidth = BUTTON_BOARDER_WIDTH,
        font=(FONT_FAMILY,SMALL_FONT_SIZE), activebackground = FONT_COLOR).place(relx = 0.7, rely = 0.6, anchor = CENTER)
        new_game_button = Button(self.current_screen, text = 'New Game', width = 20, height = 1, bg = BUTTON_COLOR, fg = FONT_COLOR, borderwidth = BUTTON_BOARDER_WIDTH,
        font=(FONT_FAMILY,BIG_FONT_SIZE), activebackground = FONT_COLOR, command = lambda : self.choose_second_screen(next_screen.get())).place(relx = 0.5, rely = 0.4, anchor = CENTER)
        self.current_screen.mainloop()
        
    def choose_second_screen(self,next_screen: bool) -> None:
        self.current_screen.destroy()
        self.starting_mode = next_screen
        if next_screen: self.initialize_load_file_screen()
        else: self.initialize_create_game_screen()
        
    def initialize_load_file_screen(self) -> None:
        pass
        
    def initialize_create_game_screen(self) -> None:
        pass