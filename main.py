import tkinter as tk
from tkinter import messagebox, simpledialog

def add_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()
    # Validate phone number length
    if len(phone_number) != 10:
        messagebox.showerror("Invalid Phone Number", "Please enter a valid 10-digit phone number.")
        return
    # Validate name and phone number are filled
    if not name or not phone_number:
        messagebox.showerror("Missing Information", "Please fill in both name and phone number.")
        return
    # Add the contact to the list
    contacts.append((name, phone_number))
    # Show a success message
    messagebox.showinfo("Contact Added", f"Contact {name} added successfully!")
    # Enable the Add to Favorites button
    add_to_favs_button.config(state=tk.NORMAL)
    # Update the recent contacts list
    update_recent_contacts()

def view_contacts():
    view_window = tk.Toplevel(root)
    view_window.title("View Contacts")
    # Display the contacts in the new window with checkboxes
    for idx, contact in enumerate(contacts):
        contact_label = tk.Label(view_window, text=f"Name: {contact[0]}, Phone Number: {contact[1]}")
        contact_label.grid(row=idx, column=0, pady=5, sticky=tk.W)
        # Add checkbox for each contact
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(view_window, variable=checkbox_var)
        checkbox.grid(row=idx, column=1, pady=5, padx=5)
        # Store the checkbox variable and contact in a dictionary
        checkbox_dict[idx] = {"checkbox_var": checkbox_var, "contact": contact}
    # Delete Selected button
    delete_selected_button = tk.Button(view_window, text="Delete Selected",
                                       command=lambda: delete_selected(view_window))
    delete_selected_button.grid(row=len(contacts), column=0, pady=10)
    # View Deleted Contacts button
    view_deleted_button = tk.Button(view_window, text="View Deleted Contacts", command=view_deleted_contacts)
    view_deleted_button.grid(row=len(contacts) + 1, column=0, pady=5)
    # Edit Contacts button
    edit_contacts_button = tk.Button(view_window, text="Edit Contacts", command=edit_contacts)
    edit_contacts_button.grid(row=len(contacts) + 2, column=0, pady=5)

def edit_contacts():
    edit_window = tk.Toplevel(root)
    edit_window.title("Edit Contacts")
    # Display the contacts in the new window with entry fields for editing
    for idx, contact in enumerate(contacts):
        name_label = tk.Label(edit_window, text="Name:")
        name_label.grid(row=idx, column=0, pady=5, sticky=tk.E)
        phone_label = tk.Label(edit_window, text="Phone Number:")
        phone_label.grid(row=idx, column=2, pady=5, sticky=tk.E)
        name_entry_edit = tk.Entry(edit_window, font=("Helvetica", 12))
        name_entry_edit.insert(0, contact[0])
        name_entry_edit.grid(row=idx, column=1, pady=5)
        phone_entry_edit = tk.Entry(edit_window, font=("Helvetica", 12))
        phone_entry_edit.insert(0, contact[1])
        phone_entry_edit.grid(row=idx, column=3, pady=5)
        # Store the entry fields in a dictionary
        entry_dict[idx] = {"name_entry": name_entry_edit, "phone_entry": phone_entry_edit}
    # Submit Edits button
    submit_edits_button = tk.Button(edit_window, text="Submit Edits", command=lambda: submit_edits(edit_window))
    submit_edits_button.grid(row=len(contacts), column=0, columnspan=4, pady=10)

def submit_edits(edit_window):
    for idx, data in entry_dict.items():
        name_entry_edit = data["name_entry"]
        phone_entry_edit = data["phone_entry"]
        updated_name = name_entry_edit.get()
        updated_phone = phone_entry_edit.get()
        contacts[idx] = (updated_name, updated_phone)
    edit_window.destroy()
    view_contacts()

def delete_selected(view_window):
    global deleted_contacts
    for idx, data in checkbox_dict.items():
        checkbox_var = data["checkbox_var"]
        contact = data["contact"]
        if checkbox_var.get():
            contacts.remove(contact)
            deleted_contacts.append(contact)
    view_window.destroy()
    view_contacts()

def delete_contact():
    view_contacts()

def view_deleted_contacts():
    deleted_window = tk.Toplevel(root)
    deleted_window.title("Deleted Contacts")
    # Display the deleted contacts
    for idx, contact in enumerate(deleted_contacts):
        contact_label = tk.Label(deleted_window, text=f"Name: {contact[0]}, Phone Number: {contact[1]}")
        contact_label.grid(row=idx, column=0, pady=5, sticky=tk.W)

# Favorites window
def show_favorite_contacts():
    favorites_window = tk.Toplevel(root)
    favorites_window.title("Favorite Contacts")
    # Display the favorite contacts
    for idx, contact in enumerate(favorite_contacts):
        contact_label = tk.Label(favorites_window, text=f"Name: {contact[0]}, Phone Number: {contact[1]}")
        contact_label.grid(row=idx, column=0, pady=5, sticky=tk.W)

# Add contact to favorites
def add_to_favorites():
    name = name_entry.get()
    phone_number = phone_entry.get()
    # Validate phone number length
    if len(phone_number) != 10:
        messagebox.showerror("Invalid Phone Number", "Please enter a valid 10-digit phone number.")
        return
    # Validate name and phone number are filled
    if not name or not phone_number:
        messagebox.showerror("Missing Information", "Please fill in both name and phone number.")
        return
    # Add the contact to the favorites list
    favorite_contacts.append((name, phone_number))
    # Show a success message
    messagebox.showinfo("Favorite Added", f"Contact {name} added to favorites!")
    # Clear the entries
    reset_fields()

def update_recent_contacts():
    recent_contacts_window = tk.Toplevel(root)
    recent_contacts_window.title("Recent Contacts")
    # Display the last three entered contacts
    recent_contacts = contacts[-3:]
    for idx, contact in enumerate(recent_contacts):
        contact_label = tk.Label(recent_contacts_window, text=f"Name: {contact[0]}, Phone Number: {contact[1]}")
        contact_label.grid(row=idx, column=0, pady=5, sticky=tk.W)

# Recent Added Contacts window
def recent_added_contacts():
    recent_added_window = tk.Toplevel(root)
    recent_added_window.title("Recent Added Contacts")
    # Display the last three added contacts
    recent_added_contacts = contacts[-3:]
    for idx, contact in enumerate(recent_added_contacts):
        contact_label = tk.Label(recent_added_window, text=f"Name: {contact[0]}, Phone Number: {contact[1]}")
        contact_label.grid(row=idx, column=0, pady=5, sticky=tk.W)

# Reset fields function
def reset_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("600x600")  # Set larger window size
root.configure(bg="#e6e6e6")  # Set background color
# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - 600) // 2
y_coordinate = (screen_height - 600) // 2
root.geometry(f"600x600+{x_coordinate}+{y_coordinate}")
# Contacts list
contacts = []
# Favorite contacts list
favorite_contacts = []
# Deleted contacts list
deleted_contacts = []
# Checkbox dictionary to store checkbox variables and corresponding contacts
checkbox_dict = {}
# Entry dictionary to store entry fields for editing
entry_dict = {}
# Name label and entry
name_label = tk.Label(root, text="Name:", bg="#e6e6e6", font=("Helvetica", 12))
name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
name_entry = tk.Entry(root, font=("Helvetica", 12))
name_entry.grid(row=0, column=1, padx=10, pady=5)  # Add space below the entry
# Phone number label and entry
phone_label = tk.Label(root, text="Phone Number:", bg="#e6e6e6", font=("Helvetica", 12))
phone_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
phone_entry = tk.Entry(root, font=("Helvetica", 12))
phone_entry.grid(row=1, column=1, padx=10, pady=5)  # Add space below the entry
# Add button
add_button = tk.Button(root, text="Add", command=add_contact, font=("Helvetica", 12))
add_button.grid(row=2, column=0, columnspan=2, pady=10)  # Add space below the button
# View button
view_button = tk.Button(root, text="View", command=view_contacts, font=("Helvetica", 12))
view_button.grid(row=3, column=0, columnspan=2, pady=5)  # Add space below the button
# Delete button
delete_button = tk.Button(root, text="Delete", command=delete_contact, font=("Helvetica", 12))
delete_button.grid(row=4, column=0, columnspan=2, pady=5)  # Add space below the button
# Edit button
edit_button = tk.Button(root, text="Edit", command=edit_contacts, font=("Helvetica", 12))
edit_button.grid(row=5, column=0, columnspan=2, pady=5)  # Add space below the button
# Reset button
reset_button = tk.Button(root, text="Reset", command=reset_fields, font=("Helvetica", 12))
reset_button.grid(row=6, column=0, columnspan=2, pady=10)  # Add space below the button
# Add to Favorites button (Initially disabled)
add_to_favs_button = tk.Button(root, text="Add to Favorites", command=add_to_favorites, font=("Helvetica", 12),
                               state=tk.DISABLED)
add_to_favs_button.grid(row=7, column=0, columnspan=2, pady=10)  # Add space below the button
# View Favorites Contacts button
view_favs_button = tk.Button(root, text="View Favorites Contacts", command=show_favorite_contacts,
                             font=("Helvetica", 12))
view_favs_button.grid(row=8, column=0, columnspan=2, pady=10)  # Add space below the button
# Recent Added Contacts button
recent_added_button = tk.Button(root, text="Recent Added Contacts", command=recent_added_contacts,
                                font=("Helvetica", 12))
recent_added_button.grid(row=9, column=0, columnspan=2, pady=10)  # Add space below the button
# Start the Tkinter event loop
root.mainloop()
