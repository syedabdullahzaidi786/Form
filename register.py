import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to save the registration data
def save_registration():
    student_id = entry_student_id.get()
    name = entry_name.get()
    father_name = entry_father_name.get()
    gender = gender_var.get()
    grade = grade_var.get()
    email = entry_email.get()

    if not (student_id and name and father_name and gender and grade and email):
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    
    with open("registrations.txt", "a") as file:
        file.write(f"{student_id},{name},{father_name},{gender},{grade},{email}\n")
    
    messagebox.showinfo("Success", "Registration Successful!")
    entry_student_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_father_name.delete(0, tk.END)
    gender_var.set("")
    grade_var.set("")
    entry_email.delete(0, tk.END)

# Main UI window
root = tk.Tk()
root.title("DIF Exam Registration")
root.geometry("500x600")
root.configure(bg="#f0f4f8")

# Title Frame
title_frame = tk.Frame(root, bg="#343a40", height=100)
title_frame.pack(fill="x")

# Logo
logo = tk.PhotoImage(file="logo.png")  # Ensure logo.png file is in the same directory
logo = logo.subsample(2)  # Resize the logo
logo_label = tk.Label(title_frame, image=logo, bg="#343a40")
logo_label.pack(pady=10)

# Title Label
title_label = tk.Label(title_frame, text="DIF Exam Registration", font=("Helvetica", 18, "bold"), fg="white", bg="#343a40")
title_label.pack(pady=5)

# Form Frame
form_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, relief="solid", borderwidth=2)
form_frame.pack(pady=20, fill="both", expand=True)

# Form labels and entries
fields = [
    ("Student ID:", "entry_student_id"),
    ("Name:", "entry_name"),
    ("Father's Name:", "entry_father_name"),
    ("Gender:", "gender"),
    ("Grade:", "grade"),
    ("Email Address:", "entry_email")
]

for index, (label_text, var_name) in enumerate(fields):
    label = tk.Label(form_frame, text=label_text, font=("Helvetica", 12), bg="#ffffff", anchor="w")
    label.grid(row=index, column=0, pady=10, padx=10, sticky="w")

    if var_name.startswith("entry"):
        entry = tk.Entry(form_frame, font=("Helvetica", 12), width=40, borderwidth=1, relief="solid")
        entry.grid(row=index, column=1, pady=10, padx=10)
        globals()[var_name] = entry
    elif var_name == "gender":
        gender_var = tk.StringVar()
        gender_frame = tk.Frame(form_frame, bg="#ffffff")
        gender_male = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", font=("Helvetica", 12), bg="#ffffff")
        gender_female = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", font=("Helvetica", 12), bg="#ffffff")
        gender_male.pack(side="left", padx=5)
        gender_female.pack(side="left", padx=5)
        gender_frame.grid(row=index, column=1, pady=10, padx=10, sticky="w")
    elif var_name == "grade":
        grade_var = tk.StringVar()
        grade_menu = ttk.Combobox(form_frame, textvariable=grade_var, font=("Helvetica", 12), values=["Grade 8", "Grade 9"], state="readonly", width=38)
        grade_menu.grid(row=index, column=1, pady=10, padx=10)

# Submit Button
def on_enter(e):
    submit_button.config(bg="#218838", fg="white")

def on_leave(e):
    submit_button.config(bg="#28a745", fg="white")

submit_button = tk.Button(root, text="Submit", font=("Helvetica", 14, "bold"), bg="#28a745", fg="white", relief="flat", padx=20, pady=10, command=save_registration)
submit_button.pack(pady=20)

# Bind hover effects
submit_button.bind("<Enter>", on_enter)
submit_button.bind("<Leave>", on_leave)

# Run the application
root.mainloop()
