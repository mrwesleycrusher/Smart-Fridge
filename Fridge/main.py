from LCD.LCDFile import LCDDisplay
from LCD.scanInput import scannerInput, getAddState
from networkingBackend.NetworkDriver import NetworkDriver
import threading
import signal
import pigpio
import time

buttonState = 1

def initButton(pi):
    pi = pigpio.pi()
    global buttonState
    pi.set_mode(16, pigpio.INPUT)
    pi.set_noise_filter(16, 10000, 500000)
    pi.set_pull_up_down(16, pigpio.PUD_UP)

def pollButton(pi):
    global buttonState
   
    while(True):
        # print("readingbutton")
        # print(pi.read(6))
        buttonState = pi.read(16)
        # print(buttonState)
        time.sleep(.3)
        
    return buttonState

def timeout_handler(signum, frame):
    exit()

def main():
    display = LCDDisplay()
    scanner = scannerInput()
    pi = pigpio.pi()
    initButton(pi)
    network = NetworkDriver('pi')
    me = True
    global buttonState
    buttonpoller = threading.Thread(target=pollButton,args = (pi,))
    buttonpoller.start()
    
    framebuffer = ['Item Scanned','']
    
    while(me):
        #signal.alarm(600)
        bcode = scanner.scanForCode()
        #print("Bcode: " + bcode + str(type(bcode)))
        network.send(bcode)
        # print(buttonState)
        if buttonState == 1:
            # print("add")
            network.send("add")
        else:
            # print("subtract")
            network.send("subtract")
        thing = network.receive()
        # print("thing: " + thing)
        display.clear()
        display.display_buffer(framebuffer)
        display.loop_string(thing, framebuffer, 1)
        display.display("Waiting for Item")


if __name__=="__main__":
    main()
