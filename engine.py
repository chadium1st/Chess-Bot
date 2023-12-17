'''
this class is responsible for storing all the information about the current state of the game.
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

		self.white_to_move = True
		self.move_log = []

	def make_move(self, move):
		self.board[move.start_row][move.start_col] = '--'
		self.board[move.end_row][move.end_col] = move.piece_moved
		self.move_log.append(move) # log the move so we can undo it later
		self.white_to_move = not self.white_to_move # swap pieces

class Move():

	# mapping files to rows and columns.
	ranks_to_rows = {
		'1': 7,
		'2': 6,
		'3': 5,
		'4': 4,
		'5': 3,
		'6': 2,
		'7': 1,
		'8': 0,
	}
	rows_to_ranks = {v: k for k, v in ranks_to_rows.items()}

	files_to_cols = {
		'a': 0,
		'b': 1,
		'c': 2,
		'd': 3,
		'e': 4,
		'f': 5,
		'g': 6,
		'h': 7,
	}
	cols_to_files = {v: k for k, v in files_to_cols.items()}



	def __init__(self, start_sq, end_sq, board):
		# decoupling the tuples for ease of use and better control.
		self.start_row, self.start_col = start_sq[0], start_sq[1]
		self.end_row, self.end_col = end_sq[0], end_sq[1]

		self.piece_moved = board[self.start_row][self.start_col]
		self.piece_captured = board[self.end_row][self.end_col]

	def get_chess_notation(self):
		return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

	def get_rank_file(self, r,c ):
		return self.cols_to_files[c].lower() + self.rows_to_ranks[r]
	
