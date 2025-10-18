import tkinter as tk

window = tk.Tk()
window.title("Main Branch")
window.geometry("300x150")

click_button = tk.Button(
    text="Generate!",
    width=10,
    height=2
)


click_button.pack(side=tk.BOTTOM, pady=20)
window.mainloop()