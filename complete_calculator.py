import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")

root.minsize(300,400)

style = ttk.Style()
if "alt" in style.theme_names():
    style.theme_use("alt")

calculation = ""

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    update_display()


def evaluate():
    global calculation
    try:
        calc_str = calculation.replace("%", "/").replace("x", "*")
        calculation = str(eval(calc_str))
    except:
        clear()
        text_result.insert("end","Error")
        text_result.configure(background = "#FF3B30")

def clear():
    global calculation
    calculation = ""
    update_display()

def update_display():
    text_result.configure(background = "#1C1C1E")
    text_result.delete(1.0, "end")
    text_result.insert("end", calculation)

for i in range(6):
    root.grid_rowconfigure(i, weight = 1)

for i in range(4):
    root.grid_columnconfigure(i, weight = 1)

text_result = tk.Text(root, height=2,font = ("Arial", 24),background="#1C1C1E", foreground="white", pady=10)

text_result.grid(row=0, column = 0, columnspan = 4, sticky = "nsew", padx= 5, pady=(10,5))

style.configure("Calculator.TButton", font = ("Arial", 14), padding = 5)

style.configure("Equal.Calculator.Tbutton", background = "#0078D7")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('%', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('=', 5, 2, 2)
]

for button in buttons:
    text = button[0]
    row = button[1]
    col = button[2]
    colspan = button[3] if len(button) > 3 else 1   

    if text == "=":
        command = evaluate
    elif text == "C":
        command = clear
    else:
        command = lambda t=text: add_calculation(t)

    if text == "=":
        btn_style = "Equal.Calculator.TButton"
    else:
        btn_style = "Calculator.TButton"

    btn = ttk.Button(root, text=text, style=btn_style, command=command)

    btn.grid(row=row, column=col, columnspan=colspan, sticky = "nsew", padx = 2, pady = 2)

root.eval("tk::PlaceWindow . center")

root.mainloop()