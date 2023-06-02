import tkinter as tk

def button_click():
    print("Button clicked!")

# Create the main window
window = tk.Tk()

# Create a button widget
button = tk.Button(window, text="exit", command=button_click)

# Add the button to the window
button.pack()

# Start the Tkinter event loop
window.mainloop()


