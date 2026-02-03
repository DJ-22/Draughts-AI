from checkers.constants import PIECE_VALUE, KING_VALUE, LIGHT_PIECE, DARK_PIECE, ROWS

def evaluateBoard(board):
    score = materialEvaluation(board) + positionalEvaluation(board) + kingEvaluation(board) + mobilityEvaluation(board)
    return score

def materialEvaluation(board):
    light_pieces = board.light_left - board.light_kings
    dark_pieces = board.dark_left - board.dark_kings
    score = (light_pieces - dark_pieces) * PIECE_VALUE
    
    return score

def kingEvaluation(board):
    return (board.light_kings - board.dark_kings) * KING_VALUE

def positionalEvaluation(board):
    score = 0
    
    for row in range(ROWS):
        for col in range(len(board.board[row])):
            piece = board.board[row][col]
            if piece != 0 and not piece.king:
                if piece.color == LIGHT_PIECE:
                    score += (ROWS - row) * 0.5
                else:
                    score -= row * 0.5
    
    return score

def mobilityEvaluation(board):
    light_moves = 0
    dark_moves = 0
    
    for piece in board.getAllPieces(LIGHT_PIECE):
        light_moves += len(board.getValidMoves(piece))
    for piece in board.getAllPieces(DARK_PIECE):
        dark_moves += len(board.getValidMoves(piece))
    
    return (light_moves - dark_moves) * 0.1