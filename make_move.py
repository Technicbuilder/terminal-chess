from board import Board
from queen import Queen

class Player:
    def __init__(self, score, player_colour, board):
        self.score = score
        self.colour = player_colour
        self.colour_bool = True if player_colour == 'white' else False
        self.captured_pieces = []
        self.board = board
        
        #   Make a check function to clean up make_move should contain all mini barriers below noted:
        
    def make_move(self):
        while True:
            self.player_move = input(f'Please enter your move, {self.colour} >>> ')
            reason, status = self.validate_input(listed_move=self.player_move)
            if not status:
                print(f'Invalid input: {reason}')   #123123
                continue

            self.listed_move = self.player_move.split()
            start_position = self.listed_move[1]
            destination = self.listed_move[2]

            start_x, start_y = self.convert_position_to_number(start_position)
            destination_x, destination_y = self.convert_position_to_number(destination)
            piece = self.board.board[start_y][start_x]

            if piece == 0: #123123
                print('There is no piece on that square, try again')
                continue

            if piece.colour != self.colour_bool:
                print('That is not your piece, try again')  #123123
                continue

            piece.move(self.board.board)
            if (destination_x, destination_y) not in piece.available_locations:
                print(f'Invalid move for {type(piece).__name__}, try again')    #123123
                continue
            
            self.capture(destination_x=destination_x, destination_y=destination_y)

            self.board.board[start_y][start_x] = 0
            piece.position = (destination_x, destination_y)
            piece.start_pawn = False
            self.board.board[destination_y][destination_x] = piece

            if self.end_of_board_pawn(piece=piece, destination_x=destination_x, destination_y=destination_y):
                break

    def convert_position_to_number(self, position):
        columns = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        x = columns[position[0]]
        y = int(position[1]) - 1
        return (x, y)
        
    def validate_input(self, listed_move):
        listed_move = listed_move.split()
        if len(listed_move) != 3:
            return 'Please input something similiar to the following: pawn e2 e4', False
        
        white_pieces = ['queen', 'king', 'bishop', 'knight', 'rook', 'pawn']
        black_pieces = ['b_' + x for x in white_pieces]
        all_pieces = white_pieces + black_pieces
        
        if listed_move[0] not in all_pieces:
            return 'Please use a real piece name, black pieces are denoted by b_[piece_name]', False
        
        
        rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        columns = [x + 1 for x in range(8)]
        all_positions = [row + str(column) for row in rows for column in columns]
        
        temp_positions = (1, 2)
        for numbers in temp_positions:
            if listed_move[numbers] not in all_positions:
                return f'Position {listed_move[numbers]} is not recognised', False
        
        return '', True
    
    def print_score(self, black_score, white_score):
        if self.score == 0:
            return
        else:
            if white_score == black_score:
                return
            elif white_score > black_score:
                print(f'White is +{self.score} points up')
            else:
                print(f'Black is {self.score} points up')

    def end_of_board_pawn(self, piece, destination_y, destination_x):
        if type(piece).__name__ == 'Pawn':
                if (self.colour_bool and destination_y == 7) or (not self.colour_bool and destination_y == 0):
                    self.board.board[destination_y][destination_x] = Queen(starting_position=(destination_x, destination_y), colour=self.colour_bool)
                    temp_dict = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
                    print(f'Pawn promoted to queen at {temp_dict[destination_x]}{destination_y}')
        return True

    def capture(self, destination_y, destination_x):
            target = self.board.board[destination_y][destination_x]
            if target != 0:
                if target.colour:
                    self.board.white_pieces.remove(target)
                else:
                    self.board.black_pieces.remove(target)
                self.captured_pieces.append(target)
                self.score += target.piece_value


if __name__ == '__main__':
    board = Board()
    board.print_board()
    white_player = Player(score=0, player_colour='white', board=board)
    black_player = Player(score=0, player_colour='black', board=board)
    
    white_king = board.board[0][4]
    black_king = board.board[7][4]
    
    while True:

        white_player.print_score(white_score=white_player.score, black_score=black_player.score)

        white_player.make_move()
        board.print_board()
        
        if black_king.checkmate(board):
            print('\nCheckmate, white wins')
            break

        black_player.make_move()
        board.print_board()
        
        if white_king.checkmate(board):
            print('\nCheckmate, black wins')
            break
        
