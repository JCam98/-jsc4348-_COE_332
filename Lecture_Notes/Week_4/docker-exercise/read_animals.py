''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    Script File Name: read_animals.py 
 
        
        Homework #1: The Island of Dr. Moreau, Part b) 
        
Description: This script constitutes the second part of two scripts 
used for homework assignment #1. This program uses the I/O method "open()"
to read in the contents of the JSON file "animals.JSON" to a JSON object. 
The random module is then used to randomly choose one of the animal descriptions
to output to the console.'''
         
import json, random 

''' Open the json file "animals.json" in read-only mode and assign contents 
of file to datastructure "animals": '''

with open('animals.json','r') as f: 
        animals= json.load(f)

''' Print the details of one of the animals at random to the console: '''

print(animals['animals'][random.randint(0,20)])