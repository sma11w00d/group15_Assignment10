# Name: Group 15 (Sam Smallwood, Ben Castro)
# email: castroba@mail.uc.edu smallwse@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/9/2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: this module pulls sweet dog facts from a cool dog facts API and saves them as a list of dictionaries, then prints them out.
# Citations:
# Anything else that's relevant: https://kinduff.github.io/dog-api/
 
#main.py
import json
import requests
import random
 
if __name__ == "__main__":
    response = requests.get('https://dogapi.dog/api/v2/breeds/')
    if response.status_code == 200:
        data = response.json()
        breed_data_list = data.get('data')#saves data as a list of dictionaries from the api
    
        if breed_data_list: #checks if breed_data_list is empty
            breed_data = random.choice(breed_data_list)  # randomly selects a dog dictionary from the list of dictionaries to display
    
            name = breed_data.get('attributes', {}).get('name') #saves the name from the selected dictionary to a variable
            description = breed_data.get('attributes', {}).get('description')#saves the description from the selected dictionary to a variable
            hypoallergenic = breed_data.get('attributes', {}).get('hypoallergenic')#saves the hypoallergenic status from the selected dictionary to a variable
 
            print(f"Name: {name}")
            print(f"Description: {description}")
            print(f"Hypoallergenic: {'Yes' if hypoallergenic else 'No'}")
 
    else:
        print("Error: Unable to fetch data from the API. Status code:", response.status_code)# prints if error occurs when reaching the API