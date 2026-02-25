class Knight:
    def __init__(self, starting_position, colour):
        self.colour = colour     #   if true, piece is white
        self.piece_value = 3
        self.start_pawn = True
        self.position = starting_position
        self.look = 'K' if colour else 'KK'
        
    def __str__(self):
        return self.look
    
    def __repr__(self):
        return self.__str__()
    
    def available(self, board, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return
        if board[y][x] == 0:   #   board goes (y, x)
            self.available_locations.append((x, y)) 
        elif board[y][x].colour != self.colour:
            self.available_locations.append((x, y))
                
                
        
    def move(self, board):
        """
        1.  Calculate possible moves
        2.  check whether the move captures a piece of same colour
        3.  Check whether king is in danger after move
        """
        self.available_locations = []
        #   NOTE No3 logic will be made later   Done
        self.position = self.position   #   (x, y) 
                                        #   board goes (y, x)
        #   NOTE: finish logic tommorow
        moves = [(2, -1), (2, 1), (-2, -1), (-2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        for possibilities in moves:
            self.available(board=board, x=self.position[0] + possibilities[0], y=self.position[1] + possibilities[1])
        
        
        """
        position = (3, 4)
        chess_board.board[position[0]][position[1]] != 0
        """
        
        
        