import random
#import os
import shelve
import tkinter as tk
from playsound import playsound

playsound("C:\\Users\\K.Ren Westin\\Desktop\\prog\\ffxiv_gui\\ff7prelude.mp3", block=False)

healers = ["Sage", "Astrologian", "White Mage", "Scholar"]
tanks = ["Dark Knight", "Warrior", "Gunbreaker", "Paladin"]
magical_dps = ["Black Mage", "Red Mage", "Summoner"]
r_physical_dps = ["Machinist", "Bard"]
melee = ["Monk", "Ninja", "Samurai", "Reaper"]
jobs = []
temp = " "

with shelve.open("jobs_db") as db:
    if "jobs" in db:
        temp = db["jobs"]
        print("Previous jobs are", temp)


def tank_click():
    temp = random.choice(tanks)
    result_label.config(text=f"Your new tank job is {temp}")
    jobs.append(temp)


def healer_click():
    temp = random.choice(healers)
    result_label.config(text=f"Your new healer job is {temp}")
    jobs.append(temp)


def magic_dps_click():
    temp = random.choice(magical_dps)
    result_label.config(text=f"Your new dps job is {temp}")
    jobs.append(temp)


def physical_dps_click():
    temp = random.choice(r_physical_dps)
    result_label.config(text=f"Your new physical ranged dps job is {temp}")
    jobs.append(temp)


def melee_click():
    temp = random.choice(melee)
    result_label.config(text=f"Your new melee job is {temp}")
    jobs.append(temp)


def all_jobs_result_click():
    temp = ", ".join(jobs)
    result_label.config(text=f"{temp}")


#def play_music():
#    playsound(
#        "C:\\Users\\K.Ren Westin\\Desktop\\prog\\ffxiv_gui\\ffxiv_gui_new\\ff7prelude.mp3", block=False)


def exit_click():
    with shelve.open("jobs_db", "n") as db:
        db["jobs"] = (", ".join(jobs))
    window.destroy()


window = tk.Tk()
window.title("FFXIV Job Finder")
window.geometry("800x300")
window.configure(bg="gray")

previous_result_label = tk.Label(text=f"Previously selected jobs are: {temp}", font=(
    "Comic Sans MS", 11, "bold"), bg="gray")
previous_result_label.pack()

result_label = tk.Label(text="", font=("Comic Sans MS", 20), bg="gray")
result_label.pack()

tank_button = tk.Button(text="Tank", fg="blue", font=(
    "Helvetica", 16), height=2, width=10, command=tank_click)
tank_button.place(x=5, y=100)
# tank_button.pack()

healer_button = tk.Button(text="Healer", fg="green", font=(
    "Helvetica", 16), height=2, width=10, command=healer_click)
healer_button.place(x=165, y=100)
# healer_button.pack()

magic_dps_button = tk.Button(
    text="Magical\n DPS", fg="red", font=(
        "Helvetica", 16), height=2, width=10, command=magic_dps_click)
magic_dps_button.place(x=330, y=100)
# magic_dps_button.pack()

physical_dps_button = tk.Button(
    text="Physical\n Ranged DPS", fg="red", font=(
        "Helvetica", 16), height=2, width=11, command=physical_dps_click)
physical_dps_button.place(x=500, y=100)
# physical_dps_button.pack()

melee_button = tk.Button(text="Melee DPS", fg="red", font=(
    "Helvetica", 16), height=2, width=10, command=melee_click)
melee_button.place(x=665, y=100)
# melee_button.pack()

all_jobs_result_button = tk.Button(
    text="All jobs", font=(
        "Helvetica", 16), height=2, width=10, command=all_jobs_result_click)
all_jobs_result_button.place(x=330, y=210)
# all_jobs_result_button.pack()

exit_button = tk.Button(text="Exit", font=(
    "Helvetica", 12), height=1, width=4, command=exit_click)
exit_button.place(x=745, y=260)
# exit_button.pack()

#music_button = tk.Button(text="Play Music", font=(
#    "Helvetica", 12), height=1, width=4, command=play_music)
#music_button.place(x=710, y=260)

window.mainloop()
