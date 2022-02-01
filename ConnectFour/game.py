# game.py
from loader import Colour, Button, Cell
import pygame
pygame.init()


# --- Window Variables --- #
width, height = 960, 720
screen = pygame.display.set_mode((width, height))
caption = "Connect 4"
pygame.display.set_caption(caption)


colour = Colour()
font = pygame.font.Font("ConnectAssets/LandasansMedium-ALJ6m.otf", 32)


class Board:
    def __init__(self):
        self.dimensionX = 8
        self.dimensionY = 6

        self.circle_width = width / self.dimensionX
        self.buffer = width / 16

        self.cells = [
            [],
            [],
            [],
            [],
            [],
            []
        ]

        self.game_state = [
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""]
        ]

    def drawBoard(self):
        for y in range(self.dimensionY):
            for x in range(self.dimensionX):
                self.cells[y].append(Cell(x, y, self.circle_width, width // 16, colour.white, colour.red, colour.yellow))
                self.cells[y][x].drawCell(screen)

    def check(self, mouse_pos):
        for y in range(self.dimensionY):
            for x in range(self.dimensionX):
                if self.cells[y][x].mouseOn(mouse_pos):
                    print(f"ON {y} {x}")



class Game:
    def __init__(self):
        self.running = True
        self.scene = 1

        self.playButton = Button(width / 2 - width / 16, height / 2 - height / 32, width / 8, height / 16,
                                 colour.cyan, colour.blue, "Play Game")

        self.board = Board()

    def draw_scenes(self, mouse_pos):
        if self.scene == 1:
            screen.fill(colour.white)
            self.playButton.drawButton(screen, font)

        elif self.scene == 2:
            screen.fill(colour.grey)

            self.board.drawBoard()
            self.board.check(mouse_pos)

        else:
            screen.fill(colour.black)
        pygame.display.update()

    def run(self):
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            self.draw_scenes(mouse_pos)

            for event in pygame.event.get():
                # --- General Window --- #
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                # --- Scene 1 --- #
                if self.playButton.mouseOn(mouse_pos):
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.playButton.mouseOn(mouse_pos):
                        self.scene += 1
                # --- Scene 2 --- #

