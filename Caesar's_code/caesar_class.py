from utilits.caesar_utilits import load_text, save_text

class CaesarEncryptDecrypt:
    """"Initialization"""
    def __init__(self, shift, input_file_path, output_file_path):
        self.shift = shift % 26
        self.input_file_path = input_file_path
        self.output_file_path = output_file_path

    def __caesar_encrypt(self, text, shift):
        """Private method for Caesar encryption and decryption"""
        result_text = ""
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
                result_text += encrypted_char
            else:
                result_text += char
        return result_text

    def encrypt_file(self):
        """Public method to encrypt and save to output file"""
        original_text = load_text(self.input_file_path)
        encrypted_text = self.__caesar_encrypt(original_text, self.shift)
        save_text(self.output_file_path, encrypted_text)

    def decrypt_file(self):
        """Public method to decrypt and save to output file"""
        encrypted_text = load_text(self.input_file_path)
        decrypted_text = self.__caesar_encrypt(encrypted_text, -self.shift)
        save_text(self.output_file_path, decrypted_text)
