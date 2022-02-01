# loader.py
import pygame


class Colour:
    white = (255, 255, 255)
    light_grey = (100, 100, 100)
    grey = (30, 30, 30)
    dark_grey = (15, 15, 15)
    black = (0, 0, 0)

    brown = (205, 175, 125)
    beige = (255, 225, 200)

    blue = (50, 50, 225)
    cyan = (50, 200, 200)

    red = (225, 50, 50)
    yellow = (225, 225, 50)


class Button:
    def __init__(self, x, y, button_width, button_height, colour1, colour2, text=""):
        self.colour = Colour()
        self.x = x
        self.y = y
        self.width = button_width
        self.height = button_height
        self.text = text
        self.colour1 = colour1
        self.colour2 = colour2
        self.border_width = 2

    def drawButton(self, screen, font):
        pygame.draw.rect(screen, self.colour1, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.colour2, (self.x, self.y, self.width, self.height), self.border_width)

        text = font.render(self.text, True, self.colour.black)
        screen.blit(text, (self.x + self.width / 16, self.y + self.height / 4))

    def mouseOn(self, mouse_pos):
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        if self.x < mouse_x < self.x + self.width:
            if self.y < mouse_y < self.y + self.height:
                self.colour1 = self.colour2
                self.border_width = 3
                return True
        return False


class Cell:
    def __init__(self, x, y, button_width, buffer, colour1, colour2, colour3):
        self.colour = Colour()
        self.x = x
        self.y = y
        self.width = button_width
        self.radius = self.width / 2
        self.buffer = buffer
        self.colour1 = colour1  # White
        self.colour2 = colour2  # Red
        self.colour3 = colour3  # Yellow
        self.border_width = 2

    def drawCell(self, screen):
        pygame.draw.circle(screen, self.colour1, (self.x * self.width + self.buffer,
                                                  self.y * self.width + self.buffer), self.width / 4)

    def mouseOn(self, mouse_pos):
        mouse_x = mouse_pos[0]
        mouse_y = mouse_pos[1]

        if self.x - self.radius < mouse_x < self.x + self.radius:
            if self.y - self.radius < mouse_y < self.y + self.radius:
                self.colour1 = self.colour2
                self.border_width = 3
                return True
        return False