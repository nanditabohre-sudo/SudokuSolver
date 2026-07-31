import tkinter as tk
from tkinter import messagebox


# Check whether number can be placed
def is_safe(board, row, col, num):

    for i in range(9):
        if board[row][i] == num:
            return False

        if board[i][col] == num:
            return False


    start_row = row - row % 3
    start_col = col - col % 3


    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    return True



# Backtracking Algorithm
def solve(board):

    for row in range(9):

        for col in range(9):

            if board[row][col] == 0:

                for num in range(1,10):

                    if is_safe(board,row,col,num):

                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0

                return False

    return True



def solve_sudoku():

    board=[]

    try:

        for i in range(9):

            row=[]

            for j in range(9):

                value=entries[i][j].get()

                if value=="":
                    row.append(0)

                else:
                    row.append(int(value))

            board.append(row)


        if solve(board):

            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0,tk.END)
                    entries[i][j].insert(0,board[i][j])

        else:
            messagebox.showerror(
                "Error",
                "No Solution Exists"
            )

    except:

        messagebox.showerror(
            "Error",
            "Enter valid numbers only"
        )



def reset():

    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0,tk.END)



# GUI

window=tk.Tk()

window.title("Sudoku Solver")
window.geometry("400x450")


entries=[]


frame=tk.Frame(window)
frame.pack(pady=20)


for i in range(9):

    row=[]

    for j in range(9):

        entry=tk.Entry(
            frame,
            width=3,
            font=("Arial",18),
            justify="center"
        )

        entry.grid(
            row=i,
            column=j,
            padx=2,
            pady=2
        )

        row.append(entry)

    entries.append(row)



solve_btn=tk.Button(
    window,
    text="Solve Sudoku",
    command=solve_sudoku,
    width=15
)

solve_btn.pack(pady=5)



reset_btn=tk.Button(
    window,
    text="Reset",
    command=reset,
    width=15
)

reset_btn.pack()



window.mainloop()