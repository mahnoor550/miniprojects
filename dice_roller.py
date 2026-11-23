import tkinter as tk
import random

dice_colors = ["#ff6b6b", "#4dabf7", "#51cf66", "#ffd43b", "#cc5de8", "#ff922b"]

faces = {
    1: ["     ", "  ●  ", "     "],
    2: ["●    ", "     ", "    ●"],
    3: ["●    ", "  ●  ", "    ●"],
    4: ["● ●", "     ", "● ●"],
    5: ["● ●", "  ●  ", "● ●"],
    6: ["● ●", "● ●", "● ●"]
}

window = tk.Tk()
window.title("Dice Roller")
window.geometry("400x550")
window.configure(bg="#10131a")
window.resizable(True, True)

title = tk.Label(
    window,
    text="DICE ROLLER",
    font=("Arial", 20, "bold"),
    bg="#10131a",
    fg="white"
)
title.pack(pady=(20, 5))

subtitle = tk.Label(
    window,
    text="Roll the dice and test your luck",
    font=("Arial", 12),
    bg="#10131a",
    fg="#9aa0aa"
)
subtitle.pack(pady=(0, 10))

dice = tk.Frame(
    window,
    width=200,
    height=200,
    bg="#ff6b6b",
    highlightbackground="#ffffff",
    highlightthickness=3
)
dice.pack(pady=10)
dice.pack_propagate(False)

face_label = tk.Label(
    dice,
    text="●",
    font=("Arial", 40, "bold"),
    bg="#ff6b6b",
    fg="white",
    justify="center"
)
face_label.place(relx=0.5, rely=0.5, anchor="center")

result = tk.Label(
    window,
    text="Ready to roll?",
    font=("Arial", 20, "bold"),
    bg="#10131a",
    fg="white"
)
result.pack(pady=20)

roll_button = tk.Button(
    window,
    text="🎲  ROLL DICE",
    font=("Arial", 16, "bold"),
    bg="#ffffff",
    fg="#10131a",
    activebackground="#dddddd",
    relief="flat",
    cursor="hand2",
    padx=40,
    pady=10
)
roll_button.pack(pady=15)

rolling = False
animation_count = 0

def show_face(number, color):
    dice.config(bg=color)
    face_label.config(
        text="\n".join(faces[number]),
        bg=color,
        fg="white"
    )

def animate_dice():
    global animation_count

    number = random.randint(1, 6)
    color = random.choice(dice_colors)

    show_face(number, color)

    animation_count += 1

    if animation_count < 15:
        window.after(80, animate_dice)
    else:
        finish_roll()

def finish_roll():
    global rolling, animation_count

    final_number = random.randint(1, 6)
    final_color = dice_colors[final_number - 1]

    show_face(final_number, final_color)

    result.config(
        text=f"You rolled: {final_number}"
    )

   
    rolling = False
    animation_count = 0
    roll_button.config(
        state="normal",
        text="🎲  ROLL DICE"
    )

def roll_dice():
    global rolling

    if rolling:
        return

    rolling = True
    animation_count = 0

    roll_button.config(
        state="disabled",
        text="ROLLING..."
    )

    animate_dice()

roll_button.config(command=roll_dice)

window.mainloop()