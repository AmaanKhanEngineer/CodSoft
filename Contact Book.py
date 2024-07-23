import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
#contact 
    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"

    def update(self, phone_number=None, email=None, address=None):
        if phone_number:
            self.phone_number = phone_number
        if email:
            self.email = email
        if address:
            self.address = address

class ContactList:
    def __init__(self):
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def view(self):
        if not self.contacts:
            return "No contacts found."
        return "\n-------------------\n".join(str(contact) for contact in self.contacts)

    def search(self, keyword):
        results = [str(contact) for contact in self.contacts if keyword.lower() in contact.name.lower() or keyword in contact.phone_number]
        if not results:
            return "Contact not found."
        return "\n-------------------\n".join(results)

    def update(self, name, phone_number=None, email=None, address=None):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                contact.update(phone_number, email, address)
                return "Contact updated successfully."
        return "Contact not found."

    def delete(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                return "Contact deleted successfully."
        return "Contact not found."

class ContactManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.contact_list = ContactList()
        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self.root, width=40, height=15)
        self.text_area.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        button_frame = tk.Frame(self.root)
        button_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        
        buttons = [
            ("Add Contact", self.add_contact),
            ("View Contacts", self.view_contacts),
            ("Search Contact", self.search_contact),
            ("Update Contact", self.update_contact),
            ("Delete Contact", self.delete_contact),
            ("Exit", self.root.quit)
        ]
        
        for i, (text, command) in enumerate(buttons):
            tk.Button(button_frame, text=text, command=command).grid(row=0, column=i, padx=5, pady=5, sticky="ew")

    def get_contact_details(self, action):
        details = simpledialog.askstring("Contact Details", f"Enter details for {action}:\n\nFormat: Name, Phone, Email, Address")
        if details:
            details = [detail.strip() for detail in details.split(',')]
            if len(details) == 4:
                return tuple(details)
            messagebox.showwarning("Input Error", "Please enter all details in the format: Name, Phone, Email, Address.")
        return None, None, None, None

    def add_contact(self):
        name, phone, email, address = self.get_contact_details("Add Contact")
        if name:
            contact = Contact(name, phone, email, address)
            self.contact_list.add(contact)
            messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, self.contact_list.view())

    def search_contact(self):
        keyword = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if keyword:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, self.contact_list.search(keyword))

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter name of contact to update:")
        if name:
            phone = simpledialog.askstring("Update Contact", "Enter new phone number (leave blank to keep current):")
            email = simpledialog.askstring("Update Contact", "Enter new email (leave blank to keep current):")
            address = simpledialog.askstring("Update Contact", "Enter new address (leave blank to keep current):")
            result = self.contact_list.update(name, phone, email, address)
            messagebox.showinfo("Update Status", result)

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter name of contact to delete:")
        if name:
            result = self.contact_list.delete(name)
            messagebox.showinfo("Delete Status", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagementApp(root)
    root.mainloop()
