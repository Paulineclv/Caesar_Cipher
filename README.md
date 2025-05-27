# 🛡️ Caesar Cipher in Python 🔐

A simple Python implementation of the Caesar Cipher algorithm for encrypting and decrypting text.

## ✨ Features

-   🔄 Encrypt text by shifting letters by a specified number.
-   🔙 Decrypt text by reversing the shift.
-   🔠 Preserves letter case (uppercase and lowercase).
-   🚫 Non-alphabetical characters remain unchanged.

## 🚀 Usage

```python
from caesar_cipher import caesar_cipher

# 🔒 Encrypting a message
encrypted = caesar_cipher("Hello World!", 3, mode='encrypt')
print("Encrypted:", encrypted)  # Outputs: Khoor Zruog!

# 🔓 Decrypting a message
decrypted = caesar_cipher(encrypted, 3, mode='decrypt')
print("Decrypted:", decrypted)  # Outputs: Hello World!
```

## 📋 Function Signature

```python
def caesar_cipher(text: str, shift: int, mode: str = 'encrypt') -> str:
    """
    Encrypts or decrypts text using Caesar Cipher.

    Parameters:
    - text (str): The message to encrypt or decrypt.
    - shift (int): Number of letters to shift.
    - mode (str): 'encrypt' to encode, 'decrypt' to decode.

    Returns:
    - str: The resulting encrypted or decrypted text.
    """
```

## 🏃 How to Run

1. 📥 Clone this repository.

2. 📂 Import the function caesar_cipher in your Python script.

3. 🔧 Use it to encrypt or decrypt your messages.

## 📄 License

This project is licensed under the MIT License.

Made with curiosity and code by CALVO Pauline 🚀.
