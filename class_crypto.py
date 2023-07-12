import csv
import cryptography
from cryptography.fernet import Fernet
from cryptography.fernet import MultiFernet

class CSVFileHandlerFenter:
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

class MultiFernetHandler:
    def __init__(self, keys):
        self.fernets = [Fernet(key) for key in keys]

    def encrypt(self, message):
        encrypted_message = message
        for fernet in self.fernets:
            encrypted_message = fernet.encrypt(encrypted_message)
        return encrypted_message

    def decrypt(self, token):
        decrypted_token = token
        for fernet in reversed(self.fernets):
            decrypted_token = fernet.decrypt(decrypted_token)
        return decrypted_token

    def rotate(self, token):
        rotated_token = token
        for fernet in self.fernets:
            rotated_token = fernet.encrypt(rotated_token)
        return rotated_token

    @staticmethod
    def generate_keys(num_keys):
        keys = []
        for _ in range(num_keys):
            keys.append(Fernet.generate_key())
        return keys


class CSVFileHandlerMulti:
    def __init__(self, key_file_path, num_keys):
        self.key_file_path = key_file_path
        self.keys = MultiFernetHandler.generate_keys(num_keys)
        self.handler = MultiFernetHandler(self.keys)

    def load_keys(self):
        with open(self.key_file_path, 'wb') as key_file:
            for key in self.keys:
                key_file.write(key + b'\n')

    def encrypt_csv(self, input_file_path, output_file_path):
        self.load_keys()
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            for row in reader:
                encrypted_row = [self.handler.encrypt(field.encode()) for field in row]
                writer.writerow(encrypted_row)

    def decrypt_csv(self, input_file_path, output_file_path):
        self.load_keys()
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            for row in reader:
                decrypted_row = [self.handler.decrypt(field.encode()).decode() for field in row]
                writer.writerow(decrypted_row)