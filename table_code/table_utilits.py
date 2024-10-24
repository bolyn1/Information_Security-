# utilities.py
import random
# Load text from a file
def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
# Save text to a file
def save_text(file_path, text):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)
# Compare original and decrypted text
def compare_texts(original_text, decrypted_text):
    return original_text == decrypted_text
# Get user input and save it to the file (up to 25 characters)
def input_text_to_file(file_path):
    """Prompts the user to enter text (up to 25 characters) and saves it to a file."""
    while True:
        text = input("Please enter text (up to 25 characters): ")
        if len(text) <= 25:
            break
        print("Text is too long. Please enter up to 25 characters.")

    save_text(file_path, text)
    print(f"Text saved to {file_path}")
