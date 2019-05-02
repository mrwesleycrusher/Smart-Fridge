import pigpio
from RPLCD.pigpio import CharLCD


#######################################
#               LCD
#Abstracts RPLCD lcd methods
#######################################
class LCDDisplay():
    
    def __init__(self):
        pi = pigpio.pi()
        self.lcd = CharLCD(pi,pin_rs=25, pin_e=24, pins_data=[23, 22, 21, 14], cols=16, rows=2, charmap='A02', auto_linebreaks=True)
        self.lcd.write_string("Welcome!")
    
#######################################
#               display
#Displays passed string in LCD
#######################################
    def display(self, str):
        self.lcd.clear()
        self.lcd.write_string(str)

#quick test code
# q = LCD()
# q.display("uwu")