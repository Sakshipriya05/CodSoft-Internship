import tkinter as tk
from tkinter import messagebox

contact_list = {}

def add_contact():
    name = name_entry.get()
    if name in contact_list:
        messagebox.showinfo("Duplicate", f"{name} already exists")
    else:
        try:
            phone_no = int(phone_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Phone number must be a number.")
            return
        email = email_entry.get()
        address = address_entry.get()
        contact_list[name] = {'phone no.': phone_no, 'email': email, 'address': address}
        messagebox.showinfo("Success", f"Contact name {name} has been successfully added")

def view_contact():
    name = name_entry.get()
    if name in contact_list:
        contact = contact_list[name]
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        phone_entry.insert(0, contact['phone no.'])
        email_entry.insert(0, contact['email'])
        address_entry.insert(0, contact['address'])
    else:
        messagebox.showerror("Not Found", "Contact not found")

def search_contact():
    search_name = name_entry.get()
    found = False
    result_list.delete(0, tk.END)
    for name, contact in contact_list.items():
        if search_name.lower() in name.lower():
            result_list.insert(tk.END, f"{name}: {contact}")
            found = True
    if not found:
        result_list.insert(tk.END, "No contact found with this name")

def update_contact():
    name = name_entry.get()
    if name in contact_list:
        try:
            phone_no = int(phone_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Phone number must be a number.")
            return
        email = email_entry.get()
        address = address_entry.get()
        contact_list[name] = {'phone no.': phone_no, 'email': email, 'address': address}
        messagebox.showinfo("Updated", f"Contact {name} has been updated.")
    else:
        messagebox.showerror("Not Found", "Contact not found")

def delete_contact():
    name = name_entry.get()
    if name in contact_list:
        del contact_list[name]
        messagebox.showinfo("Deleted", f"Contact {name} has been deleted.")
    else:
        messagebox.showerror("Not Found", "Contact not found")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    result_list.delete(0, tk.END)

# GUI Layout
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x550")

tk.Label(root, text="Contact Book", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone Number").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root)
address_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="View Contact", command=view_contact).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)
tk.Button(root, text="Clear", command=clear_fields).pack(pady=5)

tk.Label(root, text="Search Results:").pack(pady=5)
result_list = tk.Listbox(root, height=8)
result_list.pack(fill=tk.BOTH, expand=True, padx=10)

root.mainloop()


































