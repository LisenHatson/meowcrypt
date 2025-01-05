import tkinter as tk
from tkinter import messagebox, filedialog, Tk, Canvas, Entry, Button, PhotoImage
from db import create_user_table, register_user, get_user
from tools import hash_password, generate_key, encrypt_text, decrypt_text, encrypt_file, decrypt_file, save_key, load_key
from vert import meowovert, convMeow, convOrig
import pyperclip
import re

eky = load_key()

class selAll(tk.Entry):
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bind("<Control-a>", self.select_all)

     def select_all(self, event):
        self.select_range(0, tk.END)
        self.focus_set()
        return "break"


# Main GUI
class MeowCryptGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("MeowCrypt")
        self.root.geometry("800x600")
        self.root.configure(bg="#9e6df7")
        self.root.resizable(False, False)
        self.canvas = Canvas(
                self.root,
                bg="#9e6df7",
                height=600,
                width=800,
                bd=0,
                highlightthickness=0,
                relief="ridge"
                )
        self.canvas.place(x=0, y=0)

        self.loginpage()

    def loginpage(self):
        create_user_table()

        self.bg_update("./assets/Aloginpagemain.png")
        self.entry_img = PhotoImage(file=("./assets/entry.png"))

        self.canvas.create_image(400.0, 257.0, image=self.entry_img)
        self.entry_user = Entry(
                bd=0,
                bg="#ffffff",
                fg="#000716",
                highlightthickness=0,
                font=("Montserrat", 15))
        self.entry_user.place(x=235.0, y=233.0, width=300.0, height=45.0)

        self.canvas.create_image(400.0, 340.0, image=self.entry_img)
        self.entry_pass = Entry(
                bd=0,
                bg="#ffffff",
                fg="#000716",
                highlightthickness=0,
                show="*",
                font=("Montserrat", 15))
        self.entry_pass.place(x=235.0, y=316.0, width=300.0, height=45.0)

        self.aboutusbutton_img = PhotoImage(file=("./assets/boutusbutton.png"))
        self.aboutusbutton = Button(
                image=self.aboutusbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.show_aboutus,
                relief="flat",
                bg="#9e6df7", activebackground="#9e6df7"
                )
        self.aboutusbutton.place(x=46.0, y=450.0, width=120.0, height=120.0)

        self.logbutton_img = PhotoImage(file=("./assets/logbutton.png"))
        self.logbutton = Button(
                image=self.logbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.login,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.logbutton.place(x=225.0, y=395.0, width=350.0, height=70.0)

        self.regbutton_img = PhotoImage(file=("./assets/regbutton.png"))
        self.regbutton = Button(
                image=self.regbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.register,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.regbutton.place(x=225.0, y=480.0, width=350.0, height=70.0)

    def toolspage(self):
        self.bg_update("./assets/Atoolspagemain.png")

        self.outbutton_img = PhotoImage(file=("./assets/outbutton.png"))
        self.outbutton = Button(
                image=self.outbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.signout,
                relief="flat",
                bg="#9e6df7", activebackground="#9e6df7"
                )
        self.outbutton.place(x=615.0, y=500.0, width=150.0, height=60.0)

        self.meowbutton_img = PhotoImage(file=("./assets/meowbutton.png"))
        self.meowbutton = Button(
                image=self.meowbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.show_meow,
                relief="flat",
                bg="#9e6df7", activebackground="#9e6df7"
                )
        self.meowbutton.place(x=275.0, y=500.0, width=250.0, height=60.0)

        self.filebutton_img = PhotoImage(file=("./assets/filebutton.png"))
        self.filebutton = Button(
                image=self.filebutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.encrypt_file,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.filebutton.place(x=434.0, y=76.0, width=310.0, height=190.0)

        self.dfilebutton_img = PhotoImage(file=("./assets/dfilebutton.png"))
        self.dfilebutton = Button(
                image=self.dfilebutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.decrypt_file,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.dfilebutton.place(x=434.0, y=277.0, width=310.0, height=190.0)

        self.entry_img = PhotoImage(file=("./assets/entry1.png"))

        self.canvas.create_image(209.0, 135.0, image=self.entry_img)
        self.entry_input = Entry(
                bd=0,
                bg="#ffffff",
                fg="#000716",
                highlightthickness=0,
                font=("Montserrat", 15))
        self.entry_input.place(x=64.0, y=111.0, width=290.0, height=45.0)

        self.canvas.create_image(209.0, 366.0, image=self.entry_img)
        self.entry_output = Entry(
                bd=0,
                bg="#ffffff",
                fg="#000716",
                highlightthickness=0,
                font=("Montserrat", 15))
        self.entry_output.place(x=64.0, y=342.0, width=290.0, height=45.0)

        self.encryptbutton_img = PhotoImage(file=("./assets/encryptbutton.png"))
        self.encryptbutton = Button(
                image=self.encryptbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.encrypt_text,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.encryptbutton.place(x=54.0, y=174.0, width=310.0, height=60.0)

        self.decryptbutton_img = PhotoImage(file=("./assets/decryptbutton.png"))
        self.decryptbutton = Button(
                image=self.decryptbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.decrypt_text,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.decryptbutton.place(x=54.0, y=248.0, width=310.0, height=60.0)

        self.copybutton_img = PhotoImage(file=("./assets/copybutton.png"))
        self.copybutton = Button(
                image=self.copybutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.copy_to_clipboard,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.copybutton.place(x=54.0, y=403.0, width=310.0, height=60.0)

    def meowovertpage(self):
        self.bg_update("./assets/Ameowovertpagemain.png")

        self.backbutton_img = PhotoImage(file=("./assets/meowback.png"))
        self.backbutton = Button(
                image=self.backbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.meowback,
                relief="flat",
                bg="#9e6df7", activebackground="#9e6df7"
                )
        self.backbutton.place(x=29.0, y=514.0, width=120.0, height=60.0)

        self.entry_img = PhotoImage(file=("./assets/meowentry.png"))

        self.canvas.create_image(400.0, 130.5, image=self.entry_img)
        self.entry_inputm = Entry(
                bd=0,
                bg="#ffffff",
                fg="#000716",
                highlightthickness=0,
                font=("Montserrat", 15))
        self.entry_inputm.place(x=185.0, y=105.0, width=430.0, height=53.0)

        self.canvas.create_image(400.0, 379.5, image=self.entry_img)
        self.entry_output = Entry(
                bd=0,
                bg="#ffffff",
                fg="#000716",
                highlightthickness=0,
                font=("Montserrat", 15))
        self.entry_output.place(x=185.0, y=354.0, width=430.0, height=53.0)

        self.encryptbutton_img = PhotoImage(file=("./assets/meowencryptbutton.png"))
        self.encryptbuttonm = Button(
                image=self.encryptbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.convtoMeow,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.encryptbuttonm.place(x=175.0, y=168.0, width=450.0, height=70.0)

        self.decryptbutton_img = PhotoImage(file=("./assets/meowdecryptbutton.png"))
        self.decryptbuttonm = Button(
                image=self.decryptbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.convtoOrig,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.decryptbuttonm.place(x=175.0, y=248.0, width=450.0, height=70.0)

        self.copybutton_img = PhotoImage(file=("./assets/meowcopybutton.png"))
        self.copybutton = Button(
                image=self.copybutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.copy_to_clipboard,
                relief="flat",
                bg="#d2b9ff", activebackground="#d2b9ff"
                )
        self.copybutton.place(x=175.0, y=419.0, width=450.0, height=70.0)

    def aboutuspage(self):
        self.bg_update("./assets/Aaboutuspagemain.png")

        self.backbutton_img = PhotoImage(file=("./assets/backbutton.png"))
        self.backbutton = Button(
                image=self.backbutton_img,
                borderwidth=0,
                highlightthickness=0,
                command=self.signout,
                relief="flat",
                bg="#9e6df7", activebackground="#9e6df7"
                )
        self.backbutton.place(x=33.0, y=500.0, width=150.0, height=60.0)

    # Command functions

    def bg_update(self, img):
        if self.canvas:  # Check if the canvas is still valid
            self.pagebg = PhotoImage(file=(img))
            self.canvas.create_image(400.0, 300.0, image=self.pagebg)
        else:
            messagebox.showerror("Error", "Canvas is not available.")

    def register(self):
        username = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Error", "Username and password cannot be empty.")
            return

        if len(password) < 8:
            messagebox.showwarning("Input Error", "Password must be at least 8 characters long.")
            return

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            messagebox.showwarning("Input Error", "Password must contain at least one special character.")
            return

        # Check if password contains at least one uppercase letter
        if not re.search(r"[A-Z]", password):
            messagebox.showwarning("Input Error", "Password must contain at least one uppercase letter.")
            return

        if not re.search(r"\d", password):
            messagebox.showwarning("Input Error", "Password must contain at least one number.")
            return

        hashed_password = hash_password(password)
        try:
            register_user(username, hashed_password)
            messagebox.showinfo("Success", "User  registered successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def login(self):
        username = self.entry_user.get().strip()
        password = self.entry_pass.get().strip()

        if not username or not password:
            messagebox.showerror("Error", "Username and password cannot be empty.")
            return

        user = get_user(username)
        if user and user[2] == hash_password(password):
            messagebox.showinfo("Success", "Login successful!")
            self.show_tools_page()  # Show tools page after login
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def clear_page(self):
        # Instead of destroying the canvas, just hide its contents
        for widget in self.root.winfo_children():
            if widget != self.canvas:  # Keep the canvas
                widget.destroy()


    def show_tools_page(self):
        self.clear_page()
        self.toolspage()

    def show_meow(self):
        self.clear_page()
        self.meowovertpage()

    def show_aboutus(self):
        self.clear_page()
        self.aboutuspage()

    def signout(self):
        self.clear_page()
        self.loginpage()

    def meowback(self):
        self.clear_page()
        self.toolspage()

    def convtoMeow(self):
        input = self.entry_inputm.get().strip()
        if not input:
            messagebox.showerror("Mewror", "Text cannot be meowmpty.")
            return
        encrypted = convMeow(input)
        self.entry_output.delete(0 , tk.END)  # Clear previous entry
        self.entry_output.insert(0, encrypted)  # Show encrypted text

    def convtoOrig(self):
        meow_input = self.entry_inputm.get().strip()
        if not meow_input:
            messagebox.showerror("Mewror", "Meowoverted text cannot be meowmpty.")
            return
        try:
            decrypted = convOrig(meow_input)

            self.entry_output.delete(0 , tk.END)  # Clear previous entry
            self.entry_output.insert(0, decrypted)  # Show encrypted text

            # messagebox.showinfo("Meowverted!", f"Decrypted text: {decrypted}")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def encrypt_text(self):
        key = eky
        text = self.entry_input.get().strip()
        if not text:
            messagebox.showerror("Error", "Text cannot be empty.")
            return
        encrypted = encrypt_text(key, text)
        self.entry_output.delete(0 , tk.END)  # Clear previous entry
        self.entry_output.insert(0, encrypted.decode())  # Show encrypted text

    def copy_to_clipboard(self):
        encrypted_text = self.entry_output.get().strip()
        if not encrypted_text:
            messagebox.showerror("Error", "No encrypted text to copy.")
            return
        pyperclip.copy(encrypted_text)  # Copy to clipboard
        messagebox.showinfo("Success", "Encrypted text copied to clipboard!")

    def decrypt_text(self):
        key = eky
        encrypted_text = self.entry_input.get().strip()
        if not encrypted_text:
            messagebox.showerror("Error", "Encrypted text cannot be empty.")
            return
        try:
            decrypted = decrypt_text(key, encrypted_text.encode())

            self.entry_output.delete(0, tk.END)
            self.entry_output.insert(0, decrypted)

            # messagebox.showinfo("Decrypted", f"Decrypted text: {decrypted}")
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

# Initiate the loop
if __name__ == "__main__":
    root = tk.Tk()
    app = MeowCryptGUI(root)
    root.mainloop()
