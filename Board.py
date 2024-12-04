import pygame


from constants import *
from Cell import *
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
class Board:
    def __init__(self,width,height, screen, difficulty):
        self.width=width
        self.height=height
        self.screen=screen
        self.difficulty=difficulty
        self.board =[[0 for i in range(9)] for j in range(9)] #logical representation of the sudoku grid
        self.grid=[[Cell(self.board[i][j],i,j,self.screen) for j in range(BOARD_COLS)] for i in range(BOARD_ROWS)] #iterstion of each individual cell. 2D list of objectes of type cell
        self.selected_row=None
        self.selected_col=None
        self.original_board=[[0 for i in range(9)] for j in range(9)]

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
            pygame.draw.rect(self.screen,RED,(x,y,CELL_SIZE,CELL_SIZE))
        #if self.board[row][col] != "-":

    def select(self,row,col):
        self.selected_row=row
        self.selected_col=col

    def click(self,row,col):
        if 0<=row<9 and 0<=col<9:
            return ((row//100,col//100))
        else:
            return None
    def available_square(self, row, col): #new function (NOT REQUIRED)
        return self.board[row][col] == 0
    def clear(self,value):
        if self.selected_row is None or self.selected_row is None:
            return
        else:
            current_cell=self.grid[self.selected_row][self.selected_col] #object of type Cell
            if self.board[self.selected_row][self.selected_col] != 0: #if the cell is using 0 as place holder means that it can be edited otherwise, the cell cannot be edited
                return
            else:
                current_cell.value=0
                current_cell.sketched_value=0
    def sketch(self,value):
        if self.selected_row is None or self.selected_col is None:
            return
        if self.board[self.selected_row][self.selected_col] != 0: #if the cell is using 0 as place holder means that it can be edited otherwise, the cell cannot be edited
            return
        current_cell = self.grid[self.selected_row][self.selected_col]
        if value not in [1,2,3,4,5,6,7,8,9]:
            return
        current_cell = self.grid[self.selected_row][self.selected_col]
        current_cell.sketched_value=value
    def place_number(self):

        if self.selected_row is None or self.selected_col is None:
            return
        current_cell = self.grid[self.selected_row][self.selected_col]
        if self.board[self.selected_row][self.selected_col] != 0: #if the cell is using 0 as place holder means that it can be edited otherwise, the cell cannot be edited
            return
        value = current_cell.sketched_value
        if value not in [1,2,3,4,5,6,7,8,9]:
            return
        current_cell.value=value #Sets the value of the current selected cell equal to the user entered value
        self.board[self.selected_row][self.selected_col]=value
        current_cell.sketched_value=0

    def reset_to_original(self):
        for i in range(9): #i's are the rows of the 2D list
            for j in range(9):#eaach cell object (columns)
                self.original_board[i][j]=self.board

    def is_full(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False
        return True
    def update_board(self):
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.board[i][j]=self.grid[i][j].value
    def find_empty(self):
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                if self.board[i][j]==0:
                    return(i,j)
        return False
    def check_board(self):
        pass

# board = Board(WIDTH,HEIGHT,screen,difficulty=0)
# #board.select()
# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             sys.exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             x, y = event.pos
#             print((x // 100, y // 100))
#
#     screen.fill(BG_COLOR)
#     board.draw()
#
#     pygame.display.flip()