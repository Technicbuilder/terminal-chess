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
        self.generate_pieces()

    def generate_pieces(self):
        #   generate rooks
        rook_starting_positions = [(0, 0, True), (0, 7, True), (7, 0, False), (7, 7, False)]
        self.assign_object(piece=Rook, attributes=rook_starting_positions)

        #   generate knights
        knight_starting_positions = [(0, 1, True), (0, 6, True), (7, 1, False), (7, 6, False)]
        self.assign_object(piece=Knight, attributes=knight_starting_positions)
        
        #   generate bishops
        bishop_starting_positions = [(0, 2, True), (0, 5, True), (7, 2, False), (7, 5, False)]
        self.assign_object(piece=Bishop, attributes=bishop_starting_positions)
        
        
        #   generate queens
        queen_starting_positions = [(0, 3, True), (7, 3, False)]

        self.assign_object(piece=Queen, attributes=queen_starting_positions)
        
        #   generate kings
        king_starting_positions = [(0, 4, True), (7, 4, False)]
        self.assign_object(piece=Queen, attributes=king_starting_positions)
        
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
            
        
    def assign_object(self, piece, attributes):
        for (y, x , colour) in attributes:
            self.board[y][x] = piece(starting_position=(x, y), colour=colour)


    def print_board(self):
        print('      a    b    c    d    e    f    g    h')
        print('===========================================')
        for i, rows in enumerate(self.board):
            print(f'{i+1}|', ' '.join(f"{str(item):>4}" for item in rows))
            
            
            
            
if __name__ == '__main__':
    chess_board = Board()
    chess_board.print_board()
