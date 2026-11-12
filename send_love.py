import os
import random
import urllib.request
import urllib.parse
import json

MESSAGES = [
    "Доброе утро, моя любимая! Желаю тебе прекрасного дня ❤️",
    "Просто напоминаю, что я безумно тебя люблю!",
    "Ты — лучшее, что случалось в моей жизни. Скучаю по тебе 😘"
]

token = os.environ["BOT_TOKEN"]
chat_id = os.environ["CHAT_ID"]
text = random.choice(MESSAGES)

url = f"https://telegram.org{token}/sendMessage"
data = urllib.parse.urlencode({"chat_id": chat_id, "text": text}).encode("utf-8")

req = urllib.request.Request(url, data=data)
with urllib.request.urlopen(req) as response:
    print(json.loads(response.read().decode("utf-8")))
