from syncronous_speech_server.speak import speak_synchronous
import srt
from datetime import datetime
from bs4 import BeautifulSoup
import os


def clean_text(tagged_text):
    '''Strip tags from text.'''
    cleantext = BeautifulSoup(tagged_text, "lxml").text
    return cleantext
    

def clear():
    os.system('clear')



with open('subs.srt', 'r') as subs_file:
    text = subs_file.read()
    subs_generator = srt.parse(text)
    subs = list(subs_generator)


start = datetime.now()


already_read = []

while True:
    now = datetime.now()
    elapsed = now - start

    clear()
    print(elapsed)
    


    for sub in subs:

        if sub.index not in already_read and elapsed >= sub.start:
            speak_synchronous(clean_text(sub.content))
            already_read.append(sub.index)











# speak_synchronous('text for you')
# speak_synchronous('text for me')
                                                       
