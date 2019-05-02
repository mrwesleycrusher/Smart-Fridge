from barcodeProcessing.Food import Foodstuff
from networkingBackend import NetworkDriver
import timeout_decorator
import SendMessage
import json

# Configure as you like
timeout_time = 60
email = 'max.jonas_knaver@colostate.edu'

def save(json_data):
    with open('grocery_list_backup.json', 'w') as outfile:
        json.dump(json_data, outfile)


@timeout_decorator.timeout(timeout_time) # if this function takes more than timeout_time seconds, we get an exception
def receive_data(list):
    receiver = NetworkDriver.receive('laptop')
    code = receiver.recieve() # This line will time out if scanning stops

    # Check for subtraction
    if code.endswith('*'):
        subtract = True
        code.replace('*', '')
    else:
        subtract = False

    item = Foodstuff(code)

    # Well this seems too janky to work
    if item in list:
        if subtract:
            list[item] -= item
        else:
            list[item] += item
    else:
        list.add(item)

def write_list(list):
    save(list)
    SendMessage.send_to_email(email, SendMessage.get_the_message(list))


def main():
    # grocery list - all the Foodstuffs we have. Small enough to store in main memory for most kitchens.

    # initialize to include previously stored items
    with open('grocery_list_backup.json', 'r') as file:
        groceries = json.load(file)

    # loop until we kill this program
    while True:
        try:
            receive_data(groceries)
        except TimeoutError:
            write_list(groceries)

if __name__ == '__main__':
    main()
