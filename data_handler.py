# To handle passing the data in from the json files

import json

def get_data_type(name_string):
    try:
        with open('yelp_data/yelp_academic_dataset_' + name_string + '.json', 'r', encoding='ascii', errors='ignore') as f:
            data = [json.loads(line) for line in f]
        print(data)

    except json.JSONDecodeError as e:
        print(e)



data = get_data_type("business")

