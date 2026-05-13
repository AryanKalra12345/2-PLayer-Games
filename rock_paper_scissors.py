from tkinter import *
from random import randint

root = Tk()
root.geometry("400x500")
root.title("Rock Paper Scissors")
root.configure(bg="#f0f4f8")

choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "🪨", "Paper": "📄", "Scissors": "✂️"}
wins, ties, losses = 0, 0, 0
selected = "Rock"

Label(root, text="Rock Paper Scissors",
      font=("Arial", 20, "bold"), bg="#f0f4f8", fg="#333").pack(pady=20)

arena = Frame(root, bg="#f0f4f8")
arena.pack()

Label(arena, text="YOU", font=("Arial", 10, "bold"),
      bg="#f0f4f8", fg="#777").grid(row=0, column=0, padx=30)

Label(arena, text="VS", font=("Arial", 14, "bold"),
      bg="#f0f4f8", fg="#e74c3c").grid(row=0, column=1)

Label(arena, text="COMPUTER", font=("Arial", 10, "bold"),
      bg="#f0f4f8", fg="#777").grid(row=0, column=2, padx=30)

user_icon = Label(arena, text="🤜", font=("Arial", 40),
                  bg="#f0f4f8")
user_icon.grid(row=1, column=0, padx=30)

Label(arena, text="", bg="#f0f4f8").grid(row=1, column=1)

cpu_icon = Label(arena, text="🤖", font=("Arial", 40),
                 bg="#f0f4f8")
cpu_icon.grid(row=1, column=2, padx=30)

user_name = Label(arena, text="—", font=("Arial", 11, "bold"),
                  bg="#f0f4f8", fg="#333")
user_name.grid(row=2, column=0)

cpu_name = Label(arena, text="—", font=("Arial", 11, "bold"),
                 bg="#f0f4f8", fg="#333")
cpu_name.grid(row=2, column=2)

result = Label(root, text="Pick a move and spin!",
               font=("Arial", 12, "bold"), bg="#f0f4f8", fg="#555")
result.pack(pady=15)

btn_frame = Frame(root, bg="#f0f4f8")
btn_frame.pack()

choice_btns = {}

def pick(name):
    global selected
    selected = name

    for n, b in choice_btns.items():
        if n == name:
            b.config(bg="#3498db", fg="white")
        else:
            b.config(bg="#dce3ea", fg="#333")

    user_icon.config(text=emojis[name])
    user_name.config(text=name)

for c in choices:
    b = Button(btn_frame, text=f"{emojis[c]}\n{c}",
               font=("Arial", 11, "bold"), width=7, height=2,
               bg="#dce3ea", fg="#333", relief="flat",
               cursor="hand2", command=lambda x=c: pick(x))
    b.pack(side=LEFT, padx=6)
    choice_btns[c] = b

pick("Rock")

score_frame = Frame(root, bg="#f0f4f8")
score_frame.pack(pady=15)

score_labels = {}

for i, (label, color) in enumerate([
    ("WINS", "#27ae60"),
    ("TIES", "#f39c12"),
    ("LOSSES", "#e74c3c")
]):
    Label(score_frame, text="0", font=("Arial", 22, "bold"),
          bg="#f0f4f8", fg=color).grid(row=0, column=i, padx=20)

    Label(score_frame, text=label, font=("Arial", 9, "bold"),
          bg="#f0f4f8", fg="#999").grid(row=1, column=i)

    score_labels[label] = score_frame.grid_slaves(row=0, column=i)[0]

def spin():
    global wins, ties, losses

    cpu_idx = randint(0, 2)
    cpu_choice = choices[cpu_idx]
    user_idx = choices.index(selected)

    cpu_icon.config(text=emojis[cpu_choice])
    cpu_name.config(text=cpu_choice)

    win_msgs = [
        "You Won 🎉 — Computer: Lucky you!",
        "You Won 🎉 — Computer: How?!",
        "You Won 🎉"
    ]

    lose_msgs = [
        "You Lose 😬 — Computer: I am better!",
        "You Lose 😬 — Computer: Boooo!",
        "You Lose 😬 — Computer: Too easy!"
    ]

    tie_msgs = [
        "Tie! 🤝 — Computer: Bad luck!",
        "Tie! 🤝 — Computer: Nice game!",
        "Tie! 🤝"
    ]

    if user_idx == cpu_idx:
        result.config(text=tie_msgs[user_idx], fg="#f39c12")
        ties += 1

    elif (user_idx == 0 and cpu_idx == 2) or \
         (user_idx == 1 and cpu_idx == 0) or \
         (user_idx == 2 and cpu_idx == 1):

        result.config(text=win_msgs[user_idx], fg="#27ae60")
        wins += 1

    else:
        result.config(text=lose_msgs[user_idx], fg="#e74c3c")
        losses += 1

    score_labels["WINS"].config(text=str(wins))
    score_labels["TIES"].config(text=str(ties))
    score_labels["LOSSES"].config(text=str(losses))

Button(root, text="SPIN!", font=("Arial", 14, "bold"),
       bg="#e74c3c", fg="white", relief="flat",
       padx=30, pady=8, cursor="hand2",
       command=spin).pack(pady=5)

root.mainloop()
