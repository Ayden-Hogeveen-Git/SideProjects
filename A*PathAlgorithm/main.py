# main.py
"""
title: A* Pathfinding Algorithm
author: Ayden Hogeveen
date-created: 2022-01-21
"""
import pygame
pygame.init()

# Display and Screen Variables
width, height = 1000, 800
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
caption = "Pathfinding Ai"
pygame.display.set_caption(caption)

clock = pygame.time.Clock()
fps = 120

amount_cellsX = 20
amount_cellsY = 16


class Colour:
    white = (255, 255, 255)
    grey = (35, 35, 35)
    dark_grey = (20, 20, 20)
    black = (0, 0, 0)

    line_colour = (50, 255, 50)
    cell_colour = (15, 200, 255)
    highlight_colour = (40, 60, 185)


class Board:
    def __init__(self):
        self.dimensionX = width // amount_cellsX
        self.dimensionY = height // amount_cellsY
        self.col_num = width // self.dimensionX
        self.row_num = height // self.dimensionY

        self.grid = []

    def createBoardList(self):
        for row in range(self.row_num):
            self.grid.append([])
            for col in range(self.col_num):
                self.grid[row].append("")


class Cell:
    def __init__(self, col, row):
        self.board = Board()
        self.colour = Colour()

        self.col = col
        self.row = row
        self.cell_width = self.board.dimensionX
        self.line_colour = self.colour.line_colour
        self.line_width = 1

        # Booleans for the existence of the top, right, bottom and left walls of the cells
        self.walls = [True, True, True, True]

    def mouseOn(self, mouse_pos):
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        if self.col < mouse_x < self.col + self.cell_width:
            if self.row < mouse_y < self.row + self.cell_width:
                print("pressed")
                return True
        return False

    def highlight(self):
        """
        Highlights the current cell
        """
        x = self.row * self.cell_width
        y = self.col * self.cell_width

        head = pygame.Surface((self.cell_width, self.cell_width))
        head.set_alpha(225)
        head.fill(self.colour.highlight_colour)

        screen.blit(head, (x, y))

    def drawCell(self):
        """
        Draws the individual walls of each cell
        """
        x = self.row * self.cell_width
        y = self.col * self.cell_width

        pygame.draw.rect(screen, Colour.cell_colour, (x, y, self.cell_width, self.cell_width), 2)

        # Might use this later...
        """ 
        # Top of cell
        if self.walls[0]:
            pygame.draw.line(screen, self.line_colour, (x, y), (x + self.cell_width, y), self.line_width)

        # Right of cell
        if self.walls[1]:
            pygame.draw.line(screen, self.line_colour, (x + self.cell_width, y),
                             (x + self.cell_width, y + self.cell_width), self.line_width)
        # Bottom of cell
        if self.walls[2]:
            pygame.draw.line(screen, self.line_colour, (x, y + self.cell_width),
                             (x + self.cell_width, y + self.cell_width), self.line_width)
        # Left of cell
        if self.walls[3]:
            pygame.draw.line(screen, self.line_colour, (x, y), (x, y + self.cell_width), self.line_width)
        """


class Main:
    def __init__(self):
        self.running = True
        self.board = Board()

    def createCells(self):
        self.board.createBoardList()

        for x in range(amount_cellsY):
            for y in range(amount_cellsX):
                cell = Cell(x, y)
                self.board.grid[x][y] = cell

    def draw(self):
        for row in range(self.board.row_num):
            for col in range(self.board.col_num):
                self.board.grid[row][col].drawCell()

    def run(self):
        screen.fill(Colour.dark_grey)
        self.createCells()

        while self.running:
            self.draw()
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for x in range(amount_cellsY):
                        for y in range(amount_cellsX):
                            if self.board.grid[x][y].mouseOn(mouse_pos):
                                print("pressed")

            pygame.display.update()
            clock.tick(fps)


if __name__ == '__main__':
    main = Main()
    main.run()
    pygame.quit()
    quit()
