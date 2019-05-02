from barcodeProcessing.Food import Foodstuff
from sendEmail.SendMessage import send_to_email, get_the_message
from storage.StoreToDisk import save, load
from networkingBackend.NetworkDriver import NetworkDriver
import json
import signal

grocery_list = {}

def timeout_handler(signum, frame):
    global grocery_list
    send_to_email("Wow@wow.com", get_the_message(grocery_list))
    save(grocery_list)
    exit()

def main():
    network = NetworkDriver('laptop')
    me = True
    global grocery_list 
    grocery_list= load()
    
    while(me):
        signal.alarm(600)
        next_barcode = network.recieve()
        switch_state = network.recieve()

        if grocery_list[next_barcode] is not None:
                if switch_state == "add":
                    grocery_list[next_barcode] = grocery_list[next_barcode] + Foodstuff(next_barcode)
                else:
                    grocery_list[next_barcode] = Foodstuff(next_barcode)

        network.send(grocery_list[next_barcode].get_name())

if __name__=="__main__":
    main()
