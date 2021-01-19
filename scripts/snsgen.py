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

episode = sys.argv[1]
url = soup.find('meta', attrs={'property': 'og:url'})['content'].rstrip('/')
intro = soup.find('meta', attrs={'name': 'description'})['content']
tags = soup.find('meta', attrs={'name': 'keywords'})['content'].split(',')
episode_data = {
    'episode': episode,
    'intro': intro,
    'episode_url': url,
    'tags': tags,
    'video': os.path.join(VIDEO_DIR, f"{episode if len(episode) > 1 else '0' + episode}-trailer.mp4")
}

# write 2 files for each service: *.template for the text, *.yml for all metadata/fields
services = {
    'cmx': {
        'status': os.path.join(OUTPUT_DIR, 'cmx.txt'),
        'video': episode_data['video']
    },
    #'douban': {},
    #'jike': {},
    #'substack': {},
    #'telegram': {},
    #'twitter': {},
}

for service in services:
    template = Template(filename=os.path.join(RESOURCES_DIR, f'{service}.template'))
    with open(os.path.join(OUTPUT_DIR, f'{service}.txt'), 'w') as outfile:
        outfile.write(template.render(**episode_data))
    with open(os.path.join(OUTPUT_DIR, f'{service}.yml'), 'w') as outfile:
        yaml.dump(services[service], outfile)
