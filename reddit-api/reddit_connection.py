import configparser
import os
import requests

config = configparser.ConfigParser()
config.read_file(open(f'{os.path.dirname(os.path.abspath(__file__))}/config.cfg'))

# All authentication info
personal_use_script = config.get('REDDIT', 'PERSONAL_USE_SCRIPT')
secret = config.get('REDDIT', 'SECRET')
username = config.get('REDDIT', 'USERNAME')
password = config.get('REDDIT', 'PASSWORD')
name = config.get('REDDIT', 'NAME')

auth = requests.auth.HTTPBasicAuth(personal_use_script, secret)

data = {'grant_type': 'password',
        'username': username,
        'password': password}

headers = {'User-Agent': name}


# POST request for OAuth token
# Returns access_token, token_type: bearer, expiry (1 day)
res = requests.post('https://www.reddit.com/api/v1/access_token',
                     auth=auth, data=data, headers=headers)
  
TOKEN = res.json()['access_token']

headers['Authorization'] = f'bearer {TOKEN}'

print(headers)
# Test of futurology subreddit
params = {'limit': 10}

res = requests.get(f"https://oauth.reddit.com/r/futurology/top",
                    headers=headers, params=params)

print(res)
