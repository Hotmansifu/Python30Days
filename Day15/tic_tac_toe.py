from tkinter import *
from tkinter import messagebox

# create the window
root = Tk()
root.title("Tic Tac Toe")

# initialize the players and their symbols
player1 = "X"
player2 = "O"
current_player = player1

# initialize the board
board = ["", "", "", "", "", "", "", "", ""]

# function to handle button click
def button_click(index):
    global current_player
    global board

    # check if the button has already been clicked
    if board[index] != "":
        messagebox.showerror("Error", "This position is already occupied. Choose another one.")
        return

    # update the board with the player's symbol
    board[index] = current_player

    # update the button with the player's symbol
    buttons[index].config(text=current_player)

    # check if the game has been won
    if is_win(current_player):
        messagebox.showinfo("Congratulations!", f"{current_player} has won the game.")
        root.destroy()
        return

    # check if the game is a draw
    if is_draw():
        messagebox.showinfo("Game Over", "The game is a draw.")
        root.destroy()
        return

    # switch to the other player
    current_player = player2 if current_player == player1 else player1

# function to check if the game has been won
def is_win(player):
    if board[0] == board[1] == board[2] == player:
        return True
    if board[3] == board[4] == board[5] == player:
        return True
    if board[6] == board[7] == board[8] == player:
        return True
    if board[0] == board[3] == board[6] == player:
        return True
    if board[1] == board[4] == board[7] == player:
        return True
    if board[2] == board[5] == board[8] == player:
        return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# function to check if the game is a draw
def is_draw():
    for cell in board:
        if cell == "":
            return False
    return True

# create the buttons
buttons = []
for i in range(9):
    button = Button(root, text="", font=("Arial", 40), width=3, height=1, command=lambda index=i: button_click(index))
    button.grid(row=i//3, column=i%3)
    buttons.append(button)

# run the window
root.mainloop()
