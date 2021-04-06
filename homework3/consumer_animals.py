''' Property of Justin Campbell; UT eID: jsc4348                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
    Purpose of Use: COE 332: Software Engineering and Design                                                                                                                                                                                                                 \
                                                                                                                                                                                                                                                                              
    Script File Name: consumer_animals.py                                                                                                                                                                                                                                    \
                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
        Homework #3: The Island of Dr. Moreau                                                                                                                                                                                                                                \
                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
Description: This script constitutes the second of two python scripts                                                                                                                                                                                                        \
                                                                                                                                                                                                                                                                              
used for homework assignment #3. This program uses the "requests" module                                                                                                                                                                                                      
to print the response from the url to look at properties such as "status_code",                                                                                                                                                                                               
"json()", and "headers" '''

# Import modules:                                                                                                                                                                                                                                                            \
                                                                                                                                                                                                                                                                              

import requests

''' Make a "GET" request to the "/animals" base URL in application running on                                                                                                                                                                                                 
    local host is specified by port number 5005 and capture response in                                                                                                                                                                                                       
    "response":'''
                                                                                                                                                                                                                                                                             \

response = requests.get(url='http://localhost:5005/animals')                                                                                                                                                                                                                 \

                                                                                                                                                                                                                                                                             \

# Return the response code:                                                                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                             \

print(response.status_code)                                                                                                                                                                                                                                                  \

print(response.json())
print(response.headers)
