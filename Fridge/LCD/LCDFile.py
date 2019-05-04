import pigpio
from RPLCD.pigpio import CharLCD
import time



#######################################
#               LCD
#Abstracts RPLCD lcd methods
#######################################
class LCDDisplay():
    
    def __init__(self):
        pi = pigpio.pi()
        self.lcd = CharLCD(pi,pin_rs=26, pin_contrast=8, pin_e=19, pins_data=[13,6,5,11], cols=16, rows=2, charmap='A02', auto_linebreaks=True)
        self.lcd.clear()
        self.lcd.home()
        print("Initialized LCD")
        self.lcd.write_string("Welcome!")
    
#######################################
#               display
#Displays passed string in LCD
#######################################
    def display(self, str):
        self.lcd.clear()
        self.lcd.write_string(str)
    def clear(self):
        self.lcd.clear()
    
    def display_buffer(self, framebuffer):
        self.lcd.home()
        for row in framebuffer:
            self.lcd.write_string(row.ljust(16)[:16])
            self.lcd.write_string('\n')
    


    def loop_string(self, string, framebuffer, row, delay=0.2):
        padding = ' ' * 16
        s = padding + string + padding
        for i in range(len(s) - 16 + 1):
            framebuffer[row] = s[i:i+16]
            self.display_buffer(framebuffer)
            time.sleep(delay)
#quick test code
# q = LCD()
# q.display("uwu")