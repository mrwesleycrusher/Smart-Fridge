import json
import pickle

def save(json_data):
    with open('grocery_list_backup.json', 'w') as outfile:
        json.dump([value.__dict__ for key,value in json_data.items()], outfile)

def load():
    with open('grocery_list_backup.json', 'r') as infile:
        return json.loads(infile.read())

# def pickleSave(data):
#         with open('grocery_list_backup.json', 'wb') as outfile:
#                 pickle.dump(data, outfile)
