from tkinter import *

# Create the window
window = Tk()

# Name the window
window.title("Welcome to test app")

# set window default size
window.geometry('350x200')

# add a label widget
lbl = Label(window, text = "Hello", bg = "Blue", fg = "Yellow", font = ("Monotype Cursiva", 14))

# display the widget
lbl.grid(column = 0, row = 0)

# set click event
def clicked():
	lbl.configure(text = "Button clicked")
	
# add a button widget
btn = Button(window, text = "Click me", bg = "Orange", fg = "Red", command = clicked)

# display button
btn.grid(column = 1, row = 0)

# start the main loop for user interaction
window.mainloop()