from barcodeProcessing.Food import Foodstuff
from sendEmail.SendMessage import send_to_email, get_the_message
from storage.StoreToDisk import save, load
from networkingBackend.NetworkDriver import NetworkDriver
import json
import signal
import timeout_decorator

grocery_list = {}


def timeout_handler():
    global grocery_list
    print("Sending Email")
    send_to_email("monzohno@gmail.com", get_the_message(grocery_list))
    # print(grocery_list)
    save(grocery_list)




@timeout_decorator.timeout(30, timeout_exception=TimeoutError)
def receive_data(network):
    global grocery_list
    next_barcode = network.receive()
    switch_state = network.receive()

    food_temp = Foodstuff(next_barcode, 0.0)
    if(food_temp.get_name != "NoSuchCode"):
        grocery_list.setdefault(next_barcode, food_temp)  # should add the key if it is not found

        if switch_state == "add":
            grocery_list[next_barcode] = grocery_list[next_barcode] + Foodstuff(next_barcode)
        else:
            grocery_list[next_barcode] = grocery_list[next_barcode] - Foodstuff(next_barcode)

        network.send(grocery_list[next_barcode].get_name())
    else:
        network.send("Scan Failed")

def main():
    network = NetworkDriver('laptop')
    global grocery_list
    grocery_list = load()
    # print(grocery_list)

    while (True):
        try:
            receive_data(network)
        except TimeoutError:
            timeout_handler()


if __name__ == "__main__":
    main()
