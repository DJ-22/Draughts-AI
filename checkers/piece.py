from .constants import SQUARE_SIZE, LIGHT_PIECE, CROWN_PADDING, BORDER_WIDTH, CROWN_COLOR
import pygame

class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calcPos()
    
    def calcPos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
    
    def makeKing(self):
        self.king = True
    
    def draw(self, win):
        radius = SQUARE_SIZE // 2 - CROWN_PADDING
        pygame.draw.circle(win, (128, 128, 128), (self.x, self.y), radius + BORDER_WIDTH)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        
        if self.king:
            crown_size = radius - CROWN_PADDING
            pygame.draw.circle(win, CROWN_COLOR, (self.x, self.y), crown_size // 2)
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calcPos()
    
    def __repr__(self):
        color_name = "Light" if self.color == LIGHT_PIECE else "Dark"
        check_king = "King" if self.king else "Normal"
        
        return f"{color_name} {check_king} at ({self.row}, {self.col})"