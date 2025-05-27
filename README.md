# 🔐 Caesar Cipher Tool

A simple **Caesar Cipher** implementation in Python with an easy-to-use command line interface (CLI).  
Encrypt or decrypt text by shifting letters in the alphabet. Perfect for beginners learning about encryption!

---

## 📚 What is a Caesar Cipher?

The Caesar Cipher is one of the oldest known encryption techniques.  
It works by shifting the letters of the alphabet by a certain number of steps.  
For example, shifting `A` by 3 gives you `D`.

---

## 🚀 Features

-   🔄 **Encrypt** or **decrypt** text using Caesar Cipher
-   📂 **Load text from a file** or enter it manually
-   💾 **Save the result** to a file
-   🔁 **Run multiple times** without restarting the program
-   🛡️ Handles both uppercase and lowercase letters, keeps punctuation intact

---

## 💻 How to Use

1. Run the script:

```bash
    python caesar_cipher.py
```

2. Run the script in a terminal:

Choose a mode: `encrypt` or `decrypt`

3. Decide if you want to load the text from a file or input manually

4. Enter the shift number (an integer)

5. View the encrypted/decrypted result

6. Optionally save the result to a file

7. Repeat as many times as you want!

---

## ⚙️ Example

```bash
🔐 Caesar Cipher Tool
Choose mode (encrypt/decrypt): encrypt
Do you want to load the text from a file? (y/n): n
Enter the text: Hello World!
Enter the shift number (e.g. 3): 3

Result:
Khoor Zruog!

Do you want to save the result to a file? (y/n): y
Enter the filename to save to (e.g. result.txt): output.txt
Result saved to output.txt

Do you want to run another encryption/decryption? (y/n): n
👋 Goodbye!
```

---

## 🧠 Learnings

This small project covers:

-   Loops (for)

-   Conditionals (if/else)

-   ASCII operations with ord() and chr()

-   Command-line input with input()

-   Defensive programming with basic error handling

---

## 🤝 Contributions

Feel free to open issues or submit pull requests to improve this tool!

---

## 📄 License

This project is licensed under the MIT License.

Made with curiosity and code by CALVO Pauline 🚀.
