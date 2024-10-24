import tkinter as tk
from tkinter import filedialog, messagebox
from caesar_class import CaesarEncryptDecrypt


def perform_encryption():
    try:
        shift = int(shift_entry.get()) % 26  # Getting Shift
        input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])
        if not input_file_path:
            return
        output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Encrypted File",
                                                        filetypes=[("Text files", "*.txt")])
        if not output_file_path:
            return
        cipher_tool = CaesarEncryptDecrypt(shift, input_file_path, output_file_path)
        cipher_tool.encrypt_file()  # Encryption into the file
        messagebox.showinfo("Success", "Text encrypted and saved successfully.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift value.")


def perform_decryption():
    try:
        shift = int(shift_entry.get()) % 26  # Getting Shift
        input_file_path = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])
        if not input_file_path:
            return
        output_file_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Decrypted File",
                                                        filetypes=[("Text files", "*.txt")])
        if not output_file_path:
            return
        cipher_tool = CaesarEncryptDecrypt(shift, input_file_path, output_file_path)
        cipher_tool.decrypt_file()
        messagebox.showinfo("Success", "Text decrypted and saved successfully.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid shift value.")

if __name__ == "__main__":
    # Set up the main window
    root = tk.Tk()
    root.title("Caesar Cipher Encryption/Decryption")
    root.geometry("400x250")

    # Shift label and entry
    shift_label = tk.Label(root, text="Shift:")
    shift_label.pack(pady=10)
    shift_entry = tk.Entry(root)
    shift_entry.pack(pady=5)

    # Encryption button
    encrypt_button = tk.Button(root, text="Encrypt", command=perform_encryption)
    encrypt_button.pack(pady=10)

    # Decryption button
    decrypt_button = tk.Button(root, text="Decrypt", command=perform_decryption)
    decrypt_button.pack(pady=10)

    # Run the application
    root.mainloop()
