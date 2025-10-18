# %%
import random

rows= 6
cols= 7
game = []
empty = "_"
firstPlayer = "Ram"
secondPlayer = "Shyam"
firsPlayerCoin = "X"
secondPlayerCoin = "O"


def initialize_game():
    for x in range(rows):
        game.append([])
        for y in range(cols):
            game[x].append(empty)

#print(game)

def fill_random_values():
    for x in range(rows):
        game.append([])
        for y in range(cols):
            game[x][y] = random.randint(0, 1)


def output_board():
    print("-------------------Board update------------------")
    for i in range(len(game)):
        for j in range(len(game[i])):
            print(game[i][j], end=" ")
        print("\n")


def game_finished():
    flag = False
    # todo check game finish conditions
    for row in range(rows):
        count = 1
        for col in range(cols-1):
            if(game[row][col] == game[row][col+1] and game[row][col] != empty):
                count= count + 1 
                if(count == 4):
                    flag = True
                    break
            else:
                count = 1

    if (flag == True):
        return flag 

    for col in range(cols):
        count = 1
        for row in range(rows-1):
            if(game[row][col] == game[row+1][col] and game[row][col] != empty):
                count= count + 1 
                if(count == 4):
                    flag = True
                    break
            else:
                count = 1

    return flag

def player_move(player):
    coin = ""
    if(player == firstPlayer ):
        coin = firsPlayerCoin
    else:
        coin = secondPlayerCoin
    
    column = 0
    column = int(input(player + " enter column number"))

    if(column > 7 or column < 1):
        print("plz enter value within 1 to 7")
        return 
    
    updated_flag = False
    for row in range(rows-1, 0, -1):
        if(game[row][column-1] == empty):
            game[row][column-1] = coin
            updated_flag = True
            break

    
    if(updated_flag == False):
        print("Column is full, try again.")
        #player(player)

       
def swap_player(player):
    if(player == firstPlayer):
        return secondPlayer
    else:
        return firstPlayer

        






def main():
    print("Hello World")
        
    initialize_game()
    # output_board()
    # fill_random_values()
    output_board()
    player = firstPlayer
    while(not game_finished()):
        player_move(player)
        output_board()
        if(not game_finished()):
            player = swap_player(player)
    
    print("Game Over")

if __name__=="__main__":
    main()

# %%
# 01 CALL InitialiseBoard
# 02 CALL SetUpGame
# 03 CALL OutputBoard
# 04 WHILE GameFinished = FALSE DO
# 05 CALL PlayerMakesMove
# 06 CALL OutputBoard
# 07 CALL CheckGameFinished
# 08 IF GameFinished = FALSE
# 09 THEN
# 10 CALL SwapThisPlayer
# 11 ENDIF
# 12 ENDWHILE






