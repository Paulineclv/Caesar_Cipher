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

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


if __name__ == "__main__":
    print("🔐 Caesar Cipher Tool")

    while True:
        # Select mode
        mode = input("Choose mode (encrypt/decrypt): ").strip().lower()
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
            continue

        # Load text from file or input manually
        use_file = input("Do you want to load the text from a file? (y/n): ").strip().lower()
        if use_file == 'y':
            filename = input("Enter the filename (e.g. input.txt): ").strip()
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    text = f.read()
                    print(f"Loaded text:\n{text}")
            except FileNotFoundError:
                print("File not found. Using manual input.")
                text = input("Enter the text: ")
        else:
            text = input("Enter the text: ")

        # Shift number
        while True:
            try:
                shift = int(input("Enter the shift number (e.g. 3): "))
                break
            except ValueError:
                print("Shift must be a valid number.")

        result = caesar_cipher(text, shift, mode)
        print(f"\n Result:\n{result}")

        # Ask to save the result
        save = input("\nDo you want to save the result to a file? (y/n): ").strip().lower()
        if save == 'y':
            output_file = input("Enter the filename to save to (e.g. result.txt): ").strip()
            try:
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(result)
                print(f"Result saved to {output_file}")
            except IOError as e:
                print(f"Could not save file: {e}")

        # Ask if the user wants to run again
        again = input("\nDo you want to run another encryption/decryption? (y/n): ").strip().lower()
        if again != 'y':
            print("👋 Goodbye!")
            break
