from tkinter import *

root = Tk()
root.geometry("400x500")
root.title("Tic Tac Toe")
root.configure(bg="#f0f4f8")

board = [" " for _ in range(9)]
current_player = "X"

Label(root, text="Tic Tac Toe",
      font=("Arial", 20, "bold"), bg="#f0f4f8", fg="#333").pack(pady=20)

status = Label(root, text="Player X's turn",
               font=("Arial", 13, "bold"), bg="#f0f4f8", fg="#3498db")
status.pack()

board_frame = Frame(root, bg="#f0f4f8")
board_frame.pack(pady=20)

buttons = []

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return combo

    return None

def click(i):
    global current_player

    if board[i] != " ":
        return

    board[i] = current_player

    color = "#e74c3c" if current_player == "X" else "#27ae60"

    buttons[i].config(
        text=current_player,
        fg=color,
        state=DISABLED
    )

    combo = check_winner(current_player)

    if combo:
        for idx in combo:
            buttons[idx].config(bg="#ffeaa7")

        status.config(
            text=f"Player {current_player} wins! 🎉",
            fg=color
        )

        disable_all()
        reset_btn.config(bg="#e74c3c")
        return

    if " " not in board:
        status.config(
            text="It's a draw! 🤝",
            fg="#f39c12"
        )

        reset_btn.config(bg="#f39c12")
        return

    current_player = "O" if current_player == "X" else "X"

    color = "#e74c3c" if current_player == "X" else "#27ae60"

    status.config(
        text=f"Player {current_player}'s turn",
        fg=color
    )

def disable_all():
    for b in buttons:
        b.config(state=DISABLED)

def reset():
    global board, current_player

    board = [" " for _ in range(9)]
    current_player = "X"

    status.config(
        text="Player X's turn",
        fg="#3498db"
    )

    reset_btn.config(bg="#3498db")

    for b in buttons:
        b.config(
            text="",
            bg="#dce3ea",
            fg="#333",
            state=NORMAL
        )

for i in range(9):
    b = Button(
        board_frame,
        text="",
        font=("Arial", 22, "bold"),
        width=4,
        height=2,
        bg="#dce3ea",
        fg="#333",
        relief="flat",
        cursor="hand2",
        command=lambda x=i: click(x)
    )

    b.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(b)

reset_btn = Button(
    root,
    text="Reset Game",
    font=("Arial", 13, "bold"),
    bg="#3498db",
    fg="white",
    relief="flat",
    padx=25,
    pady=8,
    cursor="hand2",
    command=reset
)

reset_btn.pack(pady=10)

root.mainloop()
