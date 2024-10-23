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