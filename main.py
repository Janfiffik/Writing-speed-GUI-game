# _______Imports_____
import json
from tkinter import *
from tkinter.font import Font
from time import time
import random
import player as pl


# list for random words. And random string generator
random_text_list = ["Hello there!", "How are you?", "I'm here too.", "Time to chat.",
                    "Let's begin.", "What's up?", "Nice to meet.", "Feeling good?",
                    "Ready to talk.", "Here we go.", "Tell me more.", "I'm all ears."
                    ]


def random_text(text_list):
    global ran_text_string
    ran_text_string = ""
    for _ in text_list:
        ran_words = random.choice(text_list)
        ran_text_string += f"{ran_words}\n"
        text_list.remove(ran_words)

    return ran_text_string

# ______________FUNCTIONS_______________


def get_text():
    global start, end

    old_text = ran_text_string.replace("\n", " ")
    new_text = entry_string.get("1.0", "end").replace("\n", " ")
    if old_text == new_text:
        end = time()
        new_score = int(end-start)
        resultLabel = Label(text=f"Your score is: {int(end-start)} seconds.", fg="orange", font=Font(size=15))
        resultLabel.grid(row=7, column=1)
        with open("players_list.json", "r") as file:
            data = json.load(file)

        if new_score < data[name]:
            player = pl.Player(name, new_score)
            player.append_to_file("players_list.json")

    else:
        resultLabel = Label(text=f"Not the same. You need correct your answers.\n"
                                 f"Time is running!!!!", fg="red", font=Font(size=15))
        resultLabel.grid(row=7, column=1)
        root.after(2000, lambda: resultLabel.destroy())


def countdown():
    timer_text = Label(text=f"Timer: 3", bg="grey", fg="red", font=Font(size=25))
    timer_text.grid(column=1, row=3)
    root.after(1000, lambda: timer_text.configure(text=f"Timer: 2"))
    root.after(2000, lambda: timer_text.configure(text=f"Timer: 1"))
    root.after(3000, lambda: timer_text.destroy())


def gameplay(player):
    global start
    global entry_string
    name = player.name
    score = player.score
    gameplay_label = Label(text=f"Player: {name}\nShortest time: {score}.seconds",
                           fg="red", bg="grey", font=Font(size=15))
    gameplay_label.grid(row=2, column=1)
    countdown()
    string_to_write = Label(text=random_text(random_text_list), font=Font(size=15), fg="green",
                            width=20, height=7)
    string_to_write.grid(row=4, column=1)
    root.update()

    entry_string = Text(font=Font(size=15), width=21, height=7, fg='blue', name="get_str", )
    root.after(3000, lambda: entry_string.focus())
    entry_string.grid(row=5, column=1)
    start = time()+3

    entryButton = Button(text="OK", command=get_text, font=Font(size=20))
    entryButton.grid(row=6, column=1, pady=10, padx=10)


def add_player():
    global player, name, data

    name = name_input_window.get()
    with open("players_list.json", "r") as file:
        data = json.load(file)
        if name not in data.keys():
            player = pl.Player(name, 100)
            player.create_player()
            player.append_to_file("players_list.json")
            new_player = Label(text=f"Player {name} added to game.", bg="grey", font=Font(size=18))
            new_player.grid(row=1, column=1)
            root.after(3000, lambda: new_player.destroy())
            root.after(3500, lambda: gameplay(player))
        else:
            player = pl.Player(name, data[name])
            root.after(3000, lambda: gameplay(player))

# Set window dimensions and background color
root = Tk()
root.title("Typing speed test")
root.geometry("800x600")
root.configure(bg="grey")


# Create player and add to txt list
player_name = Label(text="New/Existing player:", bg="grey", font=Font(size=20))
player_name.grid(row=0, column=0)

name_input_window = Entry(font=Font(size=20))
name_input_window.grid(row=0, column=1, padx=15)

okButton = Button(text="game start/new", padx=15, command=add_player, font=Font(size=20))
okButton.grid(row=0, column=3)


root.mainloop()
