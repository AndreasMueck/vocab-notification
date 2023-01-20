import time
import os
import sys
import json
from plyer import notification
from random import randint

def random_word():
    with open('wordlist.json') as fp:
        data = json.load(fp)
        words = data["wordlist"]
        random_index = randint(0, len(words)-1)
        return words[random_index]

while(True):
    rnd_word = random_word()
    spanish_word = rnd_word['spanish']
    german_word = rnd_word['german']
    line_break = "\n"
    notification_title = "Spanische Vokabeln"
    words = spanish_word+line_break+german_word

    time.sleep(20)
    notification.notify(
        title=notification_title,
        message=words,
        timeout=8,
        app_icon="spain_icon.ico"
    )








