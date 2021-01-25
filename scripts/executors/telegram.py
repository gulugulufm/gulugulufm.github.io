#!/usr/bin/env python3
import requests
import yaml

import argparse
import os
import sys

SECRETS_DIR = f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/scripts/secrets"
RESOURCES_DIR = f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/scripts/snsgen-output"

parser = argparse.ArgumentParser()
parser.add_argument('--dryrun', help='dry run mode', action='store_true')
args = parser.parse_args()

# Just checking
executor_name = os.path.basename(__file__).split('.')[0]
config_file = os.path.join(RESOURCES_DIR, f'{executor_name}.yml')
if not os.path.isfile(config_file):
    print(f'Config file not found: file doesn\'t exist on {config_file}.')
    sys.exit(1)

with open(config_file, 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

if not os.path.isfile(data['message']):
    print(f"Message file not found: file doesn\'t exist on {data['message']}.")
    sys.exit(1)

with open(os.path.join(SECRETS_DIR, 'telegram_logincred.secret'), 'r') as cred:
    login_secrets = eval(cred.read())

with open(data['message'], 'r') as f:
    message = f.read()

# Now send the message
send_data = {
    'chat_id': login_secrets['chat_id'] if args.dryrun else '@gulugulufm',
    'text': message
}
url = f"https://api.telegram.org/bot{login_secrets['bot_token']}/sendMessage"
response = requests.post(url, json=send_data)

if 200 <= response.status_code < 300 and response.json()['ok']:
    print('Telegram post succeeded')
    print(response.json())
else:
    print('Failed to post status: ')
    print(response.json())
    sys.exit(1)
