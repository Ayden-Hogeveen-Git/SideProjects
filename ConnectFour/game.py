# game.py
from loader import Colour
import pygame
pygame.init()


# --- Window Variables --- #
width, height = 960, 720
screen = pygame.display.set_mode((width, height))
caption = "Connect 4"
pygame.display.set_caption(caption)

colour = Colour()


class Game:
    def __init__(self):
        self.running = True

        self.scene = 1

    def draw_scenes(self):
        if self.scene == 1:
            screen.fill(colour.white)

        elif self.scene == 2:
            screen.fill(colour.grey)
        else:
            screen.fill(colour.black)
        pygame.display.update()

    def run(self):
        while self.running:
            self.draw_scenes()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_RETURN:
                        self.scene += 1
