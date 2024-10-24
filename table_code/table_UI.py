from table_logic import create_encryption_table, encrypt, decrypt
from table_utilits import load_text, save_text, compare_texts, input_text_to_file

if __name__ == "__main__":
    while True:
        try:
            print("TO CLOSE PRESS 1, TO CONTINUE PRESS ANYTHING ELSE")
            user_choice = input().strip()
            if user_choice == "1":
                break

            # Input text from user and save to file
            input_text_to_file('input.txt')

            print("ENTER YOUR KEY (alphanumeric):")
            key = input().strip()  # Now supports alphanumeric keys

            # Generate the encryption table based on the key
            table = create_encryption_table(key)

            # Load the original text from file
            original_text = load_text('input.txt')

            # Encrypt and decrypt the text
            encrypted_text = encrypt(original_text, table)
            decrypted_text = decrypt(encrypted_text, table)

            # Output results
            print("Original text:", repr(original_text))
            print("Encrypted text:", repr(encrypted_text))
            print("Decrypted text:", repr(decrypted_text))

            # Verify if encryption is reversible
            if compare_texts(original_text, decrypted_text):
                print("Encryption and decryption are reversible.")
            else:
                print("Error: Decryption does not match the original text.")

            # Save encrypted and decrypted texts to files
            save_text('encrypted.txt', encrypted_text)
            save_text('decrypted.txt', decrypted_text)

        except Exception as e:
            print(f"An error occurred: {e}")
