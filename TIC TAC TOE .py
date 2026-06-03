import math


board = [' ' for _ in range(9)]

def print_board():

    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_winner(b, player):
   
    win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    return any(all(b[i] == player for i in condition) for condition in win_conditions)

def is_full():
    return ' ' not in board

def minimax(b, depth, is_maximizing):
    
    if check_winner(b, 'O'): return 1
    if check_winner(b, 'X'): return -1
    if is_full(): return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def get_best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move


while True:
    print_board()
    try:
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] == ' ':
            board[human_move] = 'X'
        else:
            print("Invalid move! Try again.")
            continue
    except (ValueError, IndexError):
        print("Please enter a number between 0 and 8.")
        continue

    if check_winner(board, 'X'):
        print("You win!")
        break
    if is_full():
        print("It's a draw!")
        break

    print("AI is making a move...")
    board[get_best_move()] = 'O'
    
    if check_winner(board, 'O'):
        print_board()
        print("AI wins!")
        break