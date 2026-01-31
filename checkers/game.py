from .constants import LIGHT_PIECE, DARK_PIECE, SQUARE_SIZE, SELECTED_COLOR, VALID_MOVE_COLOR
from .board import Board
import pygame

class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = LIGHT_PIECE
        self.valid_moves = {}
    
    def update(self):
        self.board.draw(self.win)
        self.drawValidMoves(self.valid_moves)
        pygame.display.update()
    
    def reset(self):
        self._init()
    
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.getPiece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.getValidMoves(piece)
            
            return True
    
        return False
    
    def _move(self, row, col):
        piece = self.board.getPiece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            
            if skipped:
                self.board.remove(skipped)
            self.changeTurn()
        else:
            return False
        
        return True
    
    def changeTurn(self):
        self.valid_moves = {}
        
        if self.turn == LIGHT_PIECE:
            self.turn = DARK_PIECE
        else:
            self.turn = LIGHT_PIECE
    
    def drawValidMoves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, VALID_MOVE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)
    
    def winner(self):
        return self.board.winner()
    
    def getBoard(self):
        return self.board
    
    def aiMove(self, board):
        self.board = board
        self.changeTurn()