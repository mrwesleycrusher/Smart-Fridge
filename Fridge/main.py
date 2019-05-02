from LCD.LCDFile import LCDDisplay
from LCD.scanInput import scannerInput, getAddState
from networkingBackend.NetworkDriver import NetworkDriver
import threading
import signal

buttonState=1

def pollButton():
    global buttonState = getAddState()

def timeout_handler(signum, frame):
    exit()

def main():
    network = NetworkDriver('pi')
    display = LCDDisplay()
    scanner = scannerInput()
    continue = True
    buttonpoller = threading.Thread(target=pollButton)
    buttonpoller.start()
    
    while(continue):
        signal.alacrm(600)
        network.send(scanner.scanForCode())
        if global buttonState is 1:
            network.send("add")
        else:
            network.send("something else")

        display.display(network.recieve())

if __name__=="__main__":
    main()
