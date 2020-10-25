#!/usr/bin/env python3
from bs4 import BeautifulSoup

with open('/home/index.html', 'r') as f:
    content = f.read()
soup = BeautifulSoup(content, 'html.parser')

# h3 reformatting
for h3 in soup.article.div.find_all('h3'):
    # append newline before each h3
    inserted = soup.new_tag('p')
    #inserted.append(soup.new_tag('br'))
    h3.insert_before(inserted)
    # h3 to p
    new_tag = soup.new_tag('p')
    new_tag.string = f"--- {h3.text} ---"
    h3.replace_with(new_tag)

# filter out the tidbits
all_ps = soup.article.div.find_all('p')
remove = False
for index, p in enumerate(all_ps):
    if '🧨 花絮' in p.text:
        remove = True
    if remove:
        p.decompose()

# output
first_p = soup.article.div.find('p')
next_ps = soup.article.div.find_all('p')[1:]
wrapper_tag = soup.new_tag('div')
first_p.wrap(wrapper_tag)
for p in next_ps:
    wrapper_tag.append(p)

with open('/home/anchor.txt', 'w') as f:
    f.write(soup.article.h1.text)
    f.write('\n')
    f.write(wrapper_tag.prettify())

with open('/home/anchor.txt', 'r') as f:
    print(f.read())

