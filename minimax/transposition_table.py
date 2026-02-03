import hashlib
import json

class TranspositionTable:
    def __init__(self):
        self.table = {}
    
    def getBoardHash(self, board):
        board_state = []
        
        for row in board.board:
            row_state = []
            
            for piece in row:
                if piece == 0:
                    row_state.append(0)
                else:
                    row_state.append({
                        'color': piece.color,
                        'king': piece.king,
                        'row': piece.row,
                        'col': piece.col
                    })
            
            board_state.append(row_state)
        
        board_str = json.dumps(board_state, sort_keys=True)
        return hashlib.md5(board_str.encode()).hexdigest()
    
    def store(self, board, depth, evaluation, best_move=None):
        board_hash = self.getBoardHash(board)
        self.table[board_hash] = {
            'depth': depth,
            'evaluation': evaluation,
            'best_move': best_move
        }
    
    def lookup(self, board, depth):
        board_hash = self.getBoardHash(board)
        if board_hash in self.table:
            entry = self.table[board_hash]
            if entry['depth'] >= depth:
                return entry
        
        return None
    
    def clear(self):
        self.table.clear()
    
    def size(self):
        return len(self.table)
    
    def __repr__(self):
        return f"TranspositionTable(entries={self.size()})"