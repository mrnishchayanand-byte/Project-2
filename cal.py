from tkinter import *
import math

root = Tk()
root.title("Advanced Scientific Calculator")
root.geometry("750x420")
root.configure(bg="white")
button_bg = "#1a1a1a"
button_fg = "white"
sci_bg = "#333333"

def key_event(event):
    global expr

    char = event.char
    key = event.keysym

def backspace():
    global expr
    expr = expr[:-1]
    display.set(expr)


    # Numbers
    if char.isdigit():
        press(char)

    # Operators
    elif char in "+-*/.":
        press(char)

    # Parentheses
    elif char in "()":
        press(char)

    # Enter = equals
    elif key == "Return":
        equal()

    # Backspace
    elif key == "BackSpace":
        expr = expr[:-1]
        display_var.set(expr)

    # Esc = clear
    elif key == "Escape":
        clear()

    # ^ → **
    elif char == "^":
        press("**")
root.bind("<Key>", key_event)
# ---------------- DISPLAY -----------------
display = StringVar()
entry = Entry(root, textvariable=display, font=("Arial", 20), bg="black", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=5, ipadx=80, ipady=15, padx=10, pady=10)
expr = ""
history_list = []

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr, {"__builtins__": None}, math.__dict__))
        display.set(result)
        add_history(expr + " = " + result)
        expr = result
    except:
        display.set("error")
        expr = ""

def equal2():
    equal()  

def clear():
    global expr
    expr = ""
    display.set("")

def add_history(item):
    history_list.append(item)
    history_box.insert(END, item)

# ---------------- HISTORY PANEL -----------------
history_label = Label(root, text="History", fg="white", bg="black", font=("Arial", 14))
history_label.grid(row=0, column=6)

history_box = Listbox(root, height=18, width=30, bg="#111111", fg="white", font=("Arial", 10))
history_box.grid(row=1, column=6, rowspan=6, padx=10)

# --------------- SCIENTIFIC BUTTONS -----------------
Button(root, text='sin', bg=sci_bg, fg=button_fg, command=lambda: press("sin("), width=7).grid(row=1, column=0)
Button(root, text='cos', bg=sci_bg, fg=button_fg, command=lambda: press("cos("), width=7).grid(row=1, column=1)
Button(root, text='tan', bg=sci_bg, fg=button_fg, command=lambda: press("tan("), width=7).grid(row=1, column=2)
Button(root, text='log', bg=sci_bg, fg=button_fg, command=lambda: press("log("), width=7).grid(row=1, column=3)
Button(root, text='ln', bg=sci_bg, fg=button_fg, command=lambda: press("log("), width=7).grid(row=1, column=4)

Button(root, text='√', bg=sci_bg, fg=button_fg, command=lambda: press("sqrt("), width=7).grid(row=2, column=0)
Button(root, text='x²', bg=sci_bg, fg=button_fg, command=lambda: press("**2"), width=7).grid(row=2, column=1)
Button(root, text='^', bg=sci_bg, fg=button_fg, command=lambda: press("**"), width=7).grid(row=2, column=2)
Button(root, text='π', bg=sci_bg, fg=button_fg, command=lambda: press("pi"), width=7).grid(row=2, column=3)
Button(root, text='e', bg=sci_bg, fg=button_fg, command=lambda: press("e"), width=7).grid(row=2, column=4)
Button(root, text="sin⁻¹", bg=sci_bg, fg=button_fg, command=lambda: press("asin("), width=7).grid(row=1,column=5)
Button(root, text="cos⁻¹", bg=sci_bg, fg=button_fg, command=lambda: press("acos("), width=7).grid(row=2,column=5)
Button(root, text="tan⁻¹", bg=sci_bg, fg=button_fg, command=lambda: press("atan("), width=7).grid(row=3,column=5)
Button(root, text="←", bg=sci_bg, fg=button_fg, command=backspace, width=7).grid(row=4, column=5)




# --------------- NUMBER ROWS -----------------
Button(root, text='7', bg=button_bg, fg=button_fg, command=lambda: press(7), width=7).grid(row=3, column=0)
Button(root, text='8', bg=button_bg, fg=button_fg, command=lambda: press(8), width=7).grid(row=3, column=1)
Button(root, text='9', bg=button_bg, fg=button_fg, command=lambda: press(9), width=7).grid(row=3, column=2)
Button(root, text='/', bg=button_bg, fg=button_fg, command=lambda: press("/"), width=7).grid(row=3, column=3)
Button(root, text='(', bg=sci_bg, fg=button_fg, command=lambda: press("("), width=7).grid(row=3, column=4)

Button(root, text='4', bg=button_bg, fg=button_fg, command=lambda: press(4), width=7).grid(row=4, column=0)
Button(root, text='5', bg=button_bg, fg=button_fg, command=lambda: press(5), width=7).grid(row=4, column=1)
Button(root, text='6', bg=button_bg, fg=button_fg, command=lambda: press(6), width=7).grid(row=4, column=2)
Button(root, text='*', bg=button_bg, fg=button_fg, command=lambda: press("*"), width=7).grid(row=4, column=3)
Button(root, text=')', bg=sci_bg, fg=button_fg, command=lambda: press(")"), width=7).grid(row=4, column=4)

Button(root, text='1', bg=button_bg, fg=button_fg, command=lambda: press(1), width=7).grid(row=5, column=0)
Button(root, text='2', bg=button_bg, fg=button_fg, command=lambda: press(2), width=7).grid(row=5, column=1)
Button(root, text='3', bg=button_bg, fg=button_fg, command=lambda: press(3), width=7).grid(row=5, column=2)
Button(root, text='-', bg=button_bg, fg=button_fg, command=lambda: press("-"), width=7).grid(row=5, column=3)
Button(root, text='%', bg=sci_bg, fg=button_fg, command=lambda: press("%"), width=7).grid(row=5, column=4)

Button(root, text='0', bg=button_bg, fg=button_fg, command=lambda: press(0), width=7).grid(row=6, column=0)
Button(root, text='.', bg=button_bg, fg=button_fg, command=lambda: press("."), width=7).grid(row=6, column=1)
Button(root, text='Clear', bg="#990000", fg="white", command=clear, width=7).grid(row=6, column=2)
Button(root, text='+', bg=button_bg, fg=button_fg, command=lambda: press("+"), width=7).grid(row=6, column=3)
Button(root, text='=', bg="#007700", fg="white", command=equal, width=7).grid(row=6, column=4)


root.mainloop()
