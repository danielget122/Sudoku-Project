import pygame
from constants import *
from Cell import *
pygame.init()

class Board:
    def __init__(self,width,height, screen, difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        self.board =[["-" for i in range(9)] for j in range(9)]
        self.grid=[[Cell(self.board[i][j],i,j,self.screen) for j in range(BOARD_COLS)] for i in range(BOARD_ROWS)]
        self.selected_row=None
        self.selected_col=None
    def draw(self):
        self.screen.fill(BG_COLOR)
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * SQUARE_SIZE),
                (WIDTH, i * SQUARE_SIZE),
                LINE_WIDTH
            )
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * SQUARE_SIZE, 0),
                (i * SQUARE_SIZE, HEIGHT),
                LINE_WIDTH
            )
        for i in range(1, BOARD_ROWS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i * CELL_SIZE),
                (WIDTH, i * CELL_SIZE),
                LINE_CELLS_WIDTH
            )
        for i in range(1, BOARD_COLS):
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * CELL_SIZE, 0),
                (i * CELL_SIZE, HEIGHT),
                LINE_CELLS_WIDTH
            )
        if self.selected_row is not None:
            x=self.selected_col*CELL_SIZE
            y=self.selected_row*CELL_SIZE
            pygame.draw.rect(self.screen,SELECTED_CELL_COLOR,(x,y,CELL_SIZE,CELL_SIZE))
        #if self.board[row][col] != "-":

    def select(self,row,col):
        self.selected_row=row
        self.selected_col=col

    def click(self,row,col):
        if 0<=row<9 and 0<=col<9:
            return ((row//100,col//100))
        else:
            return None
    def clear(self,value):
        pass
    def sketch(self,value):
        pass
    def place_number(self):
        pass
    def reset_to_original(self):
        pass
    def is_full(self):
        pass
    def update_board(self):
        self.grid=[[Cell(self.board[i][j],i,j,self.screen) for j in range(BOARD_COLS)] for i in range(BOARD_ROWS)]
    def find_empty(self):
        pass
    def check_board(self):
        pass

board = Board(WIDTH,HEIGHT,screen,difficulty=0)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print((x // 100, y // 100))

    screen.fill(BG_COLOR)
    board.draw()
    board.select()
    pygame.display.flip()