import pigpio
from RPLCD.pigpio import CharLCD


#######################################
#               LCD
#Abstracts RPLCD lcd methods
#######################################
class LCDDisplay():
    
    def __init__(self):
        pi = pigpio.pi()
        self.lcd = CharLCD(pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23], cols=16, rows=2, charmap='A02', auto_linebreaks=True)
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