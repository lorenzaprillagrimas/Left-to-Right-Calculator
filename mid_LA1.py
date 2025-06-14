import tkinter as tk

def on_click(button_value):
    current_text = entry.get()
    new_text = current_text + str(button_value)
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def calculate():
    try:
        expression = entry.get()
        result = eval_left_to_right(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(0, "Error: Division by zero")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def eval_left_to_right(expression):
    tokens = expression.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ').split()
    result = float(tokens.pop(0)) if tokens else 0
    while tokens:
        operator = tokens.pop(0) if tokens else None
        operand = float(tokens.pop(0)) if tokens else None
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            if operand != 0:
                result /= operand
            else:
                raise ZeroDivisionError("Division by zero")
    return result

def clear_entry():
    entry.delete(0, tk.END)

def change_sign():
    current_text = entry.get()
    if current_text and (current_text[0] == '-' or current_text[0] == '+'):
        entry.delete(0)
    else:
        entry.insert(0, '-')

root = tk.Tk()
root.title("Left-to-Right Calculator")
root.geometry("500x400")  
root.configure(bg='black') 

entry = tk.Entry(root, width=20, font=('Arial', 24), bd=5)  
entry.grid(row=0, column=0, columnspan=5, pady=10)

buttons = [
    '7', '8', '9', '*', 'C',
    '4', '5', '6', '-', 'MR',
    '1', '2', '3', '+', 'M+',
    '0', '+/-', '=',
]

row_val = 1
col_val = 0

button_width = 4
button_height = 2

for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, width=button_width, height=button_height, font=('Arial', 16), bg='#5D2D2D', fg='red', bd=5,
                  command=clear_entry).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button == '=':
        tk.Button(root, text=button, width=button_width, height=button_height, font=('Arial', 16), bg='#5D2D2D', fg='red', bd=5,
                  command=calculate).grid(row=row_val, column=col_val, padx=5, pady=5)
    elif button == '+/-':
        tk.Button(root, text=button, width=button_width, height=button_height, font=('Arial', 16), bg='#5D2D2D', fg='red', bd=5,
                  command=change_sign).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=button_width, height=button_height, font=('Arial', 16), bg='#643C50', fg='white', bd=5,
                  command=lambda btn=button: on_click(btn)).grid(row=row_val, column=col_val, padx=5, pady=5)
    
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

root.mainloop()
