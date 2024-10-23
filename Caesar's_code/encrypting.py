def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Сhecking if a character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # we keep non-alphabetic characters unchanged
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # decryption is negative-shift encryption


# Downloading the text from the file
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Writing the text to a file
def save_text(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


# The main logic of the program
if __name__ == "__main__":
    shift = 8  # зсув
    input_file = 'test_case_encrypting.txt'
    encrypted_file = 'encrypted_text.txt'
    decrypted_file = 'decrypted_text.txt'

    original_text = load_text(input_file)
    encrypted_text = caesar_encrypt(original_text, shift)

    save_text(encrypted_file, encrypted_text)
    decrypted_text = caesar_decrypt(encrypted_text, shift)

    save_text(decrypted_file, decrypted_text)

    # Reversibility check
    assert original_text == decrypted_text, "The decrypted message does not match the original."
    print("Encryption and decryption completed successfully!")
