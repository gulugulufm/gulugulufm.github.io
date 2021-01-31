#!/usr/bin/env python3
from bs4 import BeautifulSoup
import yaml
from mako.template import Template

import os
import sys

# usage: python snsgen.py [episode]
# e.g. python snsgen.py 9

OUTPUT_DIR = f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/scripts/snsgen-output"
RESOURCES_DIR = f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/scripts/resources"
SITE_DIR = f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/site"
VIDEO_DIR= f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/scripts/audiogram-output"

# make and/or clean up OUTPUT_DIR
try:
    os.mkdir(OUTPUT_DIR)
except FileExistsError as e:
    pass
for filename in os.listdir(OUTPUT_DIR):
    os.remove(os.path.join(OUTPUT_DIR, filename))

# gather data
with open(f'{SITE_DIR}/public/podcasts/{sys.argv[1]}/index.html', 'r') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')

def get_intro_shortened(intro, tags):
    # magic numbers
    tweet_limit = 280
    title_paragraph = 14
    link_paragraph = 5 * 2 + 23
    tag_paragraph = (len(''.join(tags)) + 4) * 2 + (len(tags) + 2) + (len(tags) + 2 - 1) # text, pound characters, and whitespaces
    whitespaces = 3 * 2 # double newlines to break paragraphs
    buffer = 0
    # length for the intro should not exceed this ...
    shorted_intro_length = (tweet_limit - title_paragraph - link_paragraph - tag_paragraph - whitespaces - buffer) // 2
    if len(intro) <= shorted_intro_length:
        shortened = intro
    else:
        shortened = intro[:shorted_intro_length-3] + '...'
    return shortened

episode = sys.argv[1]
url = soup.find('meta', attrs={'property': 'og:url'})['content'].rstrip('/')
intro = soup.find('meta', attrs={'name': 'description'})['content']
tags = soup.find('meta', attrs={'name': 'keywords'})['content'].split(',')
guest = soup.find('meta', attrs={'property': 'og:title'})['content'].split('：')[0]
episode_data = {
    'episode': episode,
    'guest': guest,
    'intro': intro,
    'intro_shortened': get_intro_shortened(intro, tags), # just for twitter
    'episode_url': url,
    'tags': tags,
    'kansou': '', # TODO
    'video': os.path.join(VIDEO_DIR, f"{episode if len(episode) > 1 else '0' + episode}-trailer.mp4"),
    'photo': os.path.join(VIDEO_DIR, f"{episode if len(episode) > 1 else '0' + episode}-trailer.mp4-3.jpg")
}

# write 2 files for each service: *.template for the text, *.yml for all metadata/fields
services = {
    'cmx': {
        'status': os.path.join(OUTPUT_DIR, 'cmx.txt'),
        'video': episode_data['video']
    },
    'douban': {
        'status': os.path.join(OUTPUT_DIR, 'douban.txt'),
        'photo': episode_data['photo'],
        'topic': '聊聊那些有趣的播客'
    },
    #'jike': {},
    #'substack': {},
    'telegram': {
        'message': os.path.join(OUTPUT_DIR, 'telegram.txt')
    },
    'twitter': {
        'status': os.path.join(OUTPUT_DIR, 'twitter.txt'),
        'video': episode_data['video']
    },
}

for service in services:
    template = Template(filename=os.path.join(RESOURCES_DIR, f'{service}.template'))
    with open(os.path.join(OUTPUT_DIR, f'{service}.txt'), 'w') as outfile:
        outfile.write(template.render(**episode_data))
    with open(os.path.join(OUTPUT_DIR, f'{service}.yml'), 'w') as outfile:
        yaml.dump(services[service], outfile, allow_unicode=True)
