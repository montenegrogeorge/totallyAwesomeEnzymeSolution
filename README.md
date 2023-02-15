# totallyAwesomeEnzymeSolution
A solution to the Food Stand Question for Enzyme. 

This application pulls JSON data from https://data.sfgov.org/resource/rqzj-sfat.json, cleans the data for missing values, then filters the data for the fields we are looking for. It then creates a dictionary with the key being the name of the establishment and the value being the distance from Union Square. 

This project uses the JSON module library to handle the json data, urlib for pulling the json data from the url, re for RegEx when filtering out the data, and finally geopy to calculate the distance in miles from the coordinates provided. 

Moving foward, I will replace the use of the dictionary with a list, create additional functionality to sort and store the list in a separate JSON file, and convert the filters list to a dictionary to make it more flexible. 