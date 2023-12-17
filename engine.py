'''
his class is responsible for storing all the information about the current state of the game.
also be responsible for determining the valid moves at the current state.
will also keep a move log.
'''

class GameState():
	def __init__(self):
		'''
		the board is 8x8 2d list
		each element of the list has two characters.
		the first character represents the color of the piece.
		the second character represents the type of the piece.
		"--" represents the empty space on the board.
		'''
		self.board = [
			['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
			['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
			['--', '--', '--', '--', '--', '--', '--', '--'],
			['--', '--', '--', '--', '--', '--', '--', '--'],
			['--', '--', '--', '--', '--', '--', '--', '--'],
			['--', '--', '--', '--', '--', '--', '--', '--'],
			['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
			['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
		]

		self.whiteToMove = True
		self.moveLog = []