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
    valid_moves = gs.get_valid_moves()
    move_made = False # flag for when a move is made
    print(gs.board)
    load_images() # only once, before the while loop.
    running = True
    sq_selected = () # keeps track of user's last click.
    player_clicks = [] # to move, keeps track of user's several clicks.

    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

            # KEY HANDLERS:
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # undo a move when z is pressed.
                    gs.undo_move()
                    move_made = True


            # MOUSE HANDLERS:
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # x, y coordinates of the mouse.
                row = location[1] // SQ_SIZE
                col = location[0] // SQ_SIZE

                if sq_selected == (row, col): # if user clicks the same square, it usually means an undo, so we undo their last move.
                    sq_selected = () # undo.
                    player_clicks = [] # undo the click as well, the user undid their move.
                else:
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected) # append for both first and second clicks.
                    print(player_clicks)

                if len(player_clicks) == 2:
                    print(player_clicks[0])
                    print(player_clicks[1])
                    move = engine.Move(player_clicks[0], player_clicks[1], gs.board)
                    print(move.get_chess_notation())

                    if move in valid_moves:
                        gs.make_move(move)
                        move_made = True
                    
                    sq_selected = () # reset user clicks.
                    player_clicks = [] # after the move, reset the array for the next move.

        if move_made:
            valid_moves = gs.get_valid_moves()
            move_made = False

        draw_game_state(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
draws the squares on the board.
'''
def draw_board(screen):
    colors = [p.Color('white'), p.Color('gray')]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE ,r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            

'''
draws the pieces on top of those squares.
'''
def draw_pieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--':
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))

'''
responsible for handling all the graphics within a current game state.
'''
def draw_game_state(screen ,gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)

if __name__ == '__main__':
    main()