# backtrackingMazeGenerator.py
"""
title: Maze Generator with recursive backtracking
author: Ayden Hogeveen
date-created: 2021-10-1

Recursive Back Tracker Algorithm:
1. Make the initial cell the current cell and mark it as visited
2. While there are unvisited cells:
    a. If the current cell has any neighbours which have not been visited:
        i. Choose randomly one of the unvisited neighbours
        ii. Push the current cell to the stack
        iii. Remove the wall between the current and chosen cell
            - Will have to remove 2 walls, the one in the current cell, and then the opposite
            (touching) one in the chosen cell
    b. else if the stack is not empty:
        i. Pop a cell from the stack
        ii. Make it the current cell
"""
import random
import pygame
pygame.init()

# Display and Screen Variables
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
caption = "Maze Generator"
pygame.display.set_caption(caption)

clock = pygame.time.Clock()
fps = 120

# Global main variables
cell_amount = 10


class Colour:
    white = (255, 255, 255)
    grey = (35, 35, 35)
    black = (0, 0, 0)

    line_colour = (255, 255, 0)
    snake_colour = (25, 160, 225)


class Board:
    def __init__(self):
        self.dimension = width // cell_amount
        self.row_num = self.col_num = width // self.dimension

        self.grid = []
        self.stack = []

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
        self.cell_width = self.board.dimension
        self.line_colour = self.colour.line_colour
        self.line_width = 1

        # Boolean for whether or not the cell has been visited
        self.visited = False

        # Booleans for the existence of the top, right, bottom and left walls of the cells
        self.walls = [True, True, True, True]

    def highlight(self):
        """
        Highlights the current cell
        """
        x = self.row * self.cell_width
        y = self.col * self.cell_width

        head = pygame.Surface((self.cell_width, self.cell_width))
        head.set_alpha(225)
        head.fill(self.colour.snake_colour)

        screen.blit(head, (x, y))

    def drawCell(self):
        """
        Draws the individual walls of each cell
        """
        x = self.row * self.cell_width
        y = self.col * self.cell_width

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

        # Change the colour of the cell if it has been visited
        if self.visited:
            visited_square = pygame.Surface((self.cell_width, self.cell_width))
            visited_square.set_alpha(200)
            visited_square.fill(self.colour.snake_colour)

            screen.blit(visited_square, (self.row * self.cell_width, self.col * self.cell_width))

    def checkNeighbours(self):
        """
        Checks the surrounding cells, if they have not been visited, append them to the array
        There is one issue in this, it doesn't really snake around, going to the cell beside it

        Issue -- List index out of range
        - need to check if the index is in the array of squares in the board
        """
        neighbours = []

        top = self.board.grid[self.row - 1][self.col]
        right = self.board.grid[self.row][self.col - 1]
        bottom = self.board.grid[self.row + 1][self.col]
        left = self.board.grid[self.row][self.col + 1]

        # If the current cell has a cell on top, right, bottom, or on the left
        if top and not top.visited:
            neighbours.append(top)
        if right and not right.visited:
            neighbours.append(right)
        if bottom and not bottom.visited:
            neighbours.append(bottom)
        if left and not left.visited:
            neighbours.append(left)

        # If the current cell has neighbours
        if len(neighbours) != 0:
            random_cell = random.randrange(0, len(neighbours))
            return neighbours[random_cell]
        else:
            return None


class Main:
    def __init__(self):
        self.running = True
        self.board = Board()

        self.current_cell = None
        self.next_cell = None

    def createCells(self):
        """
        Creates however many cells, and appends them to a 2D list
        """
        self.board.createBoardList()

        for x in range(self.board.row_num):
            for y in range(self.board.col_num):
                cell = Cell(y, x)
                self.board.grid[x][y] = cell

    @staticmethod
    def removeWalls(w1, w2):
        """
        Finds the walls that need to be removed, based on the index of cell 1 and 2
        """
        x = w1.row - w2.row
        y = w1.col - w2.col

        if x == 1:
            w1.walls[3] = False
            w2.walls[1] = False
        elif x == -1:
            w1.walls[1] = False
            w2.walls[3] = False

        if y == 1:
            w1.walls[0] = False
            w2.walls[2] = False
        elif y == -1:
            w1.walls[2] = False
            w2.walls[0] = False

    def draw(self):
        for row in range(self.board.row_num):
            for col in range(self.board.col_num):
                self.board.grid[row][col].drawCell()

        self.current_cell.visited = True
        self.current_cell.highlight()

        # STEP 1
        self.next_cell = self.current_cell.checkNeighbours()

        if self.next_cell:
            self.next_cell.visited = True

            # STEP 2
            # self.board.stack.append(self.current_cell)

            # STEP 3
            self.removeWalls(self.current_cell, self.next_cell)

            # STEP 4
            self.current_cell = self.next_cell

        elif len(self.board.stack) > 0:
            self.current_cell = self.board.stack.pop()

    def run(self):
        screen.fill(Colour.grey)

        self.createCells()
        self.current_cell = self.board.grid[0][0]

        while self.running:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            pygame.display.update()
            clock.tick(fps)


if __name__ == '__main__':
    main = Main()
    main.run()
    pygame.quit()
    quit()
