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
            display.scroll(message)
            
            
            sleep(100)
        else:
            
            display.show(Image.ASLEEP)
           
            
            
