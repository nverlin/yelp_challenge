# To handle passing the data in from the json files


import json


def get_data_type(name_string, attribute_name):
    print("Attempting to load data- " + name_string + ".json")
    try:
        with open('yelp_data/yelp_academic_dataset_' + name_string + '.json', 'r', encoding='ascii', errors='ignore') as f:
            data = [json.loads(line)[attribute_name] for line in f]
        return data
    except json.JSONDecodeError as e:
        print(e)

def get_business_id(business_name):
    print("Getting Business ID")
    ids = get_data_type("business", "business_id")
    names = get_data_type("business", "name")
    for i in range(0, len(names)):
        if names[i] == business_name:

            return ids[i]
    return -1

def get_stars_for_business(business_id):
    print('Getting stars and dates for business')
    result_stars = []
    result_dates = []
    corresponding_business = get_data_type('review', 'business_id')
    all_stars = get_data_type('review', 'stars')
    all_dates = get_data_type('review', 'date')

    for i in range(0, len(corresponding_business)):
        if corresponding_business[i] == business_id:
            result_stars.append(all_stars[i])
            result_dates.append(all_dates[i])
    print(len(result_stars))
    print(len(result_dates))
    return result_stars, result_dates

