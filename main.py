'''
responsible for handling user input and displaying the current game state object.
'''

import pygame as p
import engine 

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

'''
initialize a global set of dictionary of images. 
this will be called exactly once in the main.
'''

def load_images():
    pieces = ['wP', 'bP', 'wR', 'bR', 'wB', 'bB', 'wN', 'bN', 'wQ', 'bQ', 'wK', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load('images/' + piece + '.png'), (SQ_SIZE - 5, SQ_SIZE - 5))

'''
main driver of the code.
this handles the user inputs and updates the graphics.
'''

def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color('white'))
    gs = engine.GameState()
    print(gs.board)
    load_images() # only once, before the while loop
    running = True

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
draws the squares on the board
'''
def draw_board(screen, board):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE ,r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            
            

'''
draws the pieces on top of those squares
'''
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
responsible for handling all the graphics within a current game state
'''
def draw_game_state(screen ,gs):
    draw_board(screen, gs.board)
    draw_pieces(screen, gs.board)


if __name__ == '__main__':
    main()