import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 8:
        password_label.config(text="Password length should be at least 8 characters.", fg="red")
        return

    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    all_characters = lowercase + numbers + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))
    password_label.config(text=f"Generated Password: {password}", fg="green")

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("700x500")  # Set window size (width x height)
root.configure(bg="#f0f0f0")  # Set background color

# Create a label for the length entry
length_label = tk.Label(root, text="Enter the desired length of the password:", bg="#f0f0f0", font=("Arial", 14))
length_label.pack(pady=10)

# Create an entry box for user input
length_entry = tk.Entry(root, font=("Arial", 14))
length_entry.pack(pady=5)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 14))
generate_button.pack(pady=10)

# Create a label to display the generated password
password_label = tk.Label(root, text="", bg="#f0f0f0", font=("Arial", 14))
password_label.pack(pady=10)

# Run the application
root.mainloop()
