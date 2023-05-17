import tkinter as tk
from tkinter import messagebox
from invoice_generator import generate_invoice

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.client_name_label = tk.Label(self, text="Client Name")
        self.client_name_label.pack()
        self.client_name = tk.Entry(self)
        self.client_name.pack()

        self.client_address_label = tk.Label(self, text="Client Address")
        self.client_address_label.pack()
        self.client_address = tk.Entry(self)
        self.client_address.pack()

        self.client_phone_label = tk.Label(self, text="Client Phone")
        self.client_phone_label.pack()
        self.client_phone = tk.Entry(self)
        self.client_phone.pack()

        self.client_email_label = tk.Label(self, text="Client Email")
        self.client_email_label.pack()
        self.client_email = tk.Entry(self)
        self.client_email.pack()

        self.invoice_number_label = tk.Label(self, text="Invoice Number")
        self.invoice_number_label.pack()
        self.invoice_number = tk.Entry(self)
        self.invoice_number.pack()

        self.invoice_date_label = tk.Label(self, text="Invoice Date")
        self.invoice_date_label.pack()
        self.invoice_date = tk.Entry(self)
        self.invoice_date.pack()

        self.items_label = tk.Label(self, text="Items (comma separated list of description, quantity, price)")
        self.items_label.pack()
        self.items = tk.Entry(self)
        self.items.pack()

        self.tax_rate_label = tk.Label(self, text="Tax Rate")
        self.tax_rate_label.pack()
        self.tax_rate = tk.Entry(self)
        self.tax_rate.pack()

        self.submit = tk.Button(self)
        self.submit["text"] = "Submit"
        self.submit["command"] = self.generate_pdf_invoice
        self.submit.pack()

    def generate_pdf_invoice(self):
        items = [tuple(item.split(',')) for item in self.items.get().split(';')]
        items = [(i[0], int(i[1]), float(i[2])) for i in items]  # convert quantity and price to int and float
        tax_rate = float(self.tax_rate.get())
        generate_invoice(self.client_name.get(), self.client_address.get(), self.client_phone.get(), self.client_email.get(), self.invoice_number.get(), self.invoice_date.get(), items, tax_rate)
        messagebox.showinfo("Success", "Invoice generated successfully!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

