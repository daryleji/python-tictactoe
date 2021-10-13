import pygame
import sys

pygame.init()
display_width = 600
display_height = 600
BG_COLOR = (28, 170, 156)
window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('TIC TAC TOE')


def draw_lines():
    line_color = (23, 145, 135)
    line_width = 15

    # First horizontal line
    pygame.draw.line(window, line_color, (0, 200), (600, 200), line_width)
    pygame.draw.line(window, line_color, (0, 400), (600, 400), line_width)
    pygame.draw.line(window, line_color, (200, 0), (200, 600), line_width)
    pygame.draw.line(window, line_color, (400, 0), (400, 600), line_width)


def main():
    while True:
        window.fill(BG_COLOR)
        draw_lines()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.update()


if __name__ == '__main__':
    main()
