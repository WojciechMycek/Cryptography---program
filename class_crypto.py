import cryptography
from cryptography.fernet import Fernet

class CSVFileHandler:
    def __init__(self, key_file_path):
        self.key_file_path = key_file_path
        self.key = self.load_key()

    def load_key(self):
        with open(self.key_file_path, 'rb') as key_file:
            return key_file.read()

    def save_key(self):
        with open(self.key_file_path, 'wb') as key_file:
            key_file.write(self.key)

    def encrypt_csv(self, input_file_path, output_file_path):
        f = Fernet(self.key)
        with open(input_file_path, 'rb') as original_file:
            original = original_file.read()
        encrypted = f.encrypt(original)
        with open(output_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt_csv(self, input_file_path, output_file_path):
        f = Fernet(self.key)
        with open(input_file_path, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        decrypted = f.decrypt(encrypted)
        with open(output_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)