import tkinter as tk
import random

def change_background_color():
    redish = random.randint(0, 220)
    greenish = random.randint(0, 230)
    blueish = random.randint(0, 240)
    
    hex_color = f'#{redish:02x}{greenish:02x}{blueish:02x}'
    
    window.config(bg=hex_color)

window = tk.Tk()
window.title("Color generator")
window.geometry("500x500")

click_button = tk.Button(
    text="Generate!",
    width=10,
    height=2,
    command=change_background_color
)

click_button.pack(side=tk.BOTTOM, pady=20)
window.mainloop()
