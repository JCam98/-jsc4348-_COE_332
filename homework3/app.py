''' Property of Justin Campbell; UT eID: jsc4348                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
    Purpose of Use: COE 332: Software Engineering and Design                                                                                                                                                                                                                 \
                                                                                                                                                                                                                                                                              
    Script File Name: app.py                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
        Homework #3: The Island of Dr. Moreau                                                                                                                                                                                                                                \
                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
Description: This script constitutes the first of two scripts                                                                                                                                                                                                                 
used for homework assignment #3. This program generates a flask web application                                                                                                                                                                                               
and provides several routes for the user to return data such as animal body type, arm number, leg number, etc. from the animal JSON                                                                                                                                           
data generated from "generate_animals.py". '''

# Import modules:                                                                                                                                                                                                                                                            \
                                                                                                                                                                                                                                                                              

import json, flask

''' Open the json file in read-only mode and assign contents                                                                                                                                                                                                                  
    of file to datastructure "animals": '''

with open('animals.json','r') as f:
            animals= json.load(f)

app = flask.Flask(__name__) # Use "Flask()" method to create web app                                                                                                                                                                                                          

''' Define route "/animals" that invokes a function "get_animals()" to return                                                                                                                                                                                                 
a json-formatted string of each of the animals and their attributes: '''

@app.route('/animals', methods=['GET'])
def get_animals():

     return animals

''' Define route "/animals/headtype" that invokes a function "get_heads()" to return                                                                                                                                                                                          
a json-formatted string of each of the animals with a head type specified                                                                                                                                                                                                     
by a query parameter: '''

@app.route('/animals/headtype', methods=['GET'])
def get_head():

     ''' Get the "headtype" query parameter from the command line and assign                                                                                                                                                                                                  
     to string "head_type" '''

     head_type = flask.request.args.get('headtype')
     animal_list = [] # Initialize empty list for animal dictionaries                                                                                                                                                                                                         

     ''' Define a "for loop" to iterate through each of the animals in the                                                                                                                                                                                                    
     "animals" json data structure. Append each animal with head type equal                                                                                                                                                                                                   
     to "headtype" value read in through the route, to a new json data structure                                                                                                                                                                                              
     and return to console '''

     for i in range(0,len(animals['animals'])):
         if (animals['animals'][i]['head'] == head_type):
             animal_list.append(animals['animals'][i])

     ''' Assemble "animal_list" data into a dictionary and create an exportable                                                                                                                                                                                               
     json object '''

     animal_struct = {'animals': animal_list}

     return animal_struct


''' Define route "/animals/tailnum" that invokes a function "get_tails()" to return                                                                                                                                                                                           
a json-formatted string of each of the animals with tail number specified    
by a query parameter: '''

@app.route('/animals/tailnum', methods=['GET'])
def get_tails():

     ''' Get the "tailnum" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "tail_num_str '''

     tail_num_str = flask.request.args.get('tailnum')
     tail_num = int(tail_num_str)

     animal_list = [] # Initialize empty list for animal dictionaries                                                                                                                                                                                                         

     ''' Define a "for loop" to iterate through each of the animals in the                                                                                                                                                                                                    
     "animals" json data structure. Append each animal with tail num equal                                                                                                                                                                                                    
     to "tailnum" value read in through the route, to a new json data structure                                                                                                                                                                                               
     and return to console '''

     for i in range(0,len(animals['animals'])):
         if (animals['animals'][i]['tails'] == tail_num):
             animal_list.append(animals['animals'][i])

     ''' Assemble "animal_list" data into a dictionary and create an exportable                                                                                                                                                                                               
     json object '''

     animal_struct = {'animals': animal_list}

     return animal_struct

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
