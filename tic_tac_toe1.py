import sys
import signal
import atexit
from random import randint
import json

def quit_gracefully():
    """This allows the program to exit gracefully with a peacful message."""
    print('\n\nThanks for Playing!!')
    sys.exit(0)

def quitter():
    """Registered to the atexit to handle all exits as graceful"""
    sys.exit(0)

def signal_handler(sig, frame):
    """Function that handles the signal for CTRL+C and exits with a message"""
    sys.exit(0)

class Configuration():
    def __init__(self, score_file):
        self.score_file = score_file

class Board():
    """Creation, Displaying, Updating, and Checking Tic-Tac-Toe Board"""
    def __init__(self, layout):
        self.layout = layout

    def display_board(self, player1, player2):
        """Prints the tic-tac-toe board out with the current layout"""
        print("*****************\n")
        print("*** {}'s record: {}-{}-{}   ***   {}'s record: {}-{}-{}   ***".format(player1.name, player1.score[0], player1.score[1], player1.score[2], player2.name, player2.score[0], player2.score[1], player2.score[2]))
        print("   {0[1]:^3s}|{0[2]:^3s}|{0[3]:^3s}".format(self.layout))
        print("   ---|---|---")
        print("   {0[4]:^3s}|{0[5]:^3s}|{0[6]:^3s}".format(self.layout))
        print("   ---|---|---")
        print("   {0[7]:^3s}|{0[8]:^3s}|{0[9]:^3s}".format(self.layout))
        print("\n*****************")
    
    def update_board(self, player, slot, other):
        """Updates a specific spot on the tic-tac-toe board"""
        self.layout[slot] = player.symbol
        if player.number == 1:
            self.display_board(player, other)
        else:
            self.display_board(other, player)

    def check_board(self):
        """
        Checks to see if someone won or if there is a tie
        0 = continue game
        1 = a play won
        2 = tie
        """
        continue_game = 0
        if self.layout[1] == self.layout[2] and self.layout[2] == self.layout[3]:
            continue_game = 1
        if self.layout[4] == self.layout[5] and self.layout[5] == self.layout[6]:
            continue_game = 1
        if self.layout[7] == self.layout[8] and self.layout[8] == self.layout[9]:
            continue_game = 1
        if self.layout[1] == self.layout[4] and self.layout[4] == self.layout[7]:
            continue_game = 1
        if self.layout[2] == self.layout[5] and self.layout[5] == self.layout[8]:
            continue_game = 1
        if self.layout[3] == self.layout[6] and self.layout[6] == self.layout[9]:
            continue_game = 1
        if self.layout[1] == self.layout[5] and self.layout[5] == self.layout[9]:
            continue_game = 1
        if self.layout[3] == self.layout[5] and self.layout[5] == self.layout[7]:
            continue_game = 1
        slots_left=[]
        for k,v in self.layout.items():
            if v.isdigit():
                slots_left.append(k)
        if slots_left == [] and continue_game == 0:
            continue_game = 2
        if continue_game != 0:
            for k,v in self.layout.items():
                if v.isdigit():
                    self.layout[k] = ''
        return continue_game

class Player():
    """Creates a player and their record and controls the players turn"""
    def __init__(self, number, symbol, name, score, isComputer):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.score = score
        self.isComputer = isComputer
    
    def set_name(self):
        """Set the name for the player"""
        while True:
            self.name = input("Please enter name for Player {}: ".format(self.number))
            if len(self.name) > 0:
                break
            else:
                print("*** Please enter a name")
                continue

    def players_turn(self, board, other_player):
        """Control the input for the players turn"""
        available=[]
        computers=[]
        choice=0
        for k, v in board.layout.items():
            if v.isdigit():
                available.append(k)
            elif v == self.symbol:
                computers.append(k)
        if self.isComputer:
            for i in computers:
                if i+1 in available:
                    choice = i+1
                    break
                elif i-1 in available:
                    choice = i-1
            if choice == 0:
                choice = available[randint(available[0],available[-1])]
        else:
            while True:
                try:
                    choice = int(input("Please select slot to play (1-9): "))
                except ValueError:
                    print("Must be between 1-9")
                    continue
                if choice in available:
                    break
                else:
                    print("{} not available".format(choice))
                    continue
        board.update_board(self, choice, other_player)

    def update_score(self, result, config, scores):
        """Update the players record at end of game"""
        if result == 0:
            self.score[0] += 1
        elif result == 1:
            self.score[1] += 1
        else:
            self.score[2] += 1
        scores[self.name] = self.score
        with open(config.score_file, "w") as outfile:  
            json.dump(scores, outfile)

def play_tic_tac_toe():
    """The main function to play a game"""
    try:
        # capture exits to send message first
        atexit.register(quitter)
        # capture CTRL+C
        signal.signal(signal.SIGINT, signal_handler)
        configuration = Configuration('ticTacToeScores.json')
        score_file = open(configuration.score_file, 'r')
        try:
            scores = json.load(score_file)
        except Exception as e:
            print(e)
            scores = {}
        score_file.close()
        while True:
            try:
                players = int(input("How many players? '1/2' "))
            except ValueError:
                print("Please enter '1/2'")
                continue
            if players > 2:
                print("Please enter '1/2'")
                continue
            else:
                break
        player1 = Player(1, 'X', "", [0, 0, 0], False)
        player1.set_name()
        if players == 2:
            player2 = Player(2, 'O', "", [0, 0, 0], False)
            player2.set_name()
        else:
            player2 = Player(2, 'O', "COMPUTER", [0, 0, 0], True)
        print(scores)
        if player1.name in scores:
            player1.score = scores[player1.name]
        if player2.name in scores:
            player2.score = scores[player2.name]
        play_again = True
        starter = player2
        other = player1
        while play_again:
            layout = {1: '1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
            board = Board(layout)
            board.display_board(player1, player2)
            continue_game = 0
            while continue_game == 0:
                if starter == player1:
                    starter = player2
                    other = player1
                else:
                    starter = player1
                    other = player2
                print("{}'s turn".format(starter.name))
                starter.players_turn(board, other)
                continue_game = board.check_board()

            if continue_game == 1:
                print("\n{} is the WINNER".format(starter.name.upper()))
                board.display_board(player1, player2)
                print("{} is the WINNER\n".format(starter.name.upper()))
                if starter.number == 1:
                    player1.update_score(0, configuration, scores)
                    player2.update_score(1, configuration, scores)
                else:
                    player1.update_score(1, configuration, scores)
                    player2.update_score(0, configuration, scores)
            else:
                print("\nGame is a DRAW".format(starter.name.upper()))
                board.display_board(player1, player2)
                print("Game is a DRAW\n".format(starter.name.upper()))
                player1.update_score(2, configuration, scores)
                player2.update_score(2, configuration, scores)
            
            print("*** {}'s record: {}-{}-{}   ***   {}'s record: {}-{}-{}   ***".format(player1.name, player1.score[0], player1.score[1], player1.score[2], player2.name, player2.score[0], player2.score[1], player2.score[2]))
            while True:
                play_again = input("Play Again 'Y/N': ").lower()
                if play_again == 'y':
                    play_again = True
                    break
                if play_again == 'n':
                    play_again = False
                    break
                else:
                    print("*** Please enter 'Y/N'")
                    continue
    ### Be able to handle a CTRL+D (EOFError) and exit with a message informing the user
    ### Catch the SystemExit error, if thrown
    except (SystemExit, EOFError) as e:
        quit_gracefully()

### Check to see if the program is being called as the main program
if __name__ == '__main__':
    play_tic_tac_toe()