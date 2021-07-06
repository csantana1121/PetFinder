import requests

# CONSANTS
ANIMAL_TYPES_LIST = [None, 'Dog','Cat','Rabbit','Small & Furry','Horse','Bird','Scales, Fins & Other','Barnyard']
ANIMAL_GENDERS_LIST = [None, 'Male','Female']
ANIMAL_AGE_LIST = [None, 'Young','Adult']

def get_token(API_key, API_secret):
    response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': API_key,
        'client_secret': API_secret,
    }) # Access token request

    return response.json()['access_token']

def get_request(access_token, BASE_url):
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
    response = requests.get(BASE_url, headers=headers)
    return response

def convert_to_json(response):
    return response.json()


def parse_animals(animals):
    return

# duo comment
# Function goes through list of search paramaters to get appropriate animal
def search_values(list_of_values):
    return    

def give_location():
    return


# Check to make sure user is inputing the correct values
def valid_input(user_response, valid_types_list):
    for valid_type in valid_types_list:
        if (user_response == valid_type):
            return True
    return False
    
def print_header(title):
    print(f'\n{title}')
    print('-' * len(title))


# Displays menu options based on list
def menu(menu_list):
    print_header('Menu')
    for index, name in enumerate(menu_list):
        print(f'({index}) {name}')
    

# Ensures integer input
def handle_option(option):
    try:
        return int(option)
    except:
        return -1
    

def build_url(dict_inputs):
    url = ""
    
    return
    
# Function will handle user input prompts and structure stuff
def user_input():
    dict_inputs = {}
    
    # Request animal_type
    menu(ANIMAL_TYPES_LIST)
    option = handle_option(input('Enter your option: '))   
    
    while(not valid_input(option, range(0, len(ANIMAL_TYPES_LIST)))):
        menu(ANIMAL_TYPES_LIST)
        option = handle_option(input('What kind of animal are you looking to adopt:'))
    
    menu(ANIMAL_GENDERS_LIST)
    option = handle_option(input('Enter your option: '))
    while(not valid_input(option, range(0,len(ANIMAL_GENDERS_LIST)))):
        menu(ANIMAL_GENDERS_LIST)
        option = handle_option(input('Gender preference: '))

    dict_inputs['animal_type'] = ANIMAL_TYPES_LIST[option]
    dict_inputs['animal_gender'] = ANIMAL_GENDERS_LIST[option]

    # Request gender
    # age
    # size

    # Location Function
    #location = give_location()
    #if (location != None):
    #    return
    #    add to search paramaters?

    location = input('Enter your postal code: ')
    distance = input('Search range(in miles): ')
    response = get_request(token, 'https://api.petfinder.com/v2/animals' +
                           '?location=' + location +
                           '&distance=' + distance +
                           '&type=' + dict_inputs['animal_type'] +
                          '&gender=' + dict_inputs['animal_gender'])
    return response


API_key = 'xeEk5W9rJpZV68xsBdvtqf8pkQIg9m2a1dei0JajyGxir8Nh4o'
API_secret = '3jw6ujpIJ2BJni6XQNCUpBxvjdSFxm88FvFbhfZ2'

API_key2 = 'zJfcD6R6ADhwPimvTWthqhnv9zbA3JcHZCZwEToEUY7fq8BnsM'
API_secret2 = 'RGkqeThwQVMg3eoVWJK3fuJkXVxX1TTVdLIyFeS3'

AUTH_URL = 'https://api.petfinder.com/v2/oauth2/token'
Get_Animals = 'https://api.petfinder.com/v2/animals'

token = get_token(API_key, API_secret)

#response = get_request(token, "https://api.petfinder.com/v2/types")
#print(convert_to_json(response))

output = user_input()

print(convert_to_json(output))
