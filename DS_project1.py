import tkinter as tk
from tkinter import messagebox

class MyStack:
    class Item:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, max_size):
        self.top = None
        self.max_size = max_size
        self.under = 0
        self.over = 0

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return self.size() == self.max_size

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count

    def create(self):
        self.top = None

    def push(self, value):
        if self.is_full():
            self.over = -1
        else:
            self.over = 0
            new_item = self.Item(value)
            new_item.next = self.top
            self.top = new_item

    def pop(self):
        if self.is_empty():
            self.under = -1
            return None
        else:
            self.under = 0
            value = self.top.value
            self.top = self.top.next
            return value

def invert_string(input_str):
    max_size = len(input_str)
    output_str = [''] * max_size
    my_stack = MyStack(max_size)

    for char in input_str:
        my_stack.push(char)

    for i in range(max_size):
        output_str[i] = my_stack.pop()

    inverted_str = ''.join(output_str)
    return inverted_str

def are_pair(open, close):
    if open == '(' and close == ')':
        return True
    elif open == '{' and close == '}':
        return True
    elif open == '[' and close == ']':
        return True
    return False

def are_balanced(exp):
    my_stack = MyStack(len(exp))
    length = len(exp)
    allowed_chars = {'(', ')', '{', '}', '[', ']'}
    for i in range(length):
        if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
            my_stack.push(exp[i])
        elif exp[i] == ')' or exp[i] == '}' or exp[i] == ']':
            if my_stack.is_empty() or not are_pair(my_stack.top.value, exp[i]):
                return False
            my_stack.pop()
        elif exp[i] not in allowed_chars:
            return False
    return my_stack.is_empty()

def check_balanced():
    user_input = entry.get()
    if are_balanced(user_input):
        messagebox.showinfo("Result", "The string is balanced.")
    else:
        messagebox.showinfo("Result", "The string is not balanced.")

def invert():
    user_input = entry.get()
    inverted_str = invert_string(user_input)
    messagebox.showinfo("Result", f"Inverted String: {inverted_str}")

# GUI Setup
root = tk.Tk()
root.title("String Operations")
root.geometry("400x200")

label = tk.Label(root, text="Enter a string:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

btn_check = tk.Button(frame, text="Check Balanced", command=check_balanced)
btn_check.grid(row=0, column=0, padx=5)

btn_invert = tk.Button(frame, text="Invert String", command=invert)
btn_invert.grid(row=0, column=1, padx=5)

btn_exit = tk.Button(root, text="Exit", command=root.quit)
btn_exit.pack(pady=10)

root.mainloop()
