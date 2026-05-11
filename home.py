from tkinter import *
import subprocess
import sys
import os

# --- Make sure games run from the same folder ---
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# --- Home Screen ---
root = Tk()
root.geometry("400x500")
root.title("🎮 Select The Game")
root.configure(bg="#f0f4f8")
root.resizable(False, False)

# --- Title ---
Label(root, text="🎮 Select The Game",
      font=("Arial", 24, "bold"), bg="#f0f4f8", fg="#333").pack(pady=30)

Label(root, text="Choose a game to play",
      font=("Arial", 12), bg="#f0f4f8", fg="#777").pack()

# --- Launch Function ---
def launch(filename):
    subprocess.Popen([sys.executable, filename])

# --- Game Cards ---
games_info = [
    ("🪨  Rock Paper Scissors", "#e74c3c", "rock_paper_scissors.py", "1 player · Pick your weapon"),
    ("🔢  Number Guessing",     "#3498db", "number_guess.py",         "2 players · Set & guess"),
    ("✏️  Tic Tac Toe",          "#27ae60", "tic_tac_toe.py",          "2 players · Get 3 in a row"),
]

for title, color, filename, desc in games_info:
    # Colored card
    card = Frame(root, bg=color)
    card.pack(padx=40, pady=10, fill=X)

    Label(card, text=title, font=("Arial", 13, "bold"),
          bg=color, fg="white").pack(side=LEFT, padx=16, pady=14)

    Button(card, text="Play ▶", font=("Arial", 10, "bold"),
           bg="white", fg=color, relief="flat",
           padx=10, pady=4, cursor="hand2",
           command=lambda f=filename: launch(f)).pack(side=RIGHT, padx=12, pady=10)

    # Description bar below
    Label(root, text=desc, font=("Arial", 9),
          bg="#e8ecef", fg="#777", anchor="w").pack(fill=X, padx=40, ipady=4, ipadx=16)

# --- Footer ---
Label(root, text="Made With Love By Aryan,Piyush and Niyati",
      font=("Arial", 12), bg="#f0f4f8", fg="#bbb").pack(pady=25)

root.mainloop()
