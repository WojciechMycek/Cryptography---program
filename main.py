from class_crypto import CSVFileHandlerFenter
from class_crypto import CSVFileHandlerMulti

print(" Hello. You can choose in my programm to define which method to encrypt and decrypt you can use: 1. Library Cryptography: Fernet (symmetric encryption)")

decision = int(input())

if decision == 1:
    # Initial object

    file_handler = CSVFileHandlerFenter('mykey.key')

    # Encrypting file
    file_handler.encrypt_csv('date.csv', 'enc_date.csv')

    # Decrypting file
    file_handler.decrypt_csv('enc_date.csv', 'dec_grades.csv')

elif decision == 2:
    print("Multi Encryption!!!")

    file_handler = CSVFileHandlerMulti('mykeys_multi.key', 2)
    file_handler.encrypt_csv('date.csv', 'enc_date_multi.csv')