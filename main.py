import tkinter as tk

window = tk.Tk()
window.title("Main Branch")
window.geometry("300x150")

click_button = tk.Button(
    text="Generate!",
    width=10,
    height=2
)

window.mainloop()