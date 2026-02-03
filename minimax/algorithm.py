from copy import deepcopy
from checkers.constants import LIGHT_PIECE, DARK_PIECE

def minimax(pos, depth, max_player, game, alpha=float('-inf'), beta=float('inf')):
    if depth == 0 or pos.winner() is not None:
        return pos.evaluate(), pos
    
    if max_player:
        max_eval = float('-inf')
        best_move = None
        
        for move in getAllMoves(pos, LIGHT_PIECE, game):
            evaluation = minimax(move, depth - 1, False, game, alpha, beta)[0]
            
            if evaluation > max_eval:
                max_eval = evaluation
                best_move = move
            
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        
        for move in getAllMoves(pos, DARK_PIECE, game):
            evaluation = minimax(move, depth - 1, True, game, alpha, beta)[0]
            
            if evaluation < min_eval:
                min_eval = evaluation
                best_move = move
                
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        
        return min_eval, best_move

def getAllMoves(board, color, game):
    moves = []
    
    for piece in board.getAllPieces(color):
        valid_moves = board.getValidMoves(piece)
        
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.getPiece(piece.row, piece.col)
            new_board = simulateMove(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
            
    
    return moves

def simulateMove(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    
    if skip:
        board.remove(skip)
    
    return board