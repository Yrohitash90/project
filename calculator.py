import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.current_input = ""
        self.result_var = tk.StringVar()

        # Create the display
        self.display = tk.Entry(bg='skyblue', textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=4)

        # Create buttons including decimal point, parentheses, and undo
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '(', ')', 
            'C', 'DEL', '+',
            '='  # Add Undo button
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(bg='red', text=button, padx=20, pady=20, font=("Arial", 18),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == 'C':
            self.current_input = ""
            self.result_var.set("")
        elif button == 'DEL':
            # Remove the last character from the current input
            self.current_input = self.current_input[:-1]
            self.result_var.set(self.current_input)
        elif button == '=':
            try:
                # Evaluate the expression and update the display
                self.current_input = str(eval(self.current_input))
                self.result_var.set(self.current_input)
            except Exception:
                self.result_var.set("syntax error")
                self.current_input = ""
        else:
            # Append the button value to the current input
            self.current_input += button
            self.result_var.set(self.current_input)

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg='red')
    calculator = Calculator(root)
    root.mainloop()
