import requests
import pandas as pd
import plotly.express as px
from IPython.core.display import HTML
# Location check using google api
# error checks
# handle if returns empty animals


# CONSANTS
ANIMAL_TYPES_LIST = [None, 'Dog', 'Cat', 'Rabbit', 'Small-Furry', 'Horse',
                     'Bird', 'Scales-Fins-Other', 'Barnyard']
ANIMAL_GENDERS_LIST = [None, 'Male', 'Female']
ANIMAL_AGE_LIST = [None, 'Baby', 'Young', 'Adult', 'Senior']
ANIMAL_SIZE_LIST = [None, 'Small', 'Medium', 'Large', 'Xlarge']
LOCATION_OPTIONS = ['No', 'Yes']
API_key = 'xeEk5W9rJpZV68xsBdvtqf8pkQIg9m2a1dei0JajyGxir8Nh4o'
API_secret = '3jw6ujpIJ2BJni6XQNCUpBxvjdSFxm88FvFbhfZ2'


def get_token(API_key, API_secret):
    response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': API_key,
        'client_secret': API_secret,
    })  # Access token request

    return response.json()['access_token']


def path_to_image_html(path):
    return '<img src="' + path + '" width="60" >'


def get_request(access_token, BASE_url):
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
    response = requests.get(BASE_url, headers=headers)
    return response


def convert_to_json(response):
    return response.json()


# Parses through the animals json to get desired information
# Return dataframe
def parse_animals(animals_json):
    animalsdf = pd.DataFrame()
    animals_dict = {}
    count = 0

    # check if it returns an empty values
    for animal in animals_json["animals"]:
        
        # Add most general information
        animals_dict[count] = {
            'id': animal["id"],
            'type': animal["type"],
            'breed(primary)': animal["breeds"]["primary"],
            'color(primary)': animal["colors"]["primary"],
            'age': animal["age"],
            'gender': animal["gender"],
            'size': animal["size"],
            'coat': animal["coat"],
            'name': animal["name"],
            'description': animal["description"],
            'status': animal["status"],
            'published_at': animal["published_at"],
            'contact(email)': animal["contact"]["email"],
            'contact(phone)': animal["contact"]["phone"],
        }

        address_text = ""
        for line in animal["contact"]["address"].values():
            if (not line is None):
                address_text += line + " "
        animals_dict[count]['contact(address)'] = address_text
                
        # Add photos and videos
        try:
            photomedium = animal["primary_photo_cropped"]["medium"]
            animals_dict[count]['photos'] = photomedium
            animals_dict[count]['video'] = animal['videos'][0]["embed"]
        except TypeError:
            animals_dict[count]['photos'] = None
        except IndexError:
            animals_dict[count]['video'] = None
        count += 1

    animalsdf = pd.DataFrame.from_dict(animals_dict,
                                       orient='index')

    return animalsdf


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
        try:
            lastindex = name.rfind('-')
            if(lastindex > 0):
                name = name[:lastindex] + ' & ' + name[lastindex+1:]
                name = name.replace('-', ', ')
        except AttributeError:
            pass
        print(f'({index}) {name}')


# Ensures integer input
def handle_option(option):
    try:
        return int(option)
    except ValueError:
        return -1


# Send a get request to API with the filters the user requests
def build_url(dict_inputs):
    Get_Animals = 'https://api.petfinder.com/v2/animals'
    url = "https://api.petfinder.com/v2/animals?"
    No_preference = True
    for key, value in dict_inputs.items():
        if value is not None:
            No_preference = False
            url += f'{key}={value}&'
    url = url[:-1]
    print(url)
    if No_preference:
        return Get_Animals
    else:
        return url


# Function will handle user input prompts and structure stuff
def user_input():
    dict_inputs = {}

    # Request animal_type
    print_header('Available Animals for adoption')
    menu(ANIMAL_TYPES_LIST)
    option = handle_option(input('Animal preference: '))

    while(not valid_input(option, range(0, len(ANIMAL_TYPES_LIST)))):
        menu(ANIMAL_TYPES_LIST)
        option = handle_option(input('Animal preference: '))
    dict_inputs['type'] = ANIMAL_TYPES_LIST[option]

    print_header('Gender options')
    menu(ANIMAL_GENDERS_LIST)
    option = handle_option(input('Gender preference: '))
    while(not valid_input(option, range(0, len(ANIMAL_GENDERS_LIST)))):
        menu(ANIMAL_GENDERS_LIST)
        option = handle_option(input('Gender preference: '))
    dict_inputs['gender'] = ANIMAL_GENDERS_LIST[option]

    print_header('Age Ranges')
    menu(ANIMAL_AGE_LIST)
    option = handle_option(input('Age preference: '))
    while(not valid_input(option, range(0, len(ANIMAL_AGE_LIST)))):
        menu(ANIMAL_AGE_LIST)
        option = handle_option(input('Age preference: '))
    dict_inputs['age'] = ANIMAL_AGE_LIST[option]

    print_header('Animal Size')
    menu(ANIMAL_SIZE_LIST)
    option = handle_option(input('Size preference: '))
    while(not valid_input(option, range(0, len(ANIMAL_SIZE_LIST)))):
        menu(ANIMAL_SIZE_LIST)
        option = handle_option(input('Size preference: '))
    dict_inputs['size'] = ANIMAL_SIZE_LIST[option]
    # Request gender
    # age
    # size

    # Location Function
    # location = give_location()
    # if (location != None):
    #    return
    #    add to search paramaters?
    print_header('Would you like to give a location')
    menu(LOCATION_OPTIONS)
    option = handle_option(input('Choice: '))
    while(not valid_input(option, range(0, len(LOCATION_OPTIONS)))):
        menu(LOCATION_OPTIONS)
        option = handle_option(input('Choice: '))
    if option == 1:
        test = True
        error = ('https://www.petfinder.com/developers/v2/docs/errors/' +
                 'ERR-00002/')
        option = input('Enter your postal code: ')
        while(test):
            response = get_request(get_token(API_key, API_secret),
                                   'https://api.petfinder.com/v2/animals'
                                   + '?location=' + option)
            code = convert_to_json(response)
            try:
                if code['type'] != error:
                    print(code['type'])
                    test = False
            except KeyError:
                break
            option = input('Input valid postal code: ')
            print(test)
        dict_inputs['location'] = option
        print_header('Edit Search Range? (Default 100 miles)')
        menu(LOCATION_OPTIONS)
        option = handle_option(input('Choice: '))
        while(not valid_input(option, range(0, len(LOCATION_OPTIONS)))):
            menu(LOCATION_OPTIONS)
            option = handle_option(input('Choice: '))
        if option == 1:
            print_header('Search range(in miles): ')
            option = handle_option(input('Range(in miles): '))
            while(not valid_input(option, range(1, 501))):
                option = handle_option(input('Range(in miles): '))
            dict_inputs['distance'] = option

    return dict_inputs


# Takes Series, and displays values based on parameters and given format
# labelList and formList should be the same size as paramList and should align
# with parameter it is highlighting, otherwise function will use default format
# paramList: List of keys in dataSeries
#            If none inputed, will print all of them
# labelList: List of desired labels, is what is printed before parameter
#            If None is default is paramList
# formList: List of desired formatting, is what is printed after parameter
#           If None, default is newline
def display_profile(dataSeries, paramList=None, labelList=None, formList=None):
    if (paramList is None):
        paramList = dataSeries.keys().to_list()

    # Fill formlist with enough values to match paramlist
    if (formList is None):
        formList = []
    formList = formList + ("\n " * (len(paramList)-len(formList))).split(" ")

    # Ensure labelList is appropriate size by filling with values as needed
    if (labelList is None):
        labelList = paramList.copy()
        for i in range(0, len(paramList)):
            labelList[i] = labelList[i] + ": "
    elif len(labelList) < len(paramList):
        while (len(labelList) < len(paramList)):
            labelList.append(paramList[len(labelList)] + ": ")
    
    for i in range(0, len(paramList)):
        if labelList[i] is not None:
            print(f'{labelList[i]}', end='')
        print(f'{dataSeries.get(paramList[i])}', end=formList[i])


# Gets dataframe with animals and prints out information
def display_selected_animals(animalsdf):
    for index, animal in animalsdf.iterrows():
        print('({})'.format(index+1), end="\t")
        display_profile(animal,
                        paramList=["type", "age", "gender", "name"],
                        labelList=[ None, None, None, "Name: "],
                        formList=["\t", " ", "\t", "\n"])


# Gets dataframe with animals that may be selected
def user_select_animals(animalsdf):
    print("Based on your search criteria this is what we could find: \n")
    option = len(animalsdf)
    if (option == 0):
        print("_NONE_\nNo pets in the area based on your criteria")
    
    while(not (option == 0)):
        print_header(" List of Animals Found ")
        display_selected_animals(animalsdf)
        print(f'(0) Exit selection')
        
        option = handle_option(input("Select an animal:"))
        while(not valid_input(option, range(0, len(animalsdf)+1))):
            option = handle_option(input("Select an animal:"))
        if option == 0:
            return
        
        # Full animal profile display
        print_header("     Full Animal Profile     ")
        display_profile(animalsdf.iloc[option-1],
                        paramList=["id","name", "type", "age", "gender", "size",
                                   "color(primary)", "breed", "coat",
                                   "status",
                                   "photo", "video",
                                   "description",
                                   "contact(address)",
                                   "contact(email)","contact(phone)",
                                   "published_at"],
                        labelList=["ID:_","Name: ", "Type: ", "(", "~ ", "~ ",
                                   "~ ", "Breed: ", "Coat: ",
                                   "Adoption Status: ",
                                   "Photo Link:", "Video Link:",
                                   "Description:\n",
                                   "_Contact Information_\nAddress: ",
                                   "Email: ", "Phone: ",
                                   "Published on site at: "],
                        formList=["_\n", "\n", " ", " ", " ", " ",
                                  ")\n", "\n", "\n",
                                  "\n\n",
                                  "\n", "\n\n",
                                  "\n\n",
                                  "\n",
                                  "\n","\n\n"
                                  ,""]
                       )
        print_header("                             ")
        input("Press Enter to return to Select Screen: ")


if __name__ == '__main__':

    API_key2 = 'zJfcD6R6ADhwPimvTWthqhnv9zbA3JcHZCZwEToEUY7fq8BnsM'
    API_secret2 = 'RGkqeThwQVMg3eoVWJK3fuJkXVxX1TTVdLIyFeS3'

    AUTH_URL = 'https://api.petfinder.com/v2/oauth2/token'
    Get_Animals = 'https://api.petfinder.com/v2/animals'

    token = get_token(API_key, API_secret)

    # response = get_request(token, "https://api.petfinder.com/v2/types")
    # print(convert_to_json(response))

    output = user_input()
    url = build_url(output)
    response = get_request(token, url)
    # print(convert_to_json(response))
    animalsdf = parse_animals(convert_to_json(response))

    animalsdf.to_html(escape=False,
                         formatters=dict(photos=path_to_image_html))
    HTML(animalsdf.to_html(escape=False,
                              formatters=dict(photos=path_to_image_html)))
    animalsdf.to_html('webpage.html', escape=False,
                         formatters=dict(photos=path_to_image_html))
    
    user_select_animals(animalsdf)
