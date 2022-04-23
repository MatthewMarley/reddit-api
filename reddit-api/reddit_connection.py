import requests
import configparser
import os

config = configparser.ConfigParser()
config.read_file(open(f'{os.path.dirname(os.path.abspath(__file__))}/config.cfg'))

personal_use_script = config.get('REDDIT', 'PERSONAL_USE_SCRIPT')
secret = config.get('REDDIT', 'SECRET')

auth = requests.auth.HTTPBasicAuth(personal_use_script, secret)
