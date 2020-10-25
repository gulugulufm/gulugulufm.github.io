#!/usr/bin/env python3
from bs4 import BeautifulSoup, NavigableString

def process_meat(f):
    first_h3 = True
    for tag in section.contents:
        if isinstance(tag, NavigableString):
            continue
        if '🧨 花絮' in tag.text:
            break
        if tag.name == 'h3':
            if first_h3:
                f.write(f'--- {tag.text[1:].strip()} ---\n') # glob [1:] to purge emoji
                first_h3 = False
            else:
                f.write(f'\n--- {tag.text[1:].strip()} ---\n')
        else:
            f.write(f'{tag.text}\n')

def process_everything_else(f):
    for tag in section.contents:
        if isinstance(tag, NavigableString):
            continue
        if tag.name == 'p': # ignoring everything else except for p's
            f.write(f'\n{tag.text}\n')

with open('/home/index.html', 'r') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')

with open('/home/ximalaya.txt', 'w') as f:
    sections = soup.article.div.find_all('section')
    for i, section in enumerate(sections):
        if i == 1: # the 2nd section is the meat of the article
            process_meat(f)
        else:
            process_everything_else(f)

with open('/home/ximalaya.txt', 'r') as f:
    print(f.read())
