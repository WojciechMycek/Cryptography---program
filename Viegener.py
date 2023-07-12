import csv
from itertools import cycle

class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword.upper()

    def _creating_key(self, text_visible):
        key = ""
        pairs = zip(text_visible, cycle(self.keyword))
        for pair in pairs:
            key += pair[1].upper()
        return key

    def encrypt(self, word):
        key = self._creating_key(word)
        encrypted = ""
        for place, letter in enumerate(word.upper()):
            x = 65 + ((ord(letter) + ord(key[place])) % 26)
            encrypted += chr(x)
        return encrypted

    def encrypt_csv(self, input_file_path, output_file_path):
        with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            for row in reader:
                encrypted_row = [self.encrypt(field) for field in row]
                writer.writerow(encrypted_row)

cipher = VigenereCipher("DAD")
cipher.encrypt_csv("date.csv", "encrypted_Viegener_date.csv")