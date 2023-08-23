import tkinter as tk
import random
import string

def generate_password():
    user_name = entry_name.get()
    password_length = int(entry_length.get())

    if user_name:
        # Define the characters to be used in the password generation
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate the password using random characters
        generated_password = ''.join(random.choice(characters) for _ in range(password_length))
        label_generated_password.config(text=f"Generated Password: {generated_password}")
    else:
        label_generated_password.config(text="Please enter your name.")

def reset():
    entry_name.delete(0, tk.END)
    entry_length.delete(0, tk.END)
    label_generated_password.config(text="")

def accept_password():
    accepted_password = label_generated_password.cget("text").split()[-1]
    listbox_passwords.insert(tk.END, accepted_password)

# Create the main application window
app = tk.Tk()
app.title("Password Generator")
app.geometry("400x600")
app.config(background="red", border="2",borderwidth="3")


label_title = tk.Label(app, text="PASSWORD GENERATOR",underline="0", font=("Helvetica", 20) , bg="#BFF8F6")
label_title.pack(pady=15)

# Create and configure the widget for user name input
label_name = tk.Label(app, text="Enter your name:", bg="#BFF8F6" , font=("Arial", 12))
label_name.pack(pady=10)
entry_name = tk.Entry(app, font=("Arial", 12))
entry_name.pack(pady=5)

# Create and configure the widget for password length input
label_length = tk.Label(app, text="Enter password length:", bg="#BFF8F6" , font=("Arial", 12))
label_length.pack(pady=10)
entry_length = tk.Entry(app, font=("Arial", 12))
entry_length.pack(pady=5)

# Create and configure the button to generate the password
btn_generate = tk.Button(app, text="Generate Password", bg="#BFF8F6" , command=generate_password, font=("Arial", 12))
btn_generate.pack(pady=10)

# Create a label to display the generated password
label_generated_password = tk.Label(app, text="Displaying The Password Here",bg="#BFF8F6" , font=("Arial", 12))
label_generated_password.pack()

# Create and configure the "Accept" button to accept the generated password
btn_accept = tk.Button(app, text="Accept", command=accept_password,bg="Yellow" , font=("Arial", 12))
btn_accept.pack(pady=5)

# Create and configure the "Reset" button to reset the inputs and generated password
btn_reset = tk.Button(app, text="Reset", command=reset,bg="Yellow" ,  font=("Arial", 12))
btn_reset.pack(pady=5)

# Create a "Password Section" to display the accepted passwords
label_password_section = tk.Label(app, text="Accepted Password",bg="#BFF8F6" ,font=("Arial", 12),border="6")
label_password_section.pack(pady=5)

listbox_passwords = tk.Listbox(app, font=("Arial", 12), width=20, height=2)
listbox_passwords.pack(pady=5)

# Start the application event loop
app.mainloop()
