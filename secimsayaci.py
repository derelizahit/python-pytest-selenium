import tkinter as tk
from datetime import datetime

SECIM_GUNU = datetime(2023, 5, 14, 8, 0, 0)

def countdown():
    current_date = datetime.now()
    remaining_time = SECIM_GUNU - current_date
    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    countdown_label.config(text=f"{days} gün, {hours} saat, {minutes} dakika, {seconds} saniye kaldı")
    countdown_label.after(1000, countdown)


root = tk.Tk()
root.title("SEÇİM SAYACI 14 MAYIS 2023")

countdown_label = tk.Label(root, font=("Impact",24))
countdown_label.pack(padx=20, pady=20)

countdown()

root.mainloop()
