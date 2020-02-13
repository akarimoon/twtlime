from requests_oauthlib import OAuth1Session
from dotenv import load_dotenv; load_dotenv()
import json, os, time

# Access tokens
CK = os.getenv('CK')
CS = os.getenv('CS')
AT = os.getenv('AT')
AS = os.getenv('AS')

# URL
url = "https://api.twitter.com/1.1/statuses/home_timeline.json"

# GET using OAuth
twitter = OAuth1Session(CK, CS, AT, AS)

source = []
for j in range(100):
    params = {
        "count": 200,
        "include_entities": False,
        "include_rts": True,
        "trim_user": True,
        "exclude_replies": True
        }
    if j != 0:
        params["since_id"] = str(id1)
    req = twitter.get(url, params=params)
    if req.status_code == 200:
        timeline = json.loads(req.text)
        print(str(j))
        if j == 0:
            id1 = timeline[0]["id"]
        for i, tweet in enumerate(timeline):
            source.append(tweet["text"])
            if i == 200:
                id1 = tweet["id"] - 200
    else:
        print("Error: {}".format(req.status_code))

    time.sleep(60)
