class Game():
    def __init__(self, turn):
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
        game.print_board()
        game.print_message()

    def get_move(self):
        move = input(f'Enter a valid move (example: A1:): ').lower()
        print(f'The user entered {move}')

        while True: 
            move = input 


game = Game('X')
game.print_board()
game.print_message()
game.get_move()