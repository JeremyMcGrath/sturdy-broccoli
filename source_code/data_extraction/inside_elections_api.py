# File Name:    inside_elections_api.py
# Description:  Access Inside Elections API and retrieve necessary data. Clean data from source and submit to data_storage       
# URL:          https://insideelections.com/developer
#          
# Author:       Jeremy McGrath
# Date:         2022-04-29

# imports
import csv
import requests
import xml.etree.ElementTree as ET

# local imports
import helper_functions.states_data as states

# Access API and recieve data.
# As of 2022-04-29, data type XML
# New York Example: /api/xml/ratings/by-state/house/NY
def get_data():
    # Testing URL, NY House
    ny_house_url = 'https://insideelections.com/api/xml/ratings/by-state/house/NY'

    for state in states:
        print("State: {0},{1}".format(state[1],state[0]))

    # get request
    get_reponse = requests.get(ny_house_url)

    # saving the xml file
    with open('../data_storage/house/ny.xml', 'wb') as f:
        f.write(get_reponse.content)

def parse_data():
    pass

def main():
    
    get_data()          
      
if __name__ == "__main__":
    # calling main function
    main()