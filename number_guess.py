from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Number Guessing Game")
root.configure(bg="#f0f4f8")

secret_number = None
attempts = 0

Label(root, text="Number Guessing Game",
      font=("Arial", 20, "bold"), bg="#f0f4f8", fg="#333").pack(pady=20)

instruction = Label(root, text="Player 1: Enter a secret number",
                    font=("Arial", 12), bg="#f0f4f8", fg="#777")
instruction.pack()

entry = Entry(root, font=("Arial", 18), justify="center",
              width=10, relief="flat", bg="#dce3ea", fg="#333")
entry.pack(pady=15, ipady=8)
entry.focus()

feedback = Label(root, text="",
                 font=("Arial", 12, "bold"), bg="#f0f4f8", fg="#555")
feedback.pack(pady=5)

attempts_label = Label(root, text="Attempts: 0",
                       font=("Arial", 11), bg="#f0f4f8", fg="#999")
attempts_label.pack()

btn = Button(root, text="Set Number",
             font=("Arial", 13, "bold"),
             bg="#3498db", fg="white", relief="flat",
             padx=25, pady=8, cursor="hand2")
btn.pack(pady=20)

def set_number():
    global secret_number, attempts
    val = entry.get().strip()

    if not val.isdigit():
        feedback.config(text="Please enter a valid number!", fg="#e74c3c")
        return

    secret_number = int(val)
    attempts = 0
    entry.delete(0, END)
    instruction.config(text="Player 2: Guess the number")
    feedback.config(text="Player 2: Start guessing!", fg="#27ae60")
    attempts_label.config(text="Attempts: 0")
    btn.config(text="Guess", bg="#27ae60", command=guess)
    entry.focus()

def guess():
    global attempts
    val = entry.get().strip()

    if not val.isdigit():
        feedback.config(text="Please enter a valid number!", fg="#e74c3c")
        return

    attempts += 1
    number = int(val)
    entry.delete(0, END)
    attempts_label.config(text=f"Attempts: {attempts}")

    if number > secret_number:
        feedback.config(text="📈 Too High! Try lower.", fg="#e74c3c")
    elif number < secret_number:
        feedback.config(text="📉 Too Low! Try higher.", fg="#3498db")
    else:
        feedback.config(text=f"🎉 Correct! You got it in {attempts} attempts!", fg="#27ae60")
        btn.config(text="Play Again", bg="#e74c3c", command=play_again)

def play_again():
    global secret_number, attempts
    secret_number = None
    attempts = 0
    entry.delete(0, END)
    instruction.config(text="Player 1: Enter a secret number")
    feedback.config(text="")
    attempts_label.config(text="Attempts: 0")
    btn.config(text="Set Number", bg="#3498db", command=set_number)
    entry.focus()

btn.config(command=set_number)
root.bind("<Return>", lambda e: btn.invoke())

root.mainloop()
