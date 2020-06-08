import configparser
from cryptography.fernet import Fernet

config_file_name = name of config file

key = Fernet.generate_key()
print("Your Password Key has been generated")
cipher_suite = Fernet(key)
txt_to_encrypt = b'temp_password'  # Enter your password here between ''
cipher_text = cipher_suite.encrypt(txt_to_encrypt)
encrypted = cipher_text
plain_text = cipher_suite.decrypt(cipher_text)
print("Your Encrypted Password has been generated")

config = configparser.ConfigParser()
config.read(config_file_name)
# ['CREDS'] is a section created in config file
config['CREDS']['p_key'] = str(key.decode('UTF-8'))
config['CREDS']['p_word'] = encrypted.decode('UTF-8')

with open(config_file_name, 'w') as configfile:
    config.write(configfile)
