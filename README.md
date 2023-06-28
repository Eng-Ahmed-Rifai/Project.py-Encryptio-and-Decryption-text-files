# Project: Encryption and Decryption

## Code Description
The code provided in this project allows for the encryption and decryption of text data using the Advanced Encryption Standard (AES) algorithm. It provides functions to encrypt and decrypt text using a user-provided key and save the encrypted and decrypted data to separate files.

## Libraries Used
The code utilizes the following libraries:
- `Crypto.Cipher.AES` from the `pycryptodome` library: Provides the AES cipher implementation for encryption and decryption.
- `Crypto.Util.Padding` from the `pycryptodome` library: Offers functions for padding and unpadding data to fit the AES block size.
- `Crypto.Random.get_random_bytes` from the `pycryptodome` library: Generates random bytes for the initialization vector (IV) in AES encryption.
- `tkinter` library: Provides the graphical user interface (GUI) functionality for file selection and display of success messages.
- `os` library: Used for removing the encrypted file after decryption (optional).

## Benefits of the technology used in the project
- AES encryption is a widely used and highly secure encryption algorithm.
- The `pycryptodome` library provides a reliable implementation of the AES algorithm.
- `tkinter` is a built-in library in Python that allows for the creation of GUI applications without the need for external dependencies.

## Code Structure
The code follows a modular structure, separating the encryption and decryption functionality into separate functions. It also incorporates a GUI interface for file selection and displaying success messages.

1. Encryption:
   - The `encrypt_text` function takes a key and text as inputs, generates a random IV, and encrypts the text using AES encryption in CBC mode.
   - The `encrypt_file` function prompts the user to select a file, reads the text from the file, encrypts it using `encrypt_text`, and saves the encrypted data to a new file.

2. Decryption:
   - The `decrypt_text` function takes a key and encrypted text as inputs, extracts the IV from the encrypted text, and decrypts the text using AES decryption in CBC mode.
   - The `decrypt_file` function prompts the user to select a file, reads the encrypted data from the file, decrypts it using `decrypt_text`, and saves the decrypted data to a new file.

## Author
This mini project was developed by Ahmed Rifai.
