import tkinter as tk
from tkinter import ttk, messagebox
import os

# Define the correct passcode
CORRECT_PASSCODE = "admin123"

# Function to ensure the file exists
def ensure_file_exists():
    if not os.path.isfile("registrations.txt"):
        open("registrations.txt", "w").close()  # Create the file if it does not exist

# Function to load and display user data from file
def load_user_data():
    user_tree.delete(*user_tree.get_children())
    ensure_file_exists()  # Ensure the file exists before attempting to read

    try:
        with open("registrations.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                fields = line.strip().split(',')
                if len(fields) >= 6:
                    user_id, name, father_name, gender, grade, email = fields
                    user_tree.insert("", "end", values=(user_id, name, father_name, gender, grade, email))
    except Exception as e:
        messagebox.showerror("File Error", f"Error reading file: {e}")

# Function to update user details in file
def update_user_in_file(user_id, name, father_name, gender, grade, email):
    ensure_file_exists()  # Ensure the file exists before attempting to read

    try:
        # Read all lines from the file
        with open("registrations.txt", "r") as file:
            lines = file.readlines()
        
        # Write back all lines except the one to be updated
        with open("registrations.txt", "w") as file:
            updated = False
            for line in lines:
                if line.strip().split(",")[0] == user_id:
                    file.write(f"{user_id},{name},{father_name},{gender},{grade},{email}\n")
                    updated = True
                else:
                    file.write(line)
            
            if not updated:
                file.write(f"{user_id},{name},{father_name},{gender},{grade},{email}\n")
    except Exception as e:
        messagebox.showerror("File Error", f"Error updating file: {e}")

# Function to add a new user
def add_user():
    def save_new_user():
        user_id = entry_id.get()
        name = entry_name.get()
        father_name = entry_father_name.get()
        gender = gender_var.get()
        grade = entry_grade.get()
        email = entry_email.get()
        if user_id and name and father_name and gender and grade and email:
            with open("registrations.txt", "a") as file:
                file.write(f"{user_id},{name},{father_name},{gender},{grade},{email}\n")
            load_user_data()
            add_user_window.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    add_user_window = tk.Toplevel(root)
    add_user_window.title("Add New User")
    add_user_window.geometry("350x300")
    add_user_window.configure(bg="#2b2b2b")

    tk.Label(add_user_window, text="User ID:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_id = tk.Entry(add_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_id.pack(pady=5)

    tk.Label(add_user_window, text="Name:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_name = tk.Entry(add_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_name.pack(pady=5)

    tk.Label(add_user_window, text="Father's Name:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_father_name = tk.Entry(add_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_father_name.pack(pady=5)

    tk.Label(add_user_window, text="Gender:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    gender_var = tk.StringVar(value="Male")
    tk.Radiobutton(add_user_window, text="Male", variable=gender_var, value="Male", bg="#2b2b2b", fg="white").pack(pady=2)
    tk.Radiobutton(add_user_window, text="Female", variable=gender_var, value="Female", bg="#2b2b2b", fg="white").pack(pady=2)

    tk.Label(add_user_window, text="Grade:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_grade = tk.Entry(add_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_grade.pack(pady=5)

    tk.Label(add_user_window, text="Email:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_email = tk.Entry(add_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_email.pack(pady=5)

    tk.Button(add_user_window, text="Save", font=("Helvetica", 12, "bold"), bg="#28a745", fg="white", command=save_new_user).pack(pady=10)

# Function to update the selected user
def update_user():
    selected_item = user_tree.selection()
    if not selected_item:
        messagebox.showwarning("Select User", "Please select a user to update.")
        return

    def save_updated_user():
        user_id = entry_id.get()
        name = entry_name.get()
        father_name = entry_father_name.get()
        gender = gender_var.get()
        grade = entry_grade.get()
        email = entry_email.get()
        if user_id and name and father_name and gender and grade and email:
            update_user_in_file(user_id, name, father_name, gender, grade, email)
            load_user_data()
            update_user_window.destroy()
        else:
            messagebox.showwarning("Input Error", "All fields are required.")

    update_user_window = tk.Toplevel(root)
    update_user_window.title("Update User")
    update_user_window.geometry("350x300")
    update_user_window.configure(bg="#2b2b2b")

    current_values = user_tree.item(selected_item)["values"]

    tk.Label(update_user_window, text="User ID:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_id = tk.Entry(update_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_id.pack(pady=5)
    entry_id.insert(0, current_values[0])

    tk.Label(update_user_window, text="Name:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_name = tk.Entry(update_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_name.pack(pady=5)
    entry_name.insert(0, current_values[1])

    tk.Label(update_user_window, text="Father's Name:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_father_name = tk.Entry(update_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_father_name.pack(pady=5)
    entry_father_name.insert(0, current_values[2])

    tk.Label(update_user_window, text="Gender:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    gender_var = tk.StringVar(value=current_values[3])
    tk.Radiobutton(update_user_window, text="Male", variable=gender_var, value="Male", bg="#2b2b2b", fg="white").pack(pady=2)
    tk.Radiobutton(update_user_window, text="Female", variable=gender_var, value="Female", bg="#2b2b2b", fg="white").pack(pady=2)

    tk.Label(update_user_window, text="Grade:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_grade = tk.Entry(update_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_grade.pack(pady=5)
    entry_grade.insert(0, current_values[4])

    tk.Label(update_user_window, text="Email:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=5)
    entry_email = tk.Entry(update_user_window, font=("Helvetica", 12), bg="#454545", fg="white")
    entry_email.pack(pady=5)
    entry_email.insert(0, current_values[5])

    tk.Button(update_user_window, text="Save", font=("Helvetica", 12, "bold"), bg="#28a745", fg="white", command=save_updated_user).pack(pady=10)

# Function to delete a user
def delete_user():
    selected_item = user_tree.selection()
    if not selected_item:
        messagebox.showwarning("Select User", "Please select a user to delete.")
        return

    current_id = user_tree.item(selected_item)['values'][0]
    user_tree.delete(selected_item)

    ensure_file_exists()  # Ensure the file exists before attempting to delete

    try:
        with open("registrations.txt", "r") as file:
            lines = file.readlines()
        with open("registrations.txt", "w") as file:
            for line in lines:
                if line.strip().split(",")[0] != current_id:
                    file.write(line)
    except Exception as e:
        messagebox.showerror("File Error", f"Error deleting from file: {e}")

# Function to authenticate passcode and open admin panel
def authenticate_passcode():
    entered_passcode = passcode_entry.get()
    if entered_passcode == CORRECT_PASSCODE:
        passcode_window.destroy()
        open_admin_panel()
    else:
        messagebox.showerror("Authentication Error", "Incorrect passcode. Please try again.")

# Function to open the admin panel
def open_admin_panel():
    global root
    root = tk.Tk()
    root.title("Admin Panel")
    root.geometry("800x600")
    root.configure(bg="#2b2b2b")

    # Treeview to display user data
    global user_tree
    user_tree = ttk.Treeview(root, columns=("ID", "Name", "Father Name", "Gender", "Grade", "Email"), show='headings')
    user_tree.heading("ID", text="ID")
    user_tree.heading("Name", text="Name")
    user_tree.heading("Father Name", text="Father's Name")
    user_tree.heading("Gender", text="Gender")
    user_tree.heading("Grade", text="Grade")
    user_tree.heading("Email", text="Email")

    user_tree.pack(fill="both", expand=True, padx=10, pady=10)

    # Buttons
    tk.Button(root, text="Add User", font=("Helvetica", 12, "bold"), bg="#007bff", fg="white", command=add_user).pack(side="left", padx=10, pady=10)
    tk.Button(root, text="Update User", font=("Helvetica", 12, "bold"), bg="#17a2b8", fg="white", command=update_user).pack(side="left", padx=10, pady=10)
    tk.Button(root, text="Delete User", font=("Helvetica", 12, "bold"), bg="#dc3545", fg="white", command=delete_user).pack(side="left", padx=10, pady=10)
    tk.Button(root, text="Refresh", font=("Helvetica", 12, "bold"), bg="#28a745", fg="white", command=load_user_data).pack(side="left", padx=10, pady=10)

    # Load user data
    load_user_data()

    root.mainloop()

# Passcode window
passcode_window = tk.Tk()
passcode_window.title("Enter Passcode")
passcode_window.geometry("300x150")
passcode_window.configure(bg="#2b2b2b")

tk.Label(passcode_window, text="Enter Passcode:", font=("Helvetica", 12, "bold"), bg="#2b2b2b", fg="white").pack(pady=20)
passcode_entry = tk.Entry(passcode_window, font=("Helvetica", 12), bg="#454545", fg="white", show="*")
passcode_entry.pack(pady=10)
tk.Button(passcode_window, text="Submit", font=("Helvetica", 12, "bold"), bg="#007bff", fg="white", command=authenticate_passcode).pack(pady=10)

passcode_window.mainloop()
