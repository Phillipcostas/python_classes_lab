class Game():
    def __init__(self, turn='X'):
        self.turn = turn
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
        self.winner = None
        self.tie = False

    def print_board(self):
        b = self.board
        print(f"""
        A   B   C
    1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
        ----------
    2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
        ----------
    3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
  """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_valid_move(self):
        while True:
            move = input("Enter your move (e.g., a1, b2): ").lower()
            if move in self.board and self.board[move] is None:
                return move
            else:
                print("Invalid move. Please try again.")

    def place_piece(self):
        move = self.get_valid_move()
        self.board[move] = self.turn
        self.check_winner() 
        self.check_tie()  
        self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        pass

    def check_tie(self):
        pass

    def check_for_winner(self):
        self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])

        self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2'])

        self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3'])

        self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3'])

        self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])

        self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])

        self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])
        
        self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1'])


    print(check_for_winner)


game = Game()
while not game.winner and not game.tie:
    game.render()
    game.place_piece()
game.render() 