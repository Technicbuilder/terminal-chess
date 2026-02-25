class King:
    def __init__(self, starting_position, colour):
        self.colour = colour     #   if true, piece is white
        self.piece_value = 0
        self.start_pawn = True
        self.position = starting_position
        self.look = 'Ki' if colour else 'BKi'
        
    def __str__(self):
        return self.look
    
    def __repr__(self):
        return self.__str__()
        
        
    def move(self, board):
        x, y = self.position
        self.available_locations = []
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0),
                 (1, 1), (1, -1), (-1, 1), (-1, -1)]
        
        for move_x, move_y in moves:
            next_x = x + move_x
            next_y = y + move_y
            
            while 0 <= next_x <= 7 and 0 <= next_y <= 7:
                if board[next_y][next_x] == 0:
                    self.available_locations.append((next_x, next_y))
                    break                    
                elif board[next_y][next_x].colour != self.colour:
                    self.available_locations.append((next_x, next_y))
                    break
                else:
                    break
                
#   Got claude ai to finish this off from here (everything below)

    def in_check(self, board):
        unfriendly_pieces = board.black_pieces if self.colour else board.white_pieces
        for piece in unfriendly_pieces:
            piece.move(board.board)
            if self.position in piece.available_locations:
                return True
        return False
    
    def checkmate(self, board):
        if not self.in_check(board):
            return False
        
        self.move(board.board)
        for moves in self.available_locations:
            original = board.board[moves[1]][moves[0]]
            board.board[self.position[1]][self.position[0]] = 0
            board.board[moves[1]][moves[0]] = self
            old_pos = self.position
            self.position = moves
            
            still_in_check = self.in_check(board)
            
            #   undo the move
            self.position = old_pos
            board.board[old_pos[1]][old_pos[0]] = self
            board.board[moves[1]][moves[0]] = original
            
            if not still_in_check:
                return False
        
        return True