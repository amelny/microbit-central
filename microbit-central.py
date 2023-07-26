# Imports go at the top
from microbit import *
import radio

radio.config(group=23)
radio.on()
# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.SMILE)
    sleep(400)
   
    while True:
        
        message = radio.receive()
        if message:
            display.scroll(str(message))
            display.show(Image.YES)
            
            sleep(400)
        else:
            
            display.show(Image.ASLEEP)
            sleep(400)
