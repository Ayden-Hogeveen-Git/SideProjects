# quickSort.py
"""
title: QuickSort Algorithm Visualized
author: Ayden Hogeveen
date-created: 2021-10-27

Quick Sort
Divide and Conquer Algorithms
- Finds a pivot element in the list, which divides the list into different parts
- Swaps values so that the values on one side of the list are greater than the pivot value
  and the values on the other side are lesser than the pivot

This algorithm uses recursion to bring the pivot to the proper position, so that the values on
either side are smaller and larger, respectively, then to quickSort both parts.
"""
import random
import pygame

# Window Variables
width, height = 960, 480
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
pygame.display.set_caption("Visual QuickSort Algorithm")


class Algorithm:
    """
    Handles the algorithm and values
    """

    def __init__(self):
        self.array = []

        # Value restrictions
        self.amount = 480

        self.min_value = 0
        self.max_value = self.amount + 1

        # Line Variables
        self.line_width = width // self.amount

    def createRandArray(self):
        for i in range(self.amount):
            self.array.append(random.randint(self.min_value, self.max_value))

    @staticmethod
    def swap(arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

    def partition(self, arr, start, end):
        """
        Returns the pivot value in the proper position
        """
        index = start - 1  # Index of smaller element
        pivot = arr[end]  # Pivot Value

        for i in range(start, end):
            if arr[i] <= pivot:
                # Increment the index and then use multiple assignment to swap the values
                index += 1
                self.swap(arr, index, i)

        self.swap(arr, index + 1, end)
        return index + 1

    def quickSort(self, arr, start, end):
        """
        Parameters:
        arr --> array to be sorted
        start --> starting index
        end --> ending index

        :return: sorted list
        """
        if len(arr) == 1:
            return arr

        if start < end:
            # pivot is partitioning index, array[pivot] is now at the right position
            pivot = self.partition(arr, start, end)

            # Sort before and after the pivot index
            self.quickSort(arr, start, pivot - 1)
            self.quickSort(arr, pivot + 1, end)


class Main:
    """
    Handles the visual part of the program
    """

    def __init__(self):
        self.running = True
        self.algorithm = Algorithm()

        # Colours
        self.white = (255, 255, 255)

        self.light_grey = (145, 145, 145)
        self.grey = (100, 100, 100)
        self.dark_grey = (40, 40, 40)

        self.black = (0, 0, 0)

    def drawLines(self):
        for i in range(self.algorithm.amount):
            if i % 3 == 0:
                pygame.draw.rect(screen, self.white, (i * self.algorithm.line_width, height - self.algorithm.array[i] * height / self.algorithm.max_value, self.algorithm.line_width, self.algorithm.array[i] * height / self.algorithm.max_value))
            elif i % 3 == 1:
                pygame.draw.rect(screen, self.light_grey, (i * self.algorithm.line_width, height - self.algorithm.array[i] * height / self.algorithm.max_value, self.algorithm.line_width, self.algorithm.array[i] * height / self.algorithm.max_value))
            else:
                pygame.draw.rect(screen, self.grey, (i * self.algorithm.line_width, height - self.algorithm.array[i] * height / self.algorithm.max_value, self.algorithm.line_width, self.algorithm.array[i] * height / self.algorithm.max_value))

    def draw(self):
        screen.fill(self.dark_grey)

        # If values above or below zero, move the starting line from the bottom of the screen to the middle or top
        self.drawLines()

        pygame.display.update()

    def run(self):
        self.algorithm.createRandArray()
        while self.running:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    if event.key == pygame.K_RETURN:
                        # Sort, then draw lines again
                        self.algorithm.quickSort(self.algorithm.array, 0, self.algorithm.amount - 1)
                        self.drawLines()
                    if event.key == pygame.K_r:
                        self.algorithm.array = []
                        self.algorithm.createRandArray()
                        self.drawLines()


if __name__ == '__main__':
    main = Main()
    main.run()
    pygame.quit()
    quit()
