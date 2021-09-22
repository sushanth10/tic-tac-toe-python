import random

choices = ['X', 'O']
try:
#     Choice of X-O given to the player
    player_sym = input("Choose 'X' or 'O' : ")
#     raising an exception if the variable is not X or O
    if player_sym!='X' and player_sym!='O':
        raise Exception("Symbol not found")
except Exception as e:
    print(e.args)
else:
#     Allotting the other one as the computer symbol
    choices.remove(player_sym)
    comp_sym = choices[0]
    player_dict = {player_sym:'Player', comp_sym:'Computer'}
    
# creating the board
board = [' ']*9
gameEnd = False # to track when the game ends
unmarked = [i for i in range(9)] # to track all the blank boxes left



# gameOver function check if the game already has a winner
def gameOver(board, symbol):
#     below is the sequence of all the possible winning combinations 
    if board[0]==board[3]==board[6]==symbol or board[1]==board[7]==board[4]==symbol or board[2]==board[5]==board[8]==symbol or board[0]==board[1]==board[2]==symbol or board[5]==board[3]==board[4]==symbol or board[6]==board[7]==board[8]==symbol or board[2]==board[4]==board[6]==symbol or board[0]==board[4]==board[8]==symbol:
#             if there is a pattern match the game is over hence return True
            return True



# function for marking the box with the symbol

def mark(pos, symbol):
    board[pos] = symbol
    unmarked.remove(pos)
#    Used it for debugging : print(f"Unmarked : {unmarked}")



# function to display the board at a particular time
def displayBoard():
    for i in range(len(board)):
#         formatting the output for the middle elements
        if i==1 or i==4 or i==7:
            print(f'|{board[i]}|', end=' ')
        elif i==2 or i==5:
            print(f'{board[i]}\n--------') # marks the end of a line and hence bifurcates two lines
        else:
            print(f'{board[i]}', end=' ')


if __name__== "__main__":
    #    this is where the game starts                    
    while not gameEnd: # loop until game ends
        try:
            player_pos = int(input("\n\nWhere would you mark? "))
    #         check if position index is on the board and is available for marking else raise Exception
            if player_pos<0 or player_pos>8 or (player_pos not in unmarked): 
                raise Exception("Position out of Board")
                break
        except Exception as e:
            print(e.args)
        else:
            mark(player_pos, player_sym)
            
    #         check if the game has already ended and if yes, declare the player as winner
            if gameOver(board, player_sym): 
                displayBoard()
                print("\n\nPlayer Won!!!")
                break
                
    #         computer will mark on some random square that is not marked yet
            comp_pos = unmarked[random.randint(0, len(unmarked)-1)]
            mark(comp_pos, comp_sym)
            
    #         check if the game has already ended and if yes, declare the computer as winner
            if gameOver(board, comp_sym): 
                displayBoard()
                print("\n\nComputer WON!!!")
                break
                
    #             display the board after each iteration
            displayBoard()
            
    #         marks the end of the game
    print("GAME OVER")