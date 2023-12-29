import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
from io import BytesIO
import requests
screen = tk.Tk()
screen.title('Disappearing-Text app!')
screen.geometry('800x600')
screen.configure(bg="lightblue")

def starting():
    def clear_screen():
        # Remove all widgets from the screen
        for widget in screen.winfo_children():
            widget.pack_forget()

    
    entry = tk.Text(screen, width=50, height=10)  # Adjust width and height as desired
    entry.pack()

    custom_font = font.Font(family="Arial", size=13, slant="italic")  # Define custom font

   
    def action():
        clear_screen()
        screen.configure(bg='red')
        ending = tk.Label(bg='red', text="Oops, you lost your work because you were too slow!")
        ending.pack()

        # Download the GIF from the URL
    typing_delay = 5000  # 5 seconds
    typing_after_id = None  # To store the after callback identifier

    def check_typing():
        global typing_after_id  # Use the global variable to store the after callback identifier
        current_text = entry.get("1.0", "end-1c")  # Retrieve all text in the Text widget
        if current_text != check_typing.last_text:
            # User is still typing
            check_typing.last_text = current_text
            typing_after_id = screen.after(typing_delay, check_typing)  # Reschedule the after callback
        else:
            action()  # Call the action function
            print("User has stopped typing.")

    entry.bind("<Key>", lambda event: reschedule_check_typing(event))

    def reschedule_check_typing(event):
        nonlocal typing_after_id  # Use the global variable to cancel the after callback
        if typing_after_id is not None:
            screen.after_cancel(typing_after_id)  # Cancel the existing after callback
        typing_after_id = screen.after(typing_delay, check_typing)  # Reschedule the after callback

    check_typing.last_text = entry.get("1.0", "end-1c")
    typing_after_id = screen.after(typing_delay, check_typing)


label = tk.Label(text='You want to work fast and productive?! Your whole text will disappear,\nif you stop typing for more than 5 seconds!', bg='lightblue', font=("Arial", 13, "bold italic"))
label.pack()

button = tk.Button(text='Start', command=starting)
button.pack()

screen.mainloop()

