from flask import Flask, render_template, request

app = Flask(__name__)


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



@app.route("/", methods=["GET","POST"])
def home():

    solved = None

    if request.method == "POST":

        board=[]

        for i in range(9):

            row=[]

            for j in range(9):

                value=request.form.get(f"cell{i}{j}")

                if value=="":
                    row.append(0)
                else:
                    row.append(int(value))

            board.append(row)


        if solve(board):
            solved=board


    return render_template(
        "index.html",
        solved=solved
    )



if __name__=="__main__":
    app.run(debug=True)