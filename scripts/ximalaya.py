#!/usr/bin/env python3
from bs4 import BeautifulSoup, NavigableString
import sys

def process_meat():
    first_h3 = True
    for tag in section.contents:
        if isinstance(tag, NavigableString):
            continue
        if '🧨 花絮' in tag.text:
            break
        if tag.name == 'h3':
            if first_h3:
                print(f'--- {tag.text[1:].strip()} ---') # glob [1:] to purge emoji
                first_h3 = False
            else:
                print(f'\n--- {tag.text[1:].strip()} ---')
        else:
            print(f'{tag.text}')

def process_everything_else():
    for tag in section.contents:
        if isinstance(tag, NavigableString):
            continue
        if tag.name == 'p': # ignoring everything else except for p's
            print(f'\n{tag.text}')

with open(sys.argv[1], 'r') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')

sections = soup.article.div.find_all('section')
for i, section in enumerate(sections):
    if i == 1: # the 2nd section is the meat of the article
        process_meat()
    else:
        process_everything_else()
