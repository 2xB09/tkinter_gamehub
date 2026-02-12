import tkinter as tk
import random

def number_guessing_game():
    root.withdraw()

    screen = tk.Toplevel()
    screen.title("Number Guessing Game")
    screen.configure(bg="lightgreen")

    number = random.randint(1, 100)
    attempts = 0

    instruction_label = tk.Label(screen, text="Guess a number between 1 and 100", font=("Arial", 16), bg="lightgreen")
    instruction_label.grid(row=0, column=0, columnspan=2, pady=10)

    entry = tk.Entry(screen, font=("Arial", 16))
    entry.grid(row=1, column=0, columnspan=2, pady=10)

    result_label = tk.Label(screen, text="", font=("Arial", 14), bg="lightgreen")
    result_label.grid(row=2, column=0, columnspan=2, pady=10)

    attempts_label = tk.Label(screen, text=f"Attempts: {attempts}", font=("Arial", 14), bg="lightgreen")
    attempts_label.grid(row=3, column=0, columnspan=2, pady=10)

    def check_guess():
        try:
            guess = int(entry.get())
            if guess < 1 or guess > 100:
                result_label.config(text="Please enter a number between 1 and 100.", fg="red")
                return
        except ValueError:
            result_label.config(text="Invalid input! Please enter a number.", fg="red")
            return
        
        nonlocal attempts
        attempts += 1
        attempts_label.config(text=f"Attempts: {attempts}")

        if guess < number:
            result_label.config(text="Too low! Try again.", fg="red")
        elif guess > number:
            result_label.config(text="Too high! Try again.", fg="red")
        else:
            result_label.config(text="Congratulations! You guessed it right.", fg="green")

    guess_button = tk.Button(screen, text="Guess", font=("Arial", 16), command=check_guess)
    guess_button.grid(row=4, column=0, columnspan=2, pady=10)

    def exit_game():
        screen.destroy()
        root.deiconify()

    def reset():
        nonlocal number
        number = random.randint(1, 100)
        nonlocal attempts
        attempts = 0
        attempts_label.config(text=f"Attempts: {attempts}")
        result_label.config(text="")
        entry.delete(0, tk.END)

    reset_button = tk.Button(screen, text="Reset", font=("Arial", 16), command=reset)
    reset_button.grid(row=5, column=0, sticky='w', columnspan=2, padx=10,pady=10)

    exit_button = tk.Button(screen, text="Exit Game", font=("Arial", 16), command=exit_game)
    exit_button.grid(row=5, column=0, sticky='e', columnspan=2, padx=10, pady=10)


def four_corners_game():
    root.withdraw()

    wins = 0
    losses = 0

    screen = tk.Toplevel()
    screen.title("Four Corners Game")
    screen.configure(bg="lightyellow")

    instruction_label = tk.Label(screen, text='Select a corner to play!', font=("Arial", 16), bg="lightyellow")
    instruction_label.grid(row=0, column=0, columnspan=3, pady=10)

    bad_corner = random.randint(1, 4)

    def corner_clicked(corner):
        blue_corner.config(state='disabled')
        red_corner.config(state='disabled')
        green_corner.config(state='disabled')
        orange_corner.config(state='disabled')

        if corner == bad_corner:
            instruction_label.config(text="You clicked the bad corner! Reset to play again.", fg="red")
            nonlocal losses
            losses += 1
            losses_label.config(text=f"Losses: {losses}")
        else:
            instruction_label.config(text="Safe corner! Reset to play again.", fg="green")
            nonlocal wins
            wins += 1
            wins_label.config(text=f"Wins: {wins}")

    blue_corner = tk.Button(screen, text='   ', font=("Arial", 16), bg="blue", command=lambda: corner_clicked(1))
    blue_corner.grid(row=1, column=0, sticky='ne')

    red_corner = tk.Button(screen, text='   ', font=("Arial", 16), bg="red", command=lambda: corner_clicked(2))
    red_corner.grid(row=1, column=1, sticky='nw')

    green_corner = tk.Button(screen, text='   ', font=("Arial", 16), bg="green", command=lambda: corner_clicked(3))
    green_corner.grid(row=2, column=0, sticky='se')

    orange_corner = tk.Button(screen, text='   ', font=("Arial", 16), bg="orange", command=lambda: corner_clicked(4))
    orange_corner.grid(row=2, column=1, sticky='sw')

    def exit():
        screen.destroy()
        root.deiconify()
    
    def reset():
        blue_corner.config(state='normal')
        red_corner.config(state='normal')
        green_corner.config(state='normal')
        orange_corner.config(state='normal')

        nonlocal bad_corner
        bad_corner = random.randint(1, 4)
        instruction_label.config(text='Select a corner to play!', fg="black")

    losses_label = tk.Label(screen, text=f"Losses: {losses}", font=("Arial", 14), bg="lightyellow", fg='red')
    losses_label.grid(row=3, column=0, sticky='w', pady=10)

    wins_label = tk.Label(screen, text=f"Wins: {wins}", font=("Arial", 14), bg="lightyellow", fg='green')
    wins_label.grid(row=3, column=1, sticky='e', pady=10)

    reset_button = tk.Button(screen, text="Reset", font=("Arial", 16), command=reset)
    reset_button.grid(row=4, column=0, sticky='w', columnspan=3, padx=10,pady=10)

    exit_button = tk.Button(screen, text="Exit Game", font=("Arial", 16), command=exit)
    exit_button.grid(row=4, column=0, sticky='e',columnspan=3, pady=10)

root = tk.Tk()
root.title("Game Hub")
root.configure(bg="lightblue")

title_label = tk.Label(root, text="Welcome to my Game Hub!", font=("Arial", 24), bg="lightblue")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

game1_button = tk.Button(root, text="Number Guessing Game", font=("Arial", 16), command=number_guessing_game)
game1_button.grid(row=1, column=0, sticky='nsew', columnspan=2, padx=20, pady=10)

game2_button = tk.Button(root, text="Four Corners Game", font=("Arial", 16), command=four_corners_game)
game2_button.grid(row=2, column=0, sticky='nsew', columnspan=2, padx=20, pady=10)

game3_button = tk.Button(root, text='To be continued. . .', font=("Arial", 16), state='disabled')
game3_button.grid(row=3, column=0, sticky='nsew', columnspan=2, padx=20, pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 16), command=root.quit)
exit_button.grid(row=100, column=0, sticky='nsew', columnspan=2, padx=20, pady=10)


root.mainloop()