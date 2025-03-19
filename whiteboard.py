from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk

# Initialize main window
root = Tk()
root.title("WHITEBOARD")
root.geometry("1050x570+130+50")
root.resizable(False, False)

curr_x = 0
curr_y = 0
c = "black"
is_eraser = False  # Flag for eraser mode

# Functions
def locate_xy(work):
    global curr_x, curr_y
    curr_x = work.x
    curr_y = work.y

def addline(work):
    global curr_x, curr_y, c, is_eraser
    color = "white" if is_eraser else c  # Use white for eraser mode
    can.create_line(
        (curr_x, curr_y, work.x, work.y),
        width=get_val(),
        fill=color,
        capstyle=ROUND,
        smooth=True,
    )
    curr_x, curr_y = work.x, work.y

def show(new):
    global c, is_eraser
    is_eraser = False  # Disable eraser when selecting a color
    c = new

def ncan():
    can.delete("all")  # Clear the drawing area but keep the color palette

def toggle_eraser():
    global is_eraser
    is_eraser = True  # Enable eraser mode

def reset_canvas():
    """Reset the canvas and all settings."""
    global c, is_eraser
    ncan()  # Clear the canvas
    is_eraser = False
    c = "black"  # Reset color to black
    slider.set(5)  # Reset thickness slider to default
    vallab.configure(text=get_val())  # Update label

# Load images
logo = PhotoImage(file="whiteboard.png")
eraser_image = Image.open("eraser.png")
eraser_icon = ImageTk.PhotoImage(eraser_image.resize((30, 30)))
reset_image = Image.open("reset.png")
reset_icon = ImageTk.PhotoImage(reset_image.resize((30, 30)))
panel_image = PhotoImage(file="panel.png")
root.iconphoto(False, logo)

# Widgets
Label(root, image=panel_image, bg="#f2f3f5").place(x=10, y=20)
Button(root, image=eraser_icon, bg="#f2f3f5", width=30, height=30, command=toggle_eraser).place(x=30, y=420)
Button(root, image=reset_icon, bg="#f2f3f5", width=30, height=25, command=reset_canvas).place(x=30, y=460)

colours = Canvas(root, bg="light grey", width=39, height=350, bd=0)
colours.place(x=30, y=60)

can = Canvas(root, bg="white", width=930, height=500, cursor="hand2")
can.place(x=100, y=10)
can.bind("<Button-1>", locate_xy)
can.bind("<B1-Motion>", addline)

# Color palette function
def colp():
    colors = [
        ("black", 10, 10, 30, 30),
        ("gray", 10, 40, 30, 60),
        ("brown4", 10, 70, 30, 90),
        ("red", 10, 100, 30, 120),
        ("orange", 10, 130, 30, 150),
        ("yellow", 10, 160, 30, 180),
        ("blue", 10, 190, 30, 210),
        ("purple", 10, 220, 30, 240),
        ("pink", 10, 250, 30, 270),
        ("cyan", 10, 280, 30, 300),
        ("green", 10, 310, 30, 330),
    ]
    for color, x1, y1, x2, y2 in colors:
        rect_id = colours.create_rectangle(x1, y1, x2, y2, fill=color)
        colours.tag_bind(rect_id, "<Button-1>", lambda event, c=color: show(c))

colp()

# Slider for line thickness
val = tk.DoubleVar()

def get_val():
    return round(val.get(), 2)

def slidech(event):
    vallab.configure(text=get_val())

slider = ttk.Scale(root, from_=1, to=50, orient="horizontal", command=slidech, variable=val)
slider.place(x=30, y=530)

vallab = ttk.Label(root, text=get_val())
vallab.place(x=27, y=550)

# Initialize slider value
slider.set(5)  # Set default thickness
vallab.configure(text=get_val())

root.mainloop()
