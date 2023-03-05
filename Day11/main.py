import tkinter as tk
from currency_converter import CurrencyConverter

class CurrencyConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Currency Converter")

        self.c = CurrencyConverter()

        # Input frame
        input_frame = tk.Frame(self.master)
        input_frame.pack(padx=10, pady=10)

        tk.Label(input_frame, text="From Currency:").grid(row=0, column=0)
        self.from_currency_var = tk.StringVar(value="USD")
        tk.OptionMenu(input_frame, self.from_currency_var, *self.c.currencies).grid(row=0, column=1)

        tk.Label(input_frame, text="To Currency:").grid(row=1, column=0)
        self.to_currency_var = tk.StringVar(value="EUR")
        tk.OptionMenu(input_frame, self.to_currency_var, *self.c.currencies).grid(row=1, column=1)

        tk.Label(input_frame, text="Amount:").grid(row=2, column=0)
        self.amount_entry = tk.Entry(input_frame)
        self.amount_entry.grid(row=2, column=1)

        # Button
        tk.Button(self.master, text="Convert", command=self.convert_currency).pack(pady=10)

        # Output frame
        output_frame = tk.Frame(self.master)
        output_frame.pack(padx=10, pady=10)

        tk.Label(output_frame, text="Result:").grid(row=0, column=0)
        self.result_label = tk.Label(output_frame, text="")
        self.result_label.grid(row=0, column=1)

    def convert_currency(self):
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()
        amount = float(self.amount_entry.get())
        result = self.c.convert(amount, from_currency, to_currency)
        self.result_label.config(text=result)

root = tk.Tk()
ex = CurrencyConverterGUI(root)
root.mainloop()
