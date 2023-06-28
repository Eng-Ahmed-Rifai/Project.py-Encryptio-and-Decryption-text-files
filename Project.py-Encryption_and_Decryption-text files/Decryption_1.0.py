from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

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

# Read the encrypted data from the file
encrypted_file_path = r"C:\Users\modem\Downloads\New\EncryptedData.txt"
with open(encrypted_file_path, "rb") as encrypted_file:
    encrypted_text = encrypted_file.read()

# Decrypt the data
decrypted_text = decrypt_text(key, encrypted_text)

# Create a new file with the decrypted data
decrypted_file_path = r"C:\Users\modem\Downloads\New\DecryptedData.txt"
with open(decrypted_file_path, "w") as decrypted_file:
    decrypted_file.write(decrypted_text)
