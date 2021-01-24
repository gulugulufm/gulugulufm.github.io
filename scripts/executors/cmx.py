#!/usr/bin/env python3

from mastodon import Mastodon, MastodonError
import yaml

import os
import sys
import uuid

SECRETS_DIR = f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/scripts/secrets"
RESOURCES_DIR = f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/scripts/snsgen-output"

# Register your app! This only needs to be done once. Uncomment the code and substitute in your information.
'''
Mastodon.create_app(
     'mikihau_automated_tooter',
     api_base_url = 'https://m.cmx.im',
     to_file = os.path.join(SECRETS_DIR, 'mastodon_clientcred.secret')
)
'''

# Just checking
config_file = os.path.join(RESOURCES_DIR, 'cmx.yml')
if not os.path.isfile(config_file):
    print(f'Config file not found: file doesn\'t exist on {config_file}.')
    sys.exit(1)

with open(config_file, 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

if not os.path.isfile(data['video']):
    print(f"Video file no found: file doesn\'t exist on {data['video']}.")
    sys.exit(1)

if not os.path.isfile(data['status']):
    print(f"Status file no found: file doesn\'t exist on {data['status']}.")
    sys.exit(1)

# Then login. This can be done every time, or use persisted.
with open(os.path.join(SECRETS_DIR, 'mastodon_logincred.secret'), 'r') as cred:
     login_secrets = eval(cred.read())

mastodon = Mastodon(
    client_id = os.path.join(SECRETS_DIR, 'mastodon_clientcred.secret'),
    api_base_url = 'https://m.cmx.im'
)
mastodon.log_in(
    login_secrets['email'],
    login_secrets['password'],
    to_file = os.path.join(SECRETS_DIR, 'mastodon_usercred.secret')
)

# Upload the video file
try:
    media_response = mastodon.media_post(data['video'], mime_type='video/mp4')
except MastodonError as e:
    print('Failed to upload video: ' + repr(e))
    sys.exit(1)

print('Video upload succeeded. Response:')
print(media_response)
data['media_ids'] = [media_response]
data.pop('video')

# Now post the toot!
data['idempotency_key'] = str(uuid.uuid4()) # for now
with open(data['status'], 'r') as f:
    data['status'] = f.read()
print('Posting:')
print(data)

try:
    status_response = mastodon.status_post(**data)
except MastodonError as e:
    print('Failed to post status: ' + repr(e))
    sys.exit(1)

print(f"Toot post succeeded. Check it out at {status_response['url']}")