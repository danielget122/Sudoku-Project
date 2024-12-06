import pygame, sys
from constants import *
# pygame.font.init()
from sudoku_generator import *
from Board import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def draw_game_starts(screen):
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 50)
    screen.fill(BG_COLOR)
    title_surface = start_title_font.render("Welcome to Sudoku", 0, LINE_COLOR)
    title_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)
    game_mode_surface = start_title_font.render("Select Game Mode:", 0, LINE_COLOR)
    game_mode_rectangle = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 4 - 150))
    screen.blit(game_mode_surface, game_mode_rectangle)

    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))
    # initialize button's background color and text

    easy_text_surface = pygame.Surface((easy_text.get_size()[0] + 20, easy_text.get_size()[1] + 20))
    easy_text_surface.fill(LINE_COLOR)
    easy_text_surface.blit(easy_text, (10, 10))
    easy_text_rectangle = easy_text_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2 + 200))
    screen.blit(easy_text_surface, easy_text_rectangle)
    medium_text_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_text_surface.fill(LINE_COLOR)
    medium_text_surface.blit(medium_text, (10, 10))
    medium_text_rectangle = medium_text_surface.get_rect(center=(WIDTH // 2 - 10, HEIGHT // 2 + 200))
    screen.blit(medium_text_surface, medium_text_rectangle)
    hard_text_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_text_surface.fill(LINE_COLOR)
    hard_text_surface.blit(hard_text, (10, 10))
    hard_text_rectangle = hard_text_surface.get_rect(center=(WIDTH // 2 + 200, HEIGHT // 2 + 200))
    screen.blit(hard_text_surface, hard_text_rectangle)
    pygame.display.flip()


def draw_game_over(screen):
    button_font = pygame.font.Font(None, 50)
    screen.fill(BG_COLOR)
    game_over_font = pygame.font.Font(None, 100)
    game_over_surface = game_over_font.render("Game Over :(", 0, LINE_COLOR)
    game_over_rectangle = game_over_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(game_over_surface, game_over_rectangle)
    pygame.display.flip()

    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    restart_text_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_text_surface.fill(LINE_COLOR)
    restart_text_surface.blit(restart_text, (10, 10))
    restart_text_rectangle = restart_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(restart_text_surface, restart_text_rectangle)
    pygame.display.flip()


# draw_game_over(screen)
def game_won(screen):
    button_font = pygame.font.Font(None, 50)
    screen.fill(BG_COLOR)
    game_won_font = pygame.font.Font(None, 100)
    game_won_surface = game_won_font.render("Game Won!", 0, LINE_COLOR)
    game_won_rectangle = game_won_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 200))
    screen.blit(game_won_surface, game_won_rectangle)
    pygame.display.flip()

    exit_text_button = button_font.render("Exit", 0, (255, 255, 255))
    exit_text_surface = pygame.Surface((exit_text_button.get_size()[0] + 20, exit_text_button.get_size()[1] + 20))
    exit_text_surface.fill(LINE_COLOR)
    exit_text_surface.blit(exit_text_button, (10, 10))
    exit_text_rectangle = exit_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(exit_text_surface, exit_text_rectangle)


# game_won(screen)

easy_text_rectangle, medium_text_rectangle, hard_text_rectangle = draw_game_starts(screen)
draw_game_starts(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if easy_text_rectangle.collidepoint(event.pos):
            # print("Easy")
            elif medium_text_rectangle.collidepoint(event.pos):
            # print("Medium")
            elif hard_text_rectangle.collidepoint(event.pos):
        # print("Hard")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y=event.pos
                print((x//100,y//100))

        pygame.display.update()

