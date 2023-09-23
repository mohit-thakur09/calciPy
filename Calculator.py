from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk


class Calculator:
    expression = ""

    def __init__(self, root):
        root.title("Calculator")
        root['bg'] = '#0F0F0F'
        root.resizable(False, False)
        icon = PhotoImage(file="./calculator_icon.png")
        root.iconphoto(root, icon)
        root.config(bg="#404040")

        # style
        operator_style = ttk.Style()
        operator_style.map("TButton", foreground=[('pressed', 'red'), ('active', 'blue')], background=[('pressed', 'black'), ('active', 'white')])
        # operator_style.map("TButton", background=[("active", "#FFBF00")])
        operator_style.configure("TLabel", font=("Arial", 18, 'bold'))
        operator_style.configure("TButton", font=("Arial", 12, 'bold'))

        # Calculator Display.
        self.input_label = ttk.Label(root, text="\n\n\n\n", anchor="se", padding=10)

        # Calculator Buttons.
        # ----------------------------------------

        # operands
        self.button_one = ttk.Button(root, text=1, width=5, padding=10, command=lambda: self.temp(1))
        self.button_two = ttk.Button(root, text=2, width=5, padding=10, command=lambda: self.temp(2))
        self.button_three = ttk.Button(root, text=3, width=5, padding=10, command=lambda: self.temp(3))
        self.button_four = ttk.Button(root, text=4, width=5, padding=10, command=lambda: self.temp(4))
        self.button_five = ttk.Button(root, text=5, width=5, padding=10, command=lambda: self.temp(5))
        self.button_six = ttk.Button(root, text=6, width=5, padding=10, command=lambda: self.temp(6))
        self.button_seven = ttk.Button(root, text=7, width=5, padding=10, command=lambda: self.temp(7))
        self.button_eight = ttk.Button(root, text=8, width=5, padding=10, command=lambda: self.temp(8))
        self.button_nine = ttk.Button(root, text=9, width=5, padding=10, command=lambda: self.temp(9))
        self.button_zero = ttk.Button(root, text=0, width=5, padding=10, command=lambda: self.temp(0))

        # operators
        self.button_plus = ttk.Button(root, text="+", width=5, padding=10, command=lambda: self.temp("+"))
        self.button_minus = ttk.Button(root, text="-", width=5, padding=10, command=lambda: self.temp("-"))
        self.button_product = ttk.Button(root, text="x", width=5, padding=10, command=lambda: self.temp("*"))
        self.button_divide = ttk.Button(root, text="/", width=5, padding=10, command=lambda: self.temp("/"))
        self.button_percent = ttk.Button(root, text="%", width=5, padding=10, command=lambda: self.temp("%"))
        self.button_backspace = ttk.Button(root, text="C", width=5, padding=10, command=lambda: self.temp("C"))
        self.button_clear = ttk.Button(root, text="CA", width=5, padding=10, command=lambda: self.temp("CA"))
        self.button_dot = ttk.Button(root, text=".", width=5, padding=10, command=lambda: self.temp("."))
        self.button_equals = ttk.Button(root, text="=", width=5, padding=10, command=lambda: self.temp("="))

        # Grid all UI.
        self.input_label.grid(row=0, columnspan=4, padx=2, pady=2, sticky=E + W)

        self.button_clear.grid(row=1, column=0, padx=2, pady=2)
        self.button_percent.grid(row=1, column=1, padx=2, pady=2)
        self.button_backspace.grid(row=1, column=2, padx=2, pady=2)
        self.button_plus.grid(row=1, column=3, padx=2, pady=2)

        self.button_one.grid(row=2, column=0, padx=2, pady=2)
        self.button_two.grid(row=2, column=1, padx=2, pady=2)
        self.button_three.grid(row=2, column=2, padx=2, pady=2)
        self.button_minus.grid(row=2, column=3, padx=2, pady=2)

        self.button_four.grid(row=3, column=0, padx=2, pady=2)
        self.button_five.grid(row=3, column=1, padx=2, pady=2)
        self.button_six.grid(row=3, column=2, padx=2, pady=2)
        self.button_product.grid(row=3, column=3, padx=2, pady=2)

        self.button_seven.grid(row=4, column=0, padx=2, pady=2)
        self.button_eight.grid(row=4, column=1, padx=2, pady=2)
        self.button_nine.grid(row=4, column=2, padx=2, pady=2)
        self.button_divide.grid(row=4, column=3, padx=2, pady=2)

        self.button_dot.grid(row=5, column=0, padx=2, pady=2)
        self.button_zero.grid(row=5, column=1, padx=2, pady=2)
        self.button_equals.grid(row=5, column=2, columnspan=2, padx=2, sticky=E + W)

    def temp(self, number):
        number = str(number)

        if number == 'CA':
            Calculator.expression = ""
            self.input_label["text"] = "\n\n\n\n"
        elif number == 'C':
            Calculator.expression = Calculator.expression[0:-1]
            self.input_label["text"] = "\n\n\n\n"+Calculator.expression
        elif number == "=":
            try:
                ans = eval(Calculator.expression)
                actual_ans = (" " * (len(Calculator.expression)-len(str(ans))))+str(ans)
                self.input_label["text"] = "\n\n\n"+Calculator.expression+"\n"+actual_ans
                Calculator.expression = str(ans)
            except ZeroDivisionError:
                messagebox.showerror("Division Error!", "Cannot be divided by zero.")
            except Exception:
                messagebox.showerror("Wrong Input", "Please provide the correct input!")
        else:
            Calculator.expression += number
            self.input_label["text"] = "\n\n\n\n"+Calculator.expression


if __name__ == "__main__":
    main_root = Tk()
    calci = Calculator(main_root)
    main_root.mainloop()
