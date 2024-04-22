import random
import tkinter as tk
from tkinter import messagebox

def play_game():
    global eerste_getal, score
    h_of_l = user_input.get().lower()
    
    tweede_getal = random.randint(0, 10)
    result_label.config(text=f"Het tweede getal is: {tweede_getal}")

    if h_of_l == "lager":
        if tweede_getal <= eerste_getal:
            score += 1
            result_label.config(text="Verder spelen")
        else:
            end_game()
    elif h_of_l == "hoger":
        if tweede_getal >= eerste_getal:
            score += 1
            result_label.config(text="Verder spelen")
        else:
            end_game()

    score_label.config(text=f"Jouw score is: {score}")
    eerste_getal = tweede_getal

def end_game():
    global mag_verderspelen
    mag_verderspelen = False
    result_label.config(text="Verloren")
    messagebox.showinfo("Game Over", f"Je score is: {score}")
    root.destroy()

# Variables
mag_verderspelen = True
eerste_getal = random.randint(0, 10)
score = 0

# Main GUI window
root = tk.Tk()
root.title("Hoger of Lager")

# GUI components
tk.Label(root, text=f"Het eerste getal is: {eerste_getal}").pack()
tk.Label(root, text="Is het volgende getal hoger of lager?").pack()
user_input = tk.Entry(root)
user_input.pack()
result_label = tk.Label(root, text="")
result_label.pack()
score_label = tk.Label(root, text=f"Jouw score is: {score}")
score_label.pack()
play_button = tk.Button(root, text="Speel", command=play_game)
play_button.pack()

# Run the GUI
root.mainloop()