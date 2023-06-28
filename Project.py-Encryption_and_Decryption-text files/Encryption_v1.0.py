from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

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

# Define the encryption key (must be 16, 24, or 32 bytes long)
key = b'This is a 16, 24, or 32-byte key'

# Read the text from the file
file_path = r"C:\Users\modem\Downloads\New\Password.txt"
with open(file_path, "r") as file:
    text = file.read().strip()

# Encrypt the text
encrypted_text = encrypt_text(key, text)

# Create a new file with the encrypted data
encrypted_file_path = r"C:\Users\modem\Downloads\New\EncryptedData.txt"
with open(encrypted_file_path, "wb") as encrypted_file:
    encrypted_file.write(encrypted_text)
