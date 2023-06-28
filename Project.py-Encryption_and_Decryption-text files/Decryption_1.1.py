from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename

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

# Define the encryption key (must be 16, 24, or 32 bytes long)
key = b'This is a 16, 24, or 32-byte key'

# Create a Tkinter root window
root = Tk()
root.withdraw()

# Prompt the user to select a file for decryption
file_path = askopenfilename(title="Select File for Decryption")

# Read the encrypted data from the selected file
with open(file_path, "rb") as encrypted_file:
    encrypted_text = encrypted_file.read()

# Decrypt the data
decrypted_text = decrypt_text(key, encrypted_text)

# Create a new file with the decrypted data
decrypted_file_path = file_path
with open(decrypted_file_path, "w") as decrypted_file:
    decrypted_file.write(decrypted_text)

print("Decryption completed successfully. Decrypted data saved in", decrypted_file_path)

# Remove the encrypted file
# os.remove(file_path)
