import configparser
import os
import pysftp
from cryptography.fernet import Fernet
import warnings
warnings.filterwarnings("ignore")


config_file_name = config file name
# Parse the config parameters
print('Reading required configurations')
script_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_path)
print(script_path)
config = configparser.ConfigParser()
config.read(config_file_name)
    
os_path = config.get('OS_PATHS', 'os_path')
os.chdir(os_path)

unix_host = config.get('CREDS', 'host_name')
unix_user = config.get('CREDS', 'u_name')
unix_pass = config.get('CREDS', 'p_word')
unix_pass_key = config.get('CREDS', 'p_key')
unix_data_dir = config.get('CREDS', 'data_dir')
cipher_suite = Fernet(unix_pass_key.encode())
unix_pass_decode = cipher_suite.decrypt(unix_pass.encode('utf-8')).decode('utf-8')


def download_file(file_name_export):
    print('Downloading data from the server')
    try:
        cn_opts = pysftp.CnOpts()
        cn_opts.hostkeys = None
        srv = pysftp.Connection(host=unix_host, username=unix_user,
                                password=unix_pass_decode, cnopts=cn_opts)
        # Get the directory and file listing
        abc = srv.chdir(unix_data_dir)
        srv.get(unix_data_dir+'/'+file_name_export, os_path+'//'+file_name)
        srv.close()
        print('Downloading data from the server completed')
    except:
        print("Error while downloading the file from server")


files = ['file1.csv', 'fil2.csv']
for file in files:
    download_file(file)
