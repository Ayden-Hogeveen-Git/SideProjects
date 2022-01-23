# main.py
"""
title: Connect Four AI
author: Ayden Hogeveen
date-created: 2022-01-23
"""
import pygame
from game import Game


if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
    quit()
