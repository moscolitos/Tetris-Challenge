# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 08:05:05 2023

@author: Mosco
This is a very minimalistic version, and many features of Tetris (like rotation, line clearing, etc.) 
are missing. But this should provide you with a starting point to expand and refine into a complete game.


"""

import pygame
import random

pygame.init()

# Colors and settings
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WIDTH, HEIGHT = 300, 500
block_size = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Tetris")

shapes = [
    [[1, 1, 1],
     [0, 1, 0]],
    
    [[0, 1, 1],
     [1, 1, 0]],
    
    [[1, 1],
     [1, 1]],
    
    [[1, 1, 0],
     [0, 1, 1]]
]

current_shape = random.choice(shapes)
current_position = [0, 0]

board = [[0 for _ in range(WIDTH // block_size)] for _ in range(HEIGHT // block_size)]

def can_move(shape, position):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board_x = x + position[0]
                board_y = y + position[1]
                if board_x < 0 or board_x >= len(board[0]) or board_y >= len(board) or board[board_y][board_x]:
                    return False
    return True

def merge_shape(board, shape, position):
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                board[y + position[1]][x + position[0]] = 1

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and can_move(current_shape, [current_position[0] - 1, current_position[1]]):
                current_position[0] -= 1
            elif event.key == pygame.K_RIGHT and can_move(current_shape, [current_position[0] + 1, current_position[1]]):
                current_position[0] += 1
            elif event.key == pygame.K_DOWN:
                current_position[1] += 1

    if can_move(current_shape, [current_position[0], current_position[1] + 1]):
        current_position[1] += 1
    else:
        merge_shape(board, current_shape, current_position)
        current_shape = random.choice(shapes)
        current_position = [0, 0]
        if not can_move(current_shape, current_position):
            break

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, RED, (x * block_size, y * block_size, block_size, block_size))

    for y, row in enumerate(current_shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, BLUE, ((x + current_position[0]) * block_size, (y + current_position[1]) * block_size, block_size, block_size))

    pygame.display.flip()
    clock.tick(5)

pygame.quit()
