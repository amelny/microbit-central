# Imports go at the top
from microbit import *
import radio

uart.init()
radio.config(group=23)
radio.on()
# Code in a 'while True:' loop repeats forever
while True:
    display.show(Image.SMILE)
    sleep(400)
   
    while True:
        
        message = radio.receive()
        
        if message:
            uart.write(str(message))
            uart.write("\r\n")
            display.scroll(str(message))
            
            sleep(100)
        else:
            if button_a.was_pressed():
                uart.write(str(message))
                uart.write("\r\n")
                display.scroll(str(message))
            
            display.show(Image.ASLEEP)
            
