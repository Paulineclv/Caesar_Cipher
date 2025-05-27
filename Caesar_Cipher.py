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

    # Ask user what they want to do 
    mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
    else:
        text = input("Enter the text: ")
        try:
            shift = int(input("Enter the shift number (e.g. 3): "))
            result = caesar_cipher(text, shift, mode)
            print(f"\nResult: {result}")
        except ValueError:
            print("Shift must be a number.")