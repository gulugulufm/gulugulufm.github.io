#!/usr/bin/env python3

import tweepy
import yaml

import argparse
import os
import sys
import time
import uuid

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

if not os.path.isfile(data['video']):
    print(f"Video file no found: file doesn\'t exist on {data['video']}.")
    sys.exit(1)

if not os.path.isfile(data['status']):
    print(f"Status file no found: file doesn\'t exist on {data['status']}.")
    sys.exit(1)

# The auth.
with open(os.path.join(SECRETS_DIR, 'twitter_allcred.secret'), 'r') as cred:
    login_secrets = eval(cred.read())

auth = tweepy.OAuthHandler(login_secrets['api_key'], login_secrets['api_secret'])
auth.set_access_token(login_secrets['access_token'], login_secrets['access_token_secret']) 

# Upload the video file
api = tweepy.API(auth)
try:
    media_response = api.media_upload(data['video'], media_category='tweet_video')
except tweepy.TweepError as e:
    print('Failed to upload video: ' + repr(e))
    sys.exit(1)

print('Video upload succeeded. Response:')
print(media_response)
data['media_ids'] = [media_response.media_id]
data.pop('video')

# Now post the tweet!
wait_seconds = 15
print(f'Waiting {wait_seconds} seconds for the async processing of the uploaded media finishes ...')
time.sleep(15)
with open(data['status'], 'r') as f:
    data['status'] = f.read()
print('Posting:')
print(data)

if args.dryrun:
    print('Dryrun -- we stop here right before posting the toot.')
    sys.exit(0)
try:
    status_response = api.update_status(**data)
except tweepy.TweepError as e:
    print('Failed to post status: ' + repr(e))
    sys.exit(1)

print(f"Tweet post succeeded. Check it out at {status_response.entities}")
