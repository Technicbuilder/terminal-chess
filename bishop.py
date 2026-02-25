class Bishop:
    def __init__(self, starting_position, colour):
        self.colour = colour     #   if true, piece is white
        self.piece_value = 3
        self.start_pawn = True
        self.position = starting_position
        self.look = 'B' if colour else 'BB'
        
    def __str__(self):
        return self.look
        
    def __repr__(self):
        return self.__str__()
        
    def move(self, board):
            x, y = self.position
            self.available_locations = []
            moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
            
            for move_x, move_y in moves:
                next_x = x + move_x
                next_y = y + move_y
                
                while 0 <= next_x <= 7 and 0 <= next_y <= 7:
                    if board[next_y][next_x] == 0:
                        self.available_locations.append((next_x, next_y))
                    elif board[next_y][next_x].colour != self.colour:
                        self.available_locations.append((next_x, next_y))
                        break
                    else:
                        break
                    next_x += move_x
                    next_y += move_y