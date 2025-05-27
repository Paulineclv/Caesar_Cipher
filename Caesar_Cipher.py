def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypts or decrypts text using Caesar Cipher.
    
    Parameters:
    - text (str): The message to encrypt or decrypt.
    - shift (int): Number of letters to shift.
    - mode (str): 'encrypt' to encode, 'decrypt' to decode.
    
    Returns:
    - str: The resulting encrypted or decrypted text.
    """
    result = ""
    
    # If decrypting, reverse the shift
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():  # Only shift letters
            # Preserve case
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around the alphabet
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Keep non-letter characters unchanged
            result += char
    
    return result

if __name__ == "__main__":
    print("🔐 Caesar Cipher Tool")

    # Loop until a valid mode is selected
    while True:
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode in ['encrypt', 'decrypt']:
            break
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")

    text = input("Enter the text: ")

    # Loop until a valid shift number is entered
    while True:
        try:
            shift = int(input("Enter the shift number (e.g. 3): "))
            break
        except ValueError:
            print("Shift must be a valid number. Please try again.")

    result = caesar_cipher(text, shift, mode)
    print(f"\nResult: {result}")

