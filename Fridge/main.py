from LCD.LCDFile import LCDDisplay
from LCD.scanInput import scannerInput, getAddState
from networkingBackend.NetworkDriver import NetworkDriver
import threading
import signal
import pigpio

buttonState=1

def pollButton():
    pi = pigpio.pi()
    global buttonState
    pi.set_mode(18, pigpio.INPUT)
    pi.set_noise_filter(18, 10000, 500000)
    pi.set_pull_up_down(18, pigpio.PUD_UP)
    buttonState = pi.read(18)

def timeout_handler(signum, frame):
    exit()

def main():
    network = NetworkDriver('pi')
    display = LCDDisplay()
    scanner = scannerInput()
    me = True
    buttonpoller = threading.Thread(target=pollButton)
    buttonpoller.start()
    global buttonState
    
    while(me):
        signal.alacrm(600)
        network.send(scanner.scanForCode())
        
        if buttonState == 1:
            network.send("add")
        else:
            network.send("something else")

        display.display(network.recieve())

if __name__=="__main__":
    main()
