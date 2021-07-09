# PetFinder: Pet Adoption Finder ![license](https://img.shields.io/static/v1?label=license&message=MIT&color=red) ![license](https://img.shields.io/static/v1?label=Python&message=3.6.9&color=yellow&labelColor=blue)
![Sytle Guide Check](https://github.com/csantana1121/PetFinder/actions/workflows/github-style-checker.yaml/badge.svg) ![example branch parameter](https://github.com/csantana1121/PetFinder/actions/workflows/github-petfinder-tests.yaml/badge.svg)

## Project Description

This project works to query the user for their preferences and generate a list of pets up for adoption that meet those standards. Making use of the [PetFinder API](https://www.petfinder.com/developers/v2/docs/) to grab current data on adoptable pets at available shelters throughout the US, Canada, and Mexico. The program will then allow the user to see a generalized list of all the search results they requested and be able to look more in depth into each pet to see more specific information on each individual animal. With the goal of allowing the user to find a pet that they would like to adopt that fits them.

## Installation
### Libraries and Dependencies
After pulling this repo you will need to ensure that you have [python](https://www.python.org/downloads/) installed and the neccessary python libraries installed on your machine in order to be able to run the program. This program uses the [requests](https://docs.python-requests.org/en/master/), [pandas](https://pandas.pydata.org/), [plotly](https://plotly.com/python/), and [IPython](https://ipython.readthedocs.io/en/stable/index.html) libraries. To install each one run the following commands from the terminal command line or visit the docs for more details. Make sure all dependencies are installed before running this program.
```
sudo pip3 install requests
sudo pip3 install pandas
sudo pip3 install plotly
sudo pip3 install IPython
```
### How to install and run Petfinder
Clone this repo and navigate to its directory via the command line/terminal. Once inside run the following command to launch the program.
```
python3 Petfinder.py
```
Upon doing so your program will start the interactive commandline interface requesting if you have any preferences for the adoptable animals you see. Asking for preferences on animal type, gender, age, size, location, search range, and the max number of search results you'd like to see. The interface will like so allowing for the user to select from a list of options.
![Available Animals](https://github.com/csantana1121/PetFinder/blob/master/data/images/Petfinderstartup.jpg?raw=true)
> Note: For location, search range, and max number of search results you will have to input your own value which will be validated by the program as a valid input. Valid inputs > will be made clear at each step. Like so
> 
![Location](https://github.com/csantana1121/PetFinder/blob/master/data/images/Petfinderpostalcode.jpg?raw=true)

After selecting your search parameters if you have any then the program will generate a list of generalized search results with an overview on the animal type, age, gender, and name of the animal allowing you to get an overview of all the animals and select which one you'd like to learn more about. 

![Overview](https://github.com/csantana1121/PetFinder/blob/master/data/images/Petfinderoverview.jpg?raw=true)

Selecting any animal will bring up its full profile allowing the user to see more information on the animal that is available. Then waiting for the user to input they'd like to go back to the full list or exit the program after they are done viewing adoptable pets. Example:

![Profile](https://github.com/csantana1121/PetFinder/blob/master/data/images/Petfinderprofile.jpg?raw=true)

### Using web-display functionality

The web display is currently in development and a fully functional finalized version is not complete. If after running the program you'd like to view your search results in a web format to see the pictures and videos in browser. Currently to view the web display you will have to open an html file with some internet browser to view the file. This html file will be located within the root directory of where you are running Petfinder.py and will be generated everytime you run the program. The output will be a chart display format of all search results displaying all the animal's information and haivng their picutre and video rendered to view alongside like so.

![Web-dispay](https://github.com/csantana1121/PetFinder/blob/master/data/images/Petfinderhtml.jpg?raw=true)
> Currently all information is displayed at once and the page is not properly formatted to display 1 animal's information neatly

[Check out a sample visualization of data](./webpage.html)
## Contributors
This project was developed and built by [Christian Santana](https://github.com/csantana1121) and [Anthony Meza](https://github.com/abmeza) in python within the Codio studio. Please reach out if you have questions or concerns!
## License
See LICENSE.md in the root directory.


