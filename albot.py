import requests
from fake_useragent import UserAgent
import re
import sys

ua = UserAgent()
headers = {"User-Agent": ua.random}

def like_video(video_code):
    page = requests.get(VIDEO_BASE_URL + video_code, headers=headers).text

    try:
        like_url = APARAT_URL + re.search(r"\/video\/like\/add\/.*\/hash\/.{40}", page)[0]
    except TypeError:        
        return

    res = requests.get(like_url, headers=headers)
    if res.ok:
        print(f"({video_code}) liked!")

try: 
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            videos = f.read().split('\n')
    else:
        print("python3 albot.py <filepath>")
        exit()
except Exception as e:
    print(e)
    exit()

APARAT_URL = "https://www.aparat.com"
VIDEO_BASE_URL = f"{APARAT_URL}/v/"

for video in videos:
    like_video(video)
