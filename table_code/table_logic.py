import random
import string
import hashlib


def create_encryption_table(key):
    """Creates a random encryption table based on a hash of the provided key (supports both characters and numbers)."""
    letters = list(string.ascii_uppercase)  # List of uppercase letters A-Z

    # Hash the key to generate a consistent random seed
    key_hash = hashlib.sha256(key.encode('utf-8')).hexdigest()
    seed = int(key_hash, 16) % (2 ** 32)  # Convert hash to a number usable as a seed

    random.seed(seed)  # Set random seed based on hashed key
    random.shuffle(letters)  # Shuffle letters to create a random mapping

    return letters


def encrypt(text, table):
    """Encrypts the given text using the provided encryption table."""
    mapping = {string.ascii_uppercase[i]: table[i] for i in range(len(table))}  # Create a mapping from original to encrypted letters
    encrypted = ""
    for char in text:
        if char.upper() in mapping:
            if char.isupper():
                encrypted += mapping[char.upper()]  # Encrypt uppercase letters
            else:
                encrypted += mapping[char.upper()].lower()  # Encrypt lowercase letters
        else:
            encrypted += char  # Leave non-alphabetic characters unchanged
    return encrypted
def decrypt(encrypted_text, table):
    """Decrypts the given text using the provided encryption table."""
    reverse_mapping = {table[i]: string.ascii_uppercase[i] for i in range(len(table))}  # Reverse mapping
    reverse_mapping.update({table[i].lower(): string.ascii_lowercase[i] for i in range(len(table))})  # For lowercase
    decrypted = ""
    for char in encrypted_text:
        if char in reverse_mapping:
            decrypted += reverse_mapping[char]  # Decrypt character while maintaining case
        else:
            decrypted += char  # Leave non-alphabetic characters unchanged
    return decrypted
