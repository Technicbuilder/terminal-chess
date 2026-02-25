class Pawn:
    def __init__(self, starting_position, colour):
        self.colour = colour     #   if true, piece is white
        self.piece_value = 1
        self.start_pawn = True
        self.position = starting_position
        self.look = 'p' if colour else 'pp'
        self.direction = 1 if self.colour else -1
        
    def __str__(self):
        return self.look
    
    def __repr__(self):
        return self.__str__()
        
        
    def move(self, board):
        x, y = self.position
        self.available_locations = []
        
        if 0 <= x + 1 <= 7:
            left_piece = board[y + self.direction][x + 1]
            if left_piece != 0 and left_piece.colour != self.colour:
                self.available_locations.append((x + 1, y + self.direction))
            
        if 0 <= x - 1 <= 7: 
            right_piece = board[y + self.direction][x - 1]
            if right_piece != 0 and right_piece.colour != self.colour:
                self.available_locations.append((x - 1, y + self.direction))
            
        forward = board[y + self.direction][x]
        if forward == 0:
            self.available_locations.append((x, y + self.direction))
            if self.start_pawn and board[y + self.direction * 2][x] == 0:
                self.available_locations.append((x, y + self.direction * 2))

        