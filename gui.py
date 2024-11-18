import tkinter as tk
from tkinter import messagebox, filedialog
from db import create_user_table, register_user, get_user
from tools import hash_password, generate_key, encrypt_text, decrypt_text, encrypt_file, decrypt_file, save_key, load_key
from meowovert import meowovert, convMeow, convOrig
import pyperclip

eky = load_key()

class selAll(tk.Entry):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Control-a>", self.select_all)

     def select_all(self, event):
        # Select all text in the widget
        self.select_range(0, tk.END)
        self.focus_set()  # Focus back on the input box
        return "break"  # Prevent further handling of this event

class MeowCryptGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MeowCrypt")
        create_user_table()

        # User input fields
        self.meow = tk.Label(root, text="/^O w O^\\")
        self.meow.grid(row=0, column=2, padx=10, pady=10)

        self.username_label = tk.Label(root, text="Username")
        self.username_label.grid(row=1, column=1, padx=10, pady=10)
        self.username_entry = selAll(root)
        self.username_entry.grid(row=1, column=2, padx=10, pady=10)

        self.password_label = tk.Label(root, text="Password")
        self.password_label.grid(row=2, column=1, padx=10, pady=10)
        self.password_entry = selAll(root, show='*')
        self.password_entry.grid(row=2, column=2, padx=10, pady=10)

        # Login and Register buttons
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.grid(row=3, column=1, padx=10, pady=10)
        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.grid(row=3, column=2, padx=10, pady=10)

        self.cc = tk.Label(root, text="MeowCrypt - RKS A 2024 Kelompok 5")
        self.cc.grid(row=4, column=2, padx=10, pady=10)

        # Create a frame for the tools page
        self.tools_frame = tk.Frame(root)

        # Encryption tools frame (initially hidden)
        self.encryption_frame = tk.Frame(self.tools_frame)

        # Text encryption fields
        self.text_label = tk.Label(self.encryption_frame, text="Text to Encrypt:")
        self.text_label.grid(row=0, column=0, padx=10, pady=10)
        self.text_entry = selAll(self.encryption_frame)
        self.text_entry.grid(row=1, column=0, padx=20, pady=20)

        self.encrypt_button = tk.Button(self.encryption_frame, text="Encrypt Text", command=self.encrypt_text)
        self.encrypt_button.grid(row=2, column=0, padx=10, pady=10)

        self.clear_decrypt = tk.Button(self.encryption_frame, text="Clear")
        self.clear_decrypt.grid(row=3, column=0, padx=10, pady=10)
        self.clear_decrypt.config(command=lambda: self.text_entry.delete(0, tk.END))

        self.declabel = tk.Label(self.encryption_frame, text="Text to Decrypt:")
        self.declabel.grid(row=0, column=1, padx=10, pady=10)
        self.encrypted_text_entry = selAll(self.encryption_frame)
        self.encrypted_text_entry.grid(row=1, column=1, padx=20, pady=20)

        self.decrypt_button = tk.Button(self.encryption_frame, text="Decrypt Text", command=self.decrypt_text)
        self.decrypt_button.grid(row=2, column=1, padx=10, pady=10)

        self.clear_encrypt = tk.Button(self.encryption_frame, text="Clear")
        self.clear_encrypt.grid(row=3, column=1, padx=10, pady=10)
        self.clear_encrypt.config(command=lambda: self.encrypted_text_entry.delete(0, tk.END))

        self.copy_button = tk.Button(self.encryption_frame, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, column=1, padx=10, pady=10)

        # File encryption buttons
        self.fileEc_label = tk.Label(self.encryption_frame, text="File Encryption")
        self.fileEc_label.grid(row=0, column=2, padx=10, pady=10)

        self.file_button = tk.Button(self.encryption_frame, text="Encrypt File", command=self.encrypt_file)
        self.file_button.grid(row=1, column=2, padx=10, pady=10)

        self.decrypt_file_button = tk.Button(self.encryption_frame, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_file_button.grid(row=2, column=2, padx=10, pady=10)

        self.gotoMeow = tk.Button(self.encryption_frame, text="try Meowovert", command=self.meowGoto)
        self.gotoMeow.grid(row=4, column=3, padx=10, pady=10)

        self.cc1 = tk.Label(self.encryption_frame, text="MeowCrypt - RKS A 2024 Kelompok 5")
        self.cc1.grid(row=5, column=1, padx=10, pady=10)

        self.meowGo = tk.Frame(root)
        self.meowFrame = tk.Frame(self.meowGo)

        self.nyanLabel = tk.Label(self.meowFrame, text="The Meowovert")
        self.nyanLabel.grid(row=0, column=1, padx=10, pady=10)

        self.text_label = tk.Label(self.meowFrame, text="Text to Meowovert:")
        self.text_label.grid(row=1, column=0, padx=10, pady=10)

        self.orig_entry = selAll(self.meowFrame)
        self.orig_entry.grid(row=2, column=0, padx=20, pady=20)

        self.encrypt_button = tk.Button(self.meowFrame, text="Meowovert Text", command=self.convtoMeow)
        self.encrypt_button.grid(row=3, column=0, padx=10, pady=10)

        self.clear_decrypt = tk.Button(self.meowFrame, text="Clear")
        self.clear_decrypt.grid(row=4, column=0, padx=10, pady=10)
        self.clear_decrypt.config(command=lambda: self.orig_entry.delete(0, tk.END))

        self.declabel = tk.Label(self.meowFrame, text="Text to Demeowovert:")
        self.declabel.grid(row=1, column=1, padx=10, pady=10)

        self.meow_entry = selAll(self.meowFrame)
        self.meow_entry.grid(row=2, column=1, padx=20, pady=20)

        self.decrypt_button = tk.Button(self.meowFrame, text="Demeowovert Text", command=self.convtoOrig)
        self.decrypt_button.grid(row=3, column=1, padx=10, pady=10)

        self.clear_encrypt = tk.Button(self.meowFrame, text="Clear")
        self.clear_encrypt.grid(row=4, column=1, padx=10, pady=10)
        self.clear_encrypt.config(command=lambda: self.meow_entry.delete(0, tk.END))

        self.cc2 = tk.Label(self.meowFrame, text="MeowCrypt - RKS A 2024 Kelompok 5")
        self.cc2.grid(row=5, column=1, padx=10, pady=10)

    def register(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return

        hashed_password = hash_password(password)
        try:
            register_user(username, hashed_password)
            messagebox.showinfo("Success", "User  registered successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return

        user = get_user(username)
        if user and user[2] == hash_password(password):
            messagebox.showinfo("Success", "Login successful!")
            self.show_tools_page()  # Show tools page after login
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def show_tools_page(self):
        # Hide login elements
        for widget in self.root.winfo_children():
            widget.grid_forget()

        # Show tools frame
        self.tools_frame.grid()
        self.encryption_frame.grid()

    def meowGoto(self):
        for widget in self.encryption_frame.winfo_children():
            widget.grid_forget()

        self.meowGo.grid()
        self.meowFrame.grid()

    def convtoMeow(self):
        input = self.orig_entry.get().strip()
        if not input:
            messagebox.showerror("Mewror", "Text cannot be meowmpty.")
            return
        encrypted = convMeow(input)
        self.meow_entry.delete(0 , tk.END)  # Clear previous entry
        self.meow_entry.insert(0, encrypted)  # Show encrypted text

    def convtoOrig(self):
        meow_input = self.meow_entry.get().strip()
        if not meow_input:
            messagebox.showerror("Mewror", "Meowoverted text cannot be meowmpty.")
            return
        try:
            decrypted = convOrig(meow_input)

            self.orig_entry.delete(0, tk.END)
            self.orig_entry.insert(0, decrypted)

            # messagebox.showinfo("Meowverted!", f"Decrypted text: {decrypted}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def encrypt_text(self):
        key = eky
        text = self.text_entry.get().strip()
        if not text:
            messagebox.showerror("Error", "Text cannot be empty.")
            return
        encrypted = encrypt_text(key, text)
        self.encrypted_text_entry.delete(0 , tk.END)  # Clear previous entry
        self.encrypted_text_entry.insert(0, encrypted.decode())  # Show encrypted text

    def copy_to_clipboard(self):
        encrypted_text = self.encrypted_text_entry.get().strip()
        if not encrypted_text:
            messagebox.showerror("Error", "No encrypted text to copy.")
            return
        pyperclip.copy(encrypted_text)  # Copy to clipboard
        messagebox.showinfo("Success", "Encrypted text copied to clipboard!")

    def decrypt_text(self):
        key = eky
        encrypted_text = self.encrypted_text_entry.get().strip()
        if not encrypted_text:
            messagebox.showerror("Error", "Encrypted text cannot be empty.")
            return
        try:
            decrypted = decrypt_text(key, encrypted_text.encode())

            self.text_entry.delete(0, tk.END)
            self.text_entry.insert(0, decrypted)

            messagebox.showinfo("Decrypted", f"Decrypted text: {decrypted}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def encrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            key = eky
            encrypt_file(key, file_path)
            messagebox.showinfo("Success", "File encrypted successfully!")

    def decrypt_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            key = eky
            try:
                decrypt_file(key, file_path)
                messagebox.showinfo("Success", "File decrypted successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MeowCryptGUI(root)
    root.mainloop()
