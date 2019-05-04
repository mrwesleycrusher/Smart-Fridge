import json
import pickle
from barcodeProcessing.Food import Foodstuff

def save(json_data):
    with open('grocery_list_backup.json', 'w') as outfile:
        #print("Hecky you: " + [(value.__dict__ for key,value in json_data.items())])
        json.dump(([value.__dict__ for key,value in json_data.items()]), outfile)
        # json.dump(json_data, outfile)

def load():
        with open('grocery_list_backup.json', 'r') as infile:
                s = json.loads(infile.read())
                
                # if s:            
                #         print(s[0])
                #         temp = Foodstuff(s[0]['code'],int(s[0]['quantity']))
                #         return_list = {s[0]['code']:temp} 
                #         print(return_list)
                #         return return_list
                # else:
                #         return s
                return s

# def pickleSave(data):
#         with open('grocery_list_backup.json', 'wb') as outfile:
#                 pickle.dump(data, outfile)
