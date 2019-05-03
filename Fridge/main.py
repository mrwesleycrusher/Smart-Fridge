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
    pi.set_mode(5, pigpio.INPUT)
    pi.set_noise_filter(5, 10000, 500000)
    pi.set_pull_up_down(5, pigpio.PUD_UP)
    buttonState = pi.read(5)

def timeout_handler(signum, frame):
    exit()

def main():
    display = LCDDisplay()
    scanner = scannerInput()
    network = NetworkDriver('pi')
    me = True
    buttonpoller = threading.Thread(target=pollButton)
    buttonpoller.start()
    global buttonState
    
    while(me):
        signal.alarm(600)
        bcode = scanner.scanForCode()
        #print("Bcode: " + bcode + str(type(bcode)))
        network.send(bcode)
        
        if buttonState == 1:
            network.send("add")
        else:
            network.send("something else")

        display.display(network.recieve())

if __name__=="__main__":
    main()
