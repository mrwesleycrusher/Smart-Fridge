from LCD.LCDFile import LCDDisplay
from LCD.scanInput import scannerInput, getAddState
from networkingBackend.NetworkDriver import NetworkDriver
import threading
import signal
from RPi import GPIO

buttonState=1

def pollButton():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    buttonState = GPIO.input(18)

def timeout_handler(signum, frame):
    exit()

def main():
    network = NetworkDriver('pi')
    display = LCDDisplay()
    scanner = scannerInput()
    me = True
    buttonpoller = threading.Thread(target=pollButton)
    buttonpoller.start()
    
    while(me):
        signal.alacrm(600)
        network.send(scanner.scanForCode())
        if global buttonState == 1:
            network.send("add")
        else:
            network.send("something else")

        display.display(network.recieve())

if __name__=="__main__":
    main()
