import tkinter as tk
import random
import pygame  # enables sound effects

# Initialized pygame for sound
pygame.mixer.init()

# Funny messages
messages = [
    "I'm on a break. Try again later.",
    "Reading... Just kidding, I do nothing!",
    "Error 404: Functionality not found.",
    "Ha!Ha! That tickles!",
    "Assignment accomplished: Nothing happened.",
    "Stop clicking me! 😡",
    "You really thought I’d do something, huh?"
]

# List of colors
colors = ["red", "blue", "green", "purple", "orange", "pink", "yellow"]

click_count = 0  # Track number of clicks

def play_sound():

    #Plays a funny click sound
    pygame.mixer.Sound("click.mp3").play()

def move_window():

    #Moves the window slightly
    x = root.winfo_x() + random.randint(-50, 50)
    y = root.winfo_y() + random.randint(-50, 50)
    root.geometry(f"350x250+{x}+{y}")

def run_away(event):
    #Move button to random position when hovered
    x = random.randint(20, 280)
    y = random.randint(20, 180)
    button.place(x=x, y=y)

def on_click():
    #Changes button message text, color, move window, and play sound
    global click_count
    click_count += 1
    button.config(text=random.choice(messages), fg=random.choice(colors))
    move_window()
    play_sound()

    # Randomly close the app after a few clicks
    if click_count > 5 and random.random() < 0.3:  # 30% chance after 5 clicks
        root.destroy()

# Creates the main window
root = tk.Tk()
root.title("Fun Press")
root.geometry("350x250")

# Creates a button
button = tk.Button(root, text="Click Me!", font=("Arial", 14), command=on_click)
button.place(x=100, y=80)

# Makes the button run away when hovered
button.bind("<Enter>", run_away)

root.mainloop()
