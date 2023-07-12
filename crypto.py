import cryptography
from cryptography.fernet import Fernet

#creating key
key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)

print(key)

#defined our excel to hide information

f = Fernet(key)

with open('date.csv', 'rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_date.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

#reading information from encrypted file
with open('enc_date.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_grades.csv', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)
