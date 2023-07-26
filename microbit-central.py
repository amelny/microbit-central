# Imports go at the top
from microbit import *
import radio


radio.config(group=23)
# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.SMILE)
    sleep(400)
   
    while True:
        radio.config(group=23)
        radio.on()
        message = radio.receive()
        if message:
            display.scroll(str(message))
            display.show(Image.YES)
            radio.off()
            sleep(400)
        else:
            radio.off()
            display.show(Image.ASLEEP)
            sleep(400)
