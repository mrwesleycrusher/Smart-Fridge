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
                return_list = {}
                s = json.loads(infile.read())
                
                if s:
                        # print(s)            
                        for x in s:
                                # print(x)
                                temp = Foodstuff(x['code'],int(x['quantity']))
                                return_list.update({x['code']:temp}) 
                                # print("LIST: ")
                                # print(return_list)
                        print("List Loaded")        
                        return return_list
                else:
                        return s

# def pickleSave(data):
#         with open('grocery_list_backup.json', 'wb') as outfile:
#                 pickle.dump(data, outfile)
