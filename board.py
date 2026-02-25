from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King

class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)] for x in range(8)]
        self.white_pieces = []
        self.black_pieces = []
        #   generate rooks
        self.board[0][0] = Rook(starting_position=(0, 0), colour=True)
        self.board[0][7] = Rook(starting_position=(7, 0), colour=True)
        self.board[7][0] = Rook(starting_position=(0, 7), colour=False)
        self.board[7][7] = Rook(starting_position=(7, 7), colour=False)
        #   generate knights
        self.board[0][1] = Knight(starting_position=(1, 0), colour=True)
        self.board[0][6] = Knight(starting_position=(6, 0), colour=True)
        self.board[7][1] = Knight(starting_position=(1, 7), colour=False)
        self.board[7][6] = Knight(starting_position=(6, 7), colour=False)
        
        #   generate bishops
        self.board[0][2] = Bishop(starting_position=(2, 0), colour=True)
        self.board[0][5] = Bishop(starting_position=(5, 0), colour=True)
        self.board[7][2] = Bishop(starting_position=(2, 7), colour=False)
        self.board[7][5] = Bishop(starting_position=(5, 7), colour=False)
        
        #   generate queens
        self.board[0][3] = Queen(starting_position=(3, 0), colour=True)
        self.board[7][3] = Queen(starting_position=(3, 7), colour=False)
        
        #   generate kings
        self.board[0][4] = King(starting_position=(4, 0), colour=True)
        self.board[7][4] = King(starting_position=(4, 7), colour=False) 
        
        #   generate pawns
        for spaces in range(8):
            self.board[1][spaces] = Pawn(starting_position=(spaces, 1), colour=True)
            self.board[6][spaces] = Pawn(starting_position=(spaces, 6), colour=False)
            
        for rows in self.board:
            for pieces in rows:
                
                if pieces == 0:
                    continue
                colour = getattr(pieces, 'colour', False)
                
                if colour:
                    self.white_pieces.append(pieces)
                else:
                    self.black_pieces.append(pieces)
            
        
        
    def print_board(self):
        print('      a    b    c    d    e    f    g    h')
        for i, rows in enumerate(self.board):
            print(f'{i+1} ', ' '.join(f"{str(item):>4}" for item in rows))
            
            
            
            
if __name__ == '__main__':
    chess_board = Board()
    chess_board.print_board()