import tkinter as tk
from tkinter import messagebox
import json

class BudgetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Budget App")
        self.transactions = []
        self.load_data()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        self.income_label = tk.Label(self.root, text="Income Amount:")
        self.income_label.grid(row=0, column=0, padx=10, pady=5)
        
        self.income_entry = tk.Entry(self.root)
        self.income_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.income_desc_label = tk.Label(self.root, text="Description:")
        self.income_desc_label.grid(row=0, column=2, padx=10, pady=5)
        
        self.income_desc_entry = tk.Entry(self.root)
        self.income_desc_entry.grid(row=0, column=3, padx=10, pady=5)
        
        self.add_income_button = tk.Button(self.root, text="Add Income", command=self.add_income)
        self.add_income_button.grid(row=0, column=4, padx=10, pady=5)
        
        self.expense_label = tk.Label(self.root, text="Expense Amount:")
        self.expense_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.expense_entry = tk.Entry(self.root)
        self.expense_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.expense_desc_label = tk.Label(self.root, text="Description:")
        self.expense_desc_label.grid(row=1, column=2, padx=10, pady=5)
        
        self.expense_desc_entry = tk.Entry(self.root)
        self.expense_desc_entry.grid(row=1, column=3, padx=10, pady=5)
        
        self.add_expense_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.grid(row=1, column=4, padx=10, pady=5)
        
        self.view_summary_button = tk.Button(self.root, text="View Summary", command=self.view_summary)
        self.view_summary_button.grid(row=2, column=0, columnspan=5, pady=10)
        
        self.summary_text = tk.Text(self.root, height=10, width=80)
        self.summary_text.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

    def add_income(self):
        amount = self.income_entry.get()
        description = self.income_desc_entry.get()
        if amount and description:
            try:
                amount = float(amount)
                self.transactions.append({"type": "income", "amount": amount, "description": description})
                self.income_entry.delete(0, tk.END)
                self.income_desc_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Income added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def add_expense(self):
        amount = self.expense_entry.get()
        description = self.expense_desc_entry.get()
        if amount and description:
            try:
                amount = float(amount)
                self.transactions.append({"type": "expense", "amount": amount, "description": description})
                self.expense_entry.delete(0, tk.END)
                self.expense_desc_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Expense added successfully!")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid amount.")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_summary(self):
        total_income = sum(item['amount'] for item in self.transactions if item['type'] == 'income')
        total_expense = sum(item['amount'] for item in self.transactions if item['type'] == 'expense')
        balance = total_income - total_expense
        summary = (
            f"Total Income: ${total_income:.2f}\n"
            f"Total Expense: ${total_expense:.2f}\n"
            f"Balance: ${balance:.2f}\n"
        )
        self.summary_text.delete(1.0, tk.END)
        self.summary_text.insert(tk.END, summary)
    
    def save_data(self):
        with open('budget_data.json', 'w') as f:
            json.dump(self.transactions, f)
    
    def load_data(self):
        try:
            with open('budget_data.json', 'r') as f:
                self.transactions = json.load(f)
        except FileNotFoundError:
            self.transactions = []

    def on_closing(self):
        self.save_data()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()