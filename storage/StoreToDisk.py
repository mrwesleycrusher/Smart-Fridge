import json
def save(json_data):
    with open('grocery_list_backup.json', 'w') as outfile:
        json.dump(json_data, outfile)
