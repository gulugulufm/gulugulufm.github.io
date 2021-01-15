#!/usr/bin/env python3
from bs4 import BeautifulSoup
import sys
import os

print('Running audiogram_prep ...')

with open(sys.argv[1], 'r') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')

url = soup.find('meta', attrs={'property': 'og:url'})['content'][len('https://'):].rstrip('/')
serial = url.split('/')[-1]
title, description = soup.find('meta', attrs={'property': 'og:title'})['content'].split('：')

contents = {
    'podcast_name.txt': f'闭门造车 #{serial}',
    'episode_title.txt': f'{title}：',
    'episode_description.txt': description,
    'link.txt': f'>> {url}'
}

# output
for title, content in contents.items():
    with open(os.path.join(sys.argv[2], title), 'w') as f:
        f.write(content)
        f.write('\n')
        print(f'Wrote file: {os.path.join(sys.argv[2], title)}')
