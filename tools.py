from cryptography.fernet import Fernet
import hashlib
import os

# Generate a key for encryption
def generate_key():
    return Fernet.generate_key()

# Save the generated key to a file
def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

# Load the key from a file
def load_key(filename='secret.key'):
    with open(filename, 'rb') as key_file:
        return key_file.read()

# Encrypt text using Fernet symmetric encryption
def encrypt_text(key, text):
    f = Fernet(key)
    return f.encrypt(text.encode())

# Decrypt text using Fernet symmetric encryption
def decrypt_text(key, encrypted_text):
    f = Fernet(key)
    return f.decrypt(encrypted_text).decode()

# Hash password using SHA-256
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Encrypt a file using Fernet
def encrypt_file(key, file_path):
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + '.encrypted', 'wb') as file:
        file.write(encrypted_data)

# Decrypt a file using Fernet
def decrypt_file(key, file_path):
    f = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    original_file_path = file_path.replace('.encrypted', '')
    with open(original_file_path, 'wb') as file:
        file.write(decrypted_data)
