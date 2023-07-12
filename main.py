from class_crypto import CSVFileHandler

# Initial object

file_handler = CSVFileHandler('mykey.key')

# Encrypting file
file_handler.encrypt_csv('date.csv', 'enc_date.csv')

# Decrypting file
file_handler.decrypt_csv('enc_date.csv', 'dec_grades.csv')
