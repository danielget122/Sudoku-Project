import pygame, sys
from sudoku import *
from constants import*
from Board import *
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill(BG_COLOR)
class Cell:
    def __init__(self,value,row,col,screen):
        self.value = value
        self.row=row
        self.col=col
        self.screen=screen
        self.sketched_value=0
    def set_cell_value(self,value):
        self.value=value

    def set_sketched_values(self,value):
        self.sketched_value=value
    def draw(self):
        #draw cell rectangle(surface,color,position and size, thickness)
        pygame.draw.rect(self.screen, RED, (self.row*CELL_SIZE,self.row*CELL_SIZE, CELL_SIZE, CELL_SIZE),5)
        if self.sketched_value >0:
            number_font = pygame.font.Font(None, int(SKETCHED_FONT))
            num_surface = number_font.render(str(self.sketched_value), 0, SKETCHED_VALUE_COLOR)
            num_rect = num_surface.get_rect(center=(self.col*CELL_SIZE+CELL_SIZE/2, self.row*CELL_SIZE+CELL_SIZE/2))
            self.screen.blit(num_surface, num_rect)
        elif self.value>0:
            number_font = pygame.font.Font(None, int(NUMBER_FONT))
            num_surface = number_font.render(str(self.value), 0, NUMBER_COLOR)
            num_rect = num_surface.get_rect(
                center=(self.col * CELL_SIZE + CELL_SIZE / 2, self.row * CELL_SIZE + CELL_SIZE / 2))
            self.screen.blit(num_surface, num_rect)
# numb1=Cell(5,1,1,screen)
# numb1.draw()
# numb1.set_cell_value(3)
# while True:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             sys.exit()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             numb1.set_cell_value(5)
#     screen.fill(BG_COLOR)
#     numb1.draw()
#     pygame.display.flip()