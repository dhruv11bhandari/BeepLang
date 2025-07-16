import time
from playsound import playsound

def play_morse(morse):
    for symbol in morse:
        if symbol == '.':
            playsound("dot.mp3")
        elif symbol == '-':
            playsound("dash.mp3")
        elif symbol == ' ':
            time.sleep(0.5)
        elif symbol == '/':
            time.sleep(1)