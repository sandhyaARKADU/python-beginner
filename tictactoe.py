import tkinter as tk
from tkinter import messagebox

# Initialize the main application window
root = tk.Tk()
root.title("Tic Tac Toe")

# Initialize game variables
current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
buttons = []

# Function to check for a winner
def check_winner():
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

# Function to check for a tie
def check_tie():
    for row in board:
        if "" in row:
            return False
    return True

# Function to handle button clicks
def button_click(row, col):
    global current_player
    if board[row][col] == "":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            root.quit()
        elif check_tie():
            messagebox.showinfo("Game Over", "It's a tie!")
            root.quit()
        else:
            current_player = "O" if current_player == "X" else "X"

# Create the game board buttons
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = tk.Button(root, text="", font=("Helvetica", 20), width=5, height=2,
                           command=lambda i=i, j=j: button_click(i, j))
        button.grid(row=i, column=j)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Start the Tkinter event loop
root.mainloop()
