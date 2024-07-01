import tkinter
from tkinter import ttk


def clear_item():
    qty_spinbox.delete(0, tkinter.END)
    qty_spinbox.insert(0, '1')
    description_entry.delete(0, tkinter.END)
    unit_price_spinbox.delete(0, tkinter.END)
    unit_price_spinbox.insert(0, '0.0')


def add_item():
    qty = int(qty_spinbox.get())
    desc = description_entry.get()
    price = float(unit_price_spinbox.get())
    line_total = qty*price
    invoice_item = [qty, desc, price, line_total]

    tree.insert('', 0, values=invoice_item)
    clear_item()


def new_invoice():
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    phone_entry.delete(0, tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())


window = tkinter.Tk()
window.title('Invoice Generator Form')

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

# Row 0
first_name_label = tkinter.Label(frame, text='First Name')
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(frame, text='Last Name')
last_name_label.grid(row=0, column=1)
phone_label = tkinter.Label(frame, text='Phone')
phone_label.grid(row=0, column=2)

# Row 1
first_name_entry = tkinter.Entry(frame)
last_name_entry = tkinter.Entry(frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)
phone_entry = tkinter.Entry(frame)
phone_entry.grid(row=1, column=2)

# Row 2
qty_label = tkinter.Label(frame, text='Qty')
qty_label.grid(row=2, column=0)
description_label = tkinter.Label(frame, text='Description')
description_label.grid(row=2, column=1)
unit_price_label = tkinter.Label(frame, text='Unit Price')
unit_price_label.grid(row=2, column=2)

# Row 3
qty_spinbox = tkinter.Spinbox(frame, from_=1, to=100)
qty_spinbox.grid(row=3, column=0)
description_entry = tkinter.Entry(frame)
description_entry.grid(row=3, column=1)
unit_price_spinbox = tkinter.Spinbox(frame, from_=1, to=1000000, increment=0.5)
unit_price_spinbox.grid(row=3, column=2)

add_item_button = tkinter.Button(frame, text='Add Item', command=add_item)
add_item_button.grid(row=4, column=2)

columns = ('qty', 'desc', 'price', 'total')
tree = ttk.Treeview(frame, columns=columns, show='headings')

tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Price')
tree.heading('total', text='Price')

tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

save_invoice_button = tkinter.Button(frame, text='Generate Invoice')
save_invoice_button.grid(row=6, column=0, columnspan=3, sticky='news', padx=20, pady=5)
new_invoice_button = tkinter.Button(frame, text='New Invoice', command=new_invoice)
new_invoice_button.grid(row=7, column=0, columnspan=3, sticky='news', padx=20, pady=5)

window.mainloop()
