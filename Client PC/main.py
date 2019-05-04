from barcodeProcessing.Food import Foodstuff
from sendEmail.SendMessage import send_to_email, get_the_message
from storage.StoreToDisk import save, load
from networkingBackend.NetworkDriver import NetworkDriver
import json
import signal

grocery_list = {}

def timeout_handler(signum, frame):
    global grocery_list
    print("Sending Email")
    send_to_email("monzohno@gmail.com", get_the_message(grocery_list))
    #print(grocery_list)
    save(grocery_list)
    exit()

def main():
    network = NetworkDriver('laptop')
    signal.signal(signal.SIGALRM, timeout_handler)
    me = True
    global grocery_list 
    grocery_list= load()
    # print(grocery_list)
    
    while(me):
        signal.alarm(10)
        next_barcode = network.receive()
        switch_state = network.receive()

        grocery_list.setdefault(next_barcode, Foodstuff(next_barcode, 0.0)) # should add the key if it is not found

        if switch_state == "add":
            grocery_list[next_barcode] = grocery_list[next_barcode] + Foodstuff(next_barcode)
        else:
            grocery_list[next_barcode] = grocery_list[next_barcode] - Foodstuff(next_barcode)
        
        network.send(grocery_list[next_barcode].get_name())

if __name__=="__main__":
    main()
