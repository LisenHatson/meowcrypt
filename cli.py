import sys
from db import create_user_table, register_user, get_user
from tools import hash_password, generate_key, encrypt_text, decrypt_text, encrypt_file, decrypt_file

def cli():
    create_user_table()
    while True:
        action = input("Enter 'register' to create a new user or 'login' to access your account: ").strip().lower()
        if action == 'register':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if not username or not password:
                print("Username and password cannot be empty.")
                continue
            hashed_password = hash_password(password)
            try:
                register_user(username, hashed_password)
                print("User  registered successfully!")
            except Exception as e:
                print(f"Error: {e}")
        elif action == 'login':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            if not username or not password:
                print("Username and password cannot be empty.")
                continue
            user = get_user(username)
            if user and user[2] == hash_password(password):
                print("Login successful!")
                # Proceed to encryption tools
                while True:
                    tool_action = input("Enter 'encrypt' to encrypt text, 'decrypt' to decrypt text, or 'exit' to logout: ").strip().lower()
                    if tool_action == 'encrypt':
                        text = input("Enter text to encrypt: ").strip()
                        if not text:
                            print("Text cannot be empty.")
                            continue
                        key = generate_key()
                        encrypted = encrypt_text(key, text)
                        print(f"Encrypted text: {encrypted.decode()}")
                    elif tool_action == 'decrypt':
                        encrypted_text = input("Enter encrypted text: ").strip()
                        if not encrypted_text:
                            print("Encrypted text cannot be empty.")
                            continue
                        try:
                            decrypted = decrypt_text(key, encrypted_text.encode())
                            print(f"Decrypted text: {decrypted}")
                        except Exception as e:
                            print(f"Decryption failed: {str(e)}")
                    elif tool_action == 'exit':
                        break
                    else:
                        print("Invalid action. Please try again.")
            else:
                print("Invalid credentials!")
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    cli()
