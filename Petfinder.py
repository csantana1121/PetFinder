import requests

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

# Function will handle user input prompts and structure stuff
def user_input():
    
    # Request animal_type
    animal_type = ''
    while (animal_type != 'Exit'):
        animal_type = input('What kind of animal are you looking to adopt:')
    
    # gender
    # age
    # size

    # Location Function
    location = give_location()
    if (location != None):
        #add to search paramaters?

    location = input('Enter your postal code: ')
    distance = input('Search range(in miles): ')
    response = get_request(token, 'https://api.petfinder.com/v2/animals' + '?location=' + location + '&distance=' + distance + '&type=' + animal_type)

    


API_key = 'xeEk5W9rJpZV68xsBdvtqf8pkQIg9m2a1dei0JajyGxir8Nh4o'
API_secret = '3jw6ujpIJ2BJni6XQNCUpBxvjdSFxm88FvFbhfZ2'

API_key2 = 'zJfcD6R6ADhwPimvTWthqhnv9zbA3JcHZCZwEToEUY7fq8BnsM'
API_secret2 = 'RGkqeThwQVMg3eoVWJK3fuJkXVxX1TTVdLIyFeS3'

AUTH_URL = 'https://api.petfinder.com/v2/oauth2/token'

Get_Animals = 'https://api.petfinder.com/v2/animals'
response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': API_key,
    'client_secret': API_secret,
}) # Access token request
token = response.json()['access_token']


output = user_input()

print(convert_to_json(response))
