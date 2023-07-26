# Imports go at the top
from microbit import *
import radio


radio.config(group=23)
# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.SMILE)
    sleep(400)
    radio.on()
    while True:
        message = radio.receive()
        if message:
            display.scroll(message)
            display.show(Image.YES)
            sleep(400)
