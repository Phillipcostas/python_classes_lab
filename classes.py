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
        if not self.winner:
            self.check_tie()  
        if not self.winner and not self.tie:
            self.turn = 'O' if self.turn == 'X' else 'X'

    def check_winner(self):
        b = self.board
        win_conditions = [
            ('a1', 'b1', 'c1'),  
            ('a2', 'b2', 'c2'),  
            ('a3', 'b3', 'c3'),  
            ('a1', 'a2', 'a3'),  
            ('b1', 'b2', 'b3'),  
            ('c1', 'c2', 'c3'),  
            ('a1', 'b2', 'c3'),  
            ('c1', 'b2', 'a3'),  
        ]
        for wc in win_conditions:
            if b[wc[0]] and b[wc[0]] == b[wc[1]] == b[wc[2]]:
                self.winner = b[wc[0]]
                return

    def check_tie(self):
        if all(self.board[key] is not None for key in self.board):
            self.tie = True

    def play_game(self):
        print("Shall we play a game?")
        while not self.winner and not self.tie:
            self.render()
            self.place_piece()
        self.render()  


game = Game()
game.play_game()
