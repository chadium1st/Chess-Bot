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

		self.move_functions = {
			'P': self.get_pawn_moves,
			'R': self.get_rook_moves,
			'N': self.get_knight_moves,
			'B': self.get_bishop_moves,
			'Q': self.get_queen_moves,
			'K': self.get_king_moves
		}

		self.white_to_move = True
		self.move_log = []

	# takes a move as a parameter and executes it.
	def make_move(self, move):
		self.board[move.start_row][move.start_col] = '--'
		self.board[move.end_row][move.end_col] = move.piece_moved
		self.move_log.append(move) # log the move so we can undo it later
		self.white_to_move = not self.white_to_move # swap pieces

	# undoes the last move.
	def undo_move(self):
		if len(self.move_log) != 0: # making sure there exists a move to undo it.
			move = self.move_log.pop()
			self.board[move.start_row][move.start_col] = move.piece_moved
			self.board[move.end_row][move.end_col] = move.piece_captured
			self.white_to_move = not self.white_to_move # switch turns back.

	'''
	all moves considering checks:
	'''
	def get_valid_moves(self):
		return self.get_all_possible_moves()

	'''
	all moves without considering checks:
	'''
	def get_all_possible_moves(self):
		moves = []
		for r in range(len(self.board)):
			for c in range(len(self.board[r])):
				turn = self.board[r][c][0]
				if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):
					# print('here')
					piece = self.board[r][c][1]
					self.move_functions[piece](r, c, moves) # calls the appropriate move function based on the current piece

		return moves

	'''
	get all the pawn moves located at the specified row and column (r, c):
	'''
	def get_pawn_moves(self, r, c, moves):
		if self.white_to_move: # white pawn moves
			if self.board[r-1][c] == '--': # 1 square advance
				moves.append(Move((r, c), (r-1, c), self.board))
				if r == 6 and self.board[r-2][c] == '--': # 2 square advance
					moves.append(Move((r, c), (r-2, c), self.board))

			if c-1 >= 0: # captures to the left
				if self.board[r-1][c-1][0] == 'b': # enemy piece present to capture
					moves.append(Move((r, c), (r-1, c), self.board))

			if c+1 < len(self.board) - 1: # captures to the right
				if self.board[r-1][c+1][0] == 'b': # enemy piece to capture
					moves.append(Move((r, c), (r-1, c+1), self.board))

		else: # black pawn moves
			pass


	'''
	get all the rook moves located at the specified row and column (r, c):
	'''
	def get_rook_moves(self, r, c, moves):
		pass

	'''
	get all the knight moves located at the specified row and column (r, c):
	'''
	def get_knight_moves(self, r, c, moves):
		pass

	'''
	get all the bishop moves located at the specified row and column (r, c):
	'''
	def get_bishop_moves(self, r, c, moves):
		pass

	'''
	get all the queen moves located at the specified row and column (r, c):
	'''
	def get_queen_moves(self, r, c, moves):
		pass

	'''
	get all the king moves located at the specified row and column (r, c):
	'''
	def get_king_moves(self, r, c, moves):
		pass

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
		self.start_row = start_sq[0]
		self.start_col = start_sq[1]
		self.end_row = end_sq[0]
		self.end_col = end_sq[1]

		self.piece_moved = board[self.start_row][self.start_col]
		self.piece_captured = board[self.end_row][self.end_col]
		self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col
		print(self.move_id)

	'''
	overriding the equals method
	'''
	def __eq__(self, other):
		if isinstance(other, Move):
			return self.move_id == other.move_id
		return False


	def get_chess_notation(self):
		return self.get_rank_file(self.start_row, self.start_col) + self.get_rank_file(self.end_row, self.end_col)

	def get_rank_file(self, r,c ):
		return self.cols_to_files[c].lower() + self.rows_to_ranks[r]
	
