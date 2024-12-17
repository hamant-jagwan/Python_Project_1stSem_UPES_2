import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button click event
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_operation(op):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + op)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text in '0123456789':
        command = lambda t=text: button_click(t)
    elif text == 'C':
        command = button_clear
    elif text == '=':
        command = button_equal
    else:
        command = lambda t=text: button_operation(t)

    tk.Button(root, text=text, padx=20, pady=20, command=command).grid(row=row, column=col)

# Run the application
root.mainloop()
