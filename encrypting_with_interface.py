import tkinter as tk
from tkinter import filedialog, messagebox


def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Checking if a character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Keep non-alphabetic characters unchanged
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decryption is negative-shift encryption


def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_text(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


def encrypt_text():
    try:
        shift = int(shift_entry.get()) % 26  # Get the shift value from the entry
        input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])

        if not input_file_path:
            return  # Exit if no file is selected

        original_text = load_text(input_file_path)  # Load the original text
        encrypted_text = caesar_encrypt(original_text, shift)  # Encrypt the text

        output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Encrypted File",
                                                        filetypes=[("Text files", "*.txt")])

        if output_file_path:
            save_text(output_file_path, encrypted_text)  # Save the encrypted text
            messagebox.showinfo("Success", "Text encrypted and saved successfully.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift value.")


def decrypt_text():
    try:
        shift = int(shift_entry.get()) % 26  # Get the shift value
        input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])

        if not input_file_path:
            return  # Exit if no file is selected

        encrypted_text = load_text(input_file_path)  # Load the encrypted text
        decrypted_text = caesar_decrypt(encrypted_text, shift)  # Decrypt the text

        output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Decrypted File",
                                                        filetypes=[("Text files", "*.txt")])

        if output_file_path:
            save_text(output_file_path, decrypted_text)  # Save the decrypted text
            messagebox.showinfo("Success", "Text decrypted and saved successfully.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift value.")


# Set up the main window
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")
root.geometry("300x200")

# Shift label and entry
shift_label = tk.Label(root, text="Shift:")
shift_label.pack(pady=10)
shift_entry = tk.Entry(root)
shift_entry.pack(pady=5)

# Encryption button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack(pady=10)

# Decryption button
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack(pady=10)

# Run the application
root.mainloop()
