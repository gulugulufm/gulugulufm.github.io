#!/usr/bin/env python3

import yaml
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import argparse
import os
import sys
import time
import uuid

# WARNING: this script is slow and error prone because douban doesn't provide a public API. Notably it requires
# a human to take over the captcha verification.

SECRETS_DIR = f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/scripts/secrets"
RESOURCES_DIR = f"/Users/{os.environ.get('USER')}/Documents/projects/gulugulufm.github.io/scripts/snsgen-output"

parser = argparse.ArgumentParser()
parser.add_argument('--dryrun', help='dry run mode', action='store_true')
args = parser.parse_args()

def sleep(secs):
    print(f'Sleeping for {str(secs)} seconds ...')
    time.sleep(secs)

# Just checking
executor_name = os.path.basename(__file__).split('.')[0]
config_file = os.path.join(RESOURCES_DIR, f'{executor_name}.yml')
if not os.path.isfile(config_file):
    print(f'Config file not found: file doesn\'t exist on {config_file}.')
    sys.exit(1)

with open(config_file, 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

if not os.path.isfile(data['photo']):
    print(f"Photo file not found: file doesn\'t exist on {data['photo']}.")
    sys.exit(1)

if not os.path.isfile(data['status']):
    print(f"Status file not found: file doesn\'t exist on {data['status']}.")
    sys.exit(1)

with open(os.path.join(SECRETS_DIR, 'douban_logincred.secret'), 'r') as cred:
    login_secrets = eval(cred.read())

# The login -- we'll need manual intervention for captcha
# Reference:
# https://www.jianshu.com/p/9b917cb39481
# https://www.jianshu.com/p/5ba3d4161b9b
# open up the page
print('Logging in ...')
driver = Chrome(executable_path='/usr/local/bin/chromedriver', options=ChromeOptions())
driver.get("https://www.douban.com/")
# switch to iframe
driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
# click use username and password
driver.find_element_by_xpath("/html/body/div[1]/div[1]/ul[1]/li[2]").click()
# find username and input value
driver.find_element_by_id("username").click()
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys(login_secrets['username'])
# find password and input value
driver.find_element_by_id("password").click()
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys(login_secrets['password'])
driver.find_element_by_link_text(u"登录豆瓣").click()
print('Douban may prompt for a captcha here, so make sure to check the browser window now.')
sleep(30) # time for manual captcha
driver.switch_to.default_content()

# Now send the message!
# enter text
print('Adding status text ...')
with open(data['status'], 'r') as f:
    status = f.read()
textarea = driver.find_element_by_id('isay-cont')
textarea.click()
sleep(1)
textarea.clear()
textarea.send_keys(status)

# add photo
print('Adding the photo ...')
photo_element = driver.find_element_by_class_name('ico-pic')
photo_element.click()
sleep(1)
picture_input = driver.find_element_by_id('isay-upload-inp')
picture_input.send_keys(data['photo'])
sleep(5)

# add topic/huati
print('Adding topic (huati) ...')
hash_element = driver.find_element_by_class_name('ico-topic')
hash_element.click()
sleep(1)
topic_input = driver.find_element_by_class_name('topic-text')
topic_input.clear()
topic_input.send_keys(data['topic'])
sleep(2)
suggestions = driver.find_elements_by_class_name('suggistion_item')
for suggestion in suggestions:
    print(f"Found suggested topic named {suggestion.find_element_by_class_name('title').text}")
    if data['topic'] in suggestion.find_element_by_class_name('title').text:
        try:
            suggestion.find_element_by_class_name('btn_add').click()
        except Exception as e:
            print('Unable to find the add button for this topic -- most likely due to a issue with douban\'s suggestor. We will stop here.')
            print(e)
            sys.exit(1)
        break

if args.dryrun:
    print('Dryrun -- we stop here right before posting the message.')
    sys.exit(0)

# click submit
print('Clicking submit ...')
driver.find_element_by_class_name('btn').find_element_by_class_name('bn-flat').click()
sleep(5)

# verification
print(f"Douban.py is done with execution, but you should verify manually at https://www.douban.com/people/49489567/statuses")
