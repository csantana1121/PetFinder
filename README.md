# PetFinder: Pet Adoption Finder ![license](https://img.shields.io/static/v1?label=license&message=MIT&color=red) ![license](https://img.shields.io/static/v1?label=Python&message=3.6.9&color=yellow&labelColor=blue)
![Sytle Guide Check](https://github.com/csantana1121/PetFinder/actions/workflows/github-style-checker.yaml/badge.svg) ![example branch parameter](https://github.com/csantana1121/PetFinder/actions/workflows/github-petfinder-tests.yaml/badge.svg)

## Project Description

This project works to query the user for their preferences and generate a list of pets up for adoption that meet those standards. Making use of the [PetFinder API](https://www.petfinder.com/developers/v2/docs/) to grab current data on adoptable pets at available shelters throughout the US, Canada, and Mexico. The program will then allow the user to see a generalized list of all the search results they requested and be able to look more in depth into each pet to see more specific information on each individual animal.

## Installation
### Libraries and Dependencies
After pulling this repo you will need to ensure that you have [python](https://www.python.org/downloads/) installed and the neccessary python libraries installed on your machine in order to be able to run the program. This program uses the [requests](https://docs.python-requests.org/en/master/), [pandas](https://pandas.pydata.org/), [plotly](https://plotly.com/python/), and [IPython](https://ipython.readthedocs.io/en/stable/index.html) libraries. To install each one run the following commands from the terminal command line or visit the docs for more details. Make sure all dependencies are installed before running this program.
```
sudo pip3 install requests
sudo pip3 install pandas
sudo pip3 install plotly
sudo pip3 install IPython
```
### How to install Petfinder
Clone this repo and navigate to its directory via the command line/terminal. Once inside run the following command to launch the program.
```
python3 Petfinder.py
```
Upon doing so your program will look like this
## License
See LICENSE.md in the root directory.
