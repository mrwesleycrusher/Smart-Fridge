from barcodeProcessing.Food import Foodstuff
from sendEmail.SendMessage import send_to_email, get_the_message
from storage.StoreToDisk import save, load
from networkingBackend.NetworkDriver import NetworkDriver
import json
import signal

grocery_list

def timeout_handler(signum, frame):
    send_to_email("Wow@wow.com", get_the_message(global grocery_list))
    save(global grocery_list)
    exit()

def main():
    network = NetworkDriver('laptop')
    continue = True
    global grocery_list = load()
    
    while(continue):
        signal.alarm(600)
        next_barcode = network.recieve()
        switch_state = network.recieve()

        if global grocery_list[next_barcode] is not None:
                if switch_state == "add":
                    global grocery_list[next_barcode] = global grocery_list[next_barcode] + Foodstuff(next_barcode)
                else:
                    global grocery_list[next_barcode] = Foodstuff(next_barcode)

        network.send(global grocery_list[next_barcode].get_name())

if __name__=="__main__":
    main()
