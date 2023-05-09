import random
import os.path
import json
random.seed()

def draw_board(board):
    print(board)

def welcome(board):
    print("Welcome to the 'Unbeataible Noughts and Crossess' game .")
    print("The board layout is shown below")
    draw_board(board)
    print("When prompted,enter the number corresponding to the square you want.")

def initialise_board(board):
    board = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] =" "
    print(board)
    return board
    
def get_player_move(board):
    while True:
        try:
            move=int(input("Enter a input number between (1-9) :"))
            if (move<1 and move>9):
                raise ValueError();
            row,col=(move-1)//3,(move-1)%3
            if board[row,col] != " ":
                raise ValueError
            return row,col
        except Exception as e:
            print(e)

def choose_computer_move(board):
    while True:
        try:
            random_move=random.randint(1,9)
            row,col=(random_move-1)//3,(random_move-1)%3
            if board[row,col] != " ":
                raise ValueError
            return row,col
        except Exception as e:
            print(e)


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    return True
        
def play_game(board):
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    # then draw the board
    # then in a loop, get the player move, update and draw the board
    # check if the player has won by calling check_for_win(board, mark),
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
    # check if the computer has won by calling check_for_win(board, mark),
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
    # if drawn, return 0 for the score
    #repeat the loop
    return 0
                    
                
def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    return leaders
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    pass




def menu():
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    return choice

def load_scores():
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    # return the dictionary in leaders
    return leaders
    
def save_score(score):
    # develop code to ask the player for their name
    # and then save the current score to the file 'leaderboard.txt'
    return


def display_leaderboard(leaders):
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    pass

