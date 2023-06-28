from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import tkinter as tk
from tkinter import filedialog
import os

# Encryption function
def encrypt_text(key, text):
    # Generate a random initialization vector (IV)
    iv = get_random_bytes(AES.block_size)
    
    # Create the AES cipher object with the provided key and AES.MODE_CBC mode
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Pad the text to be a multiple of the block size
    padded_text = pad(text.encode(), AES.block_size)
    
    # Encrypt the padded text
    encrypted_text = cipher.encrypt(padded_text)
    
    # Return the IV and encrypted text as bytes
    return iv + encrypted_text

# Decryption function
def decrypt_text(key, encrypted_text):
    # Extract the IV from the encrypted text
    iv = encrypted_text[:AES.block_size]
    
    # Create the AES cipher object with the provided key, AES.MODE_CBC mode, and the extracted IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt the encrypted text
    decrypted_text = cipher.decrypt(encrypted_text[AES.block_size:])
    
    # Remove the padding from the decrypted text
    unpadded_text = unpad(decrypted_text, AES.block_size)
    
    # Return the decrypted text as a string
    return unpadded_text.decode()

# Function to handle the encryption button click
def encrypt_file():
    # Prompt the user to select a file for encryption
    file_path = filedialog.askopenfilename(title="Select File for Encryption")
    
    # Read the text from the selected file
    with open(file_path, "r") as file:
        text = file.read().strip()
    
    # Encrypt the text
    encrypted_text = encrypt_text(key, text)
    
    # Create a new file with the encrypted data
    encrypted_file_path = file_path 
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_text)
    
    # Update the status label with success message
    status_label.config(text="Encryption completed successfully. Encrypted data saved in : \n" + encrypted_file_path, fg="green")

# Function to handle the decryption button click
def decrypt_file():
    # Prompt the user to select a file for decryption
    file_path = filedialog.askopenfilename(title="Select File for Decryption")
    
    # Read the encrypted data from the selected file
    with open(file_path, "rb") as encrypted_file:
        encrypted_text = encrypted_file.read()
    
    # Decrypt the data
    decrypted_text = decrypt_text(key, encrypted_text)
    
    # Create a new file with the decrypted data
    decrypted_file_path = file_path 
    with open(decrypted_file_path, "w") as decrypted_file:
        decrypted_file.write(decrypted_text)
    
    # Optional Remove the encrypted file
    #os.remove(file_path)
    
    # Update the status label with success message
    status_label.config(text="Decryption completed successfully. Decrypted data saved in : \n" + decrypted_file_path, fg="green")

# Define the encryption key (must be 16, 24, or 32 bytes long)
key = b'This is a 16, 24, or 32-byte key'

# Create the GUI window
window = tk.Tk()
window.title("-                         Encryption and Decryption - By Ahmed Rifai")
window.configure(bg="#E38AAE")

# Create a frame for the buttons
frame = tk.Frame(window, bg="#E38AAE")
frame.pack(ipadx=150,ipady=100)

# Create the encryption button
encrypt_button = tk.Button(frame, text="Encrypt", command=encrypt_file, bg="#FFC0CB", fg="white", font=("Tempus Sans ITC", 20))
encrypt_button.pack(side=tk.LEFT, ipadx=5,ipady=5, expand=True)

# Create the decryption button
decrypt_button = tk.Button(frame, text="Decrypt", command=decrypt_file, bg="#87CEFA", fg="white", font=("Tempus Sans ITC", 20))
decrypt_button.pack(side=tk.LEFT, ipadx=5,ipady=5, expand=True)

# Create a label for status messages
status_label = tk.Label(window, text="", bg="#87CEFA", fg="black", font=("Tempus Sans ITC", 18))
status_label.pack(pady=20)

# Start the GUI event loop
window.mainloop()
