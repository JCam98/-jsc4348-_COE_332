''' Property of Justin Campbell; UT eID: jsc4348                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
    Purpose of Use: COE 332: Software Engineering and Design                                                                                                                                                                                                                 \
                                                                                                                                                                                                                                                                              
    Script File Name: app.py                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        Midterm Project: The Island of Dr. Moreau                                                                                                                                                                                                                            \
                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                              
Description: This python script contains the flask application for the midterm
project that contains routes that will: 
    
    1) query a range of  dates
    2) selects a particular creature by its unique identifier
    3) edits a particular creature by passing the UUID, and updated stats
    4) deletes a selection of animals by a date range(s)
    5) returns the average number of legs per animal
    6) returns a total count of animals   '''

# Import modules:                                                                                                                                                                                                                                                            \
                                                                                                                                                                                                                                                                              

import json, flask

''' Open the json file in read-only mode and assign contents                                                                                                                                                                                                                  
    of file to datastructure "animals": '''

with open('animals.json','r') as f:
            animals= json.load(f)

app = flask.Flask(__name__) # Use "Flask()" method to create web app                                                                                                                                                                                                          

''' Define route "/animals/query_dates" that queries a range of dates. Note: This 
route is defined such that there are three pairs of query parameters, namely,
minutes, seconds, and microseconds In order for this route to return a range of
dates, each of these query parameters (6 in total) must be read in
through the command line". In particular: 
    
    "initial_min" - string containing the initial minute of date range
    "final_min" - string containing the final minute of date range
    "initial_sec" - string containing the initial second of date range
    "final_sec" - string containing the final second of date range
    "initial_microsecond" - string containing the initial microsecond of date range
    "final_microsecond" - string containing the final microsecond of date range '''

@app.route('/animals/query_dates', methods=['GET'])
def query_dates():

     ''' Get the "initial_min" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "initial_min_str '''

     initial_min_str = flask.request.args.get('initial_min')
     initial_min = int(initial_min_str)

     ''' Get the "final_min" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "final_min_str '''

     final_min_str = flask.request.args.get('final_min')
     final_min = int(final_min_str)
     
     ''' Get the "initial_sec" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "initial_sec_str '''

     initial_sec_str = flask.request.args.get('initial_sec')
     initial_sec = int(initial_sec_str)
     
     ''' Get the "final_sec" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "final_sec_str '''

     final_sec_str = flask.request.args.get('final_sec')
     final_sec = int(final_sec_str)
     
     ''' Get the "initial_microsecond" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "initial_micro_str '''

     initial_micro_str = flask.request.args.get('initial_microsecond')
     initial_microsecond = int(initial_micro_str)
     
     ''' Get the "final_microsecond" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "final_micro_str '''

     final_micro_str = flask.request.args.get('final_microsecond')
     final_microsecond = int(final_micro_str)

     query_date_struct = {'StartMinute': initial_min, 'StartSecond': initial_sec,
                          'StartMicrosecond': initial_microsecond, 
                          'FinalMinute': final_min, 'FinalSecond': final_sec, 
                          'FinalMicrosecond': final_microsecond}    

     return query_date_struct

''' Define route "/animals/creature/UUID " to return a particular creature by
its unique identifier. Note: The http shortcut, "%20" must be inserted into the
curl request command to fill in any spaces in query parameter values.: '''

@app.route('/animals/creature/UUID', methods=['GET'])
def get_creature_UUID():

     ''' Get the "UUID" query parameter from the command line and assign                                                                                                                                                                                                  
     to string "UUID" '''

     UUID = flask.request.args.get('UUID')   

     ''' Intitialize a list to return creature with unique identifier '''

     animal_list = []                                                                                                                                                                                                      

     ''' Define a "for loop" to iterate through each of the animals in the                                                                                                                                                                                                    
     "animals" json data structure. Append the animal with UUID equal                                                                                                                                                                                                   
     to "UUID" value read in through the route, to the "animal_list" list                                                                                                                                                                                             
     and return to console '''

     for i in range(0,len(animals['animals'])):
         if (animals['animals'][i]['UUID'] == UUID):
             animal_list.append(animals['animals'][i])

     ''' Assemble "animal_list" data into a dictionary and create an exportable                                                                                                                                                                                               
     json object '''

     animal_struct = {'animals': animal_list}

     return animal_struct


''' Define route "/animals/creature/UUID/stats" to update the statistics (leg
number) of an animal with the unique identifier read in through the query 
parameter, "UUID", and return the animal to the console: '''

@app.route('/animals/creature/UUID/stats', methods=['GET'])
def get_updated_creature():

     ''' Get the "UUID" query parameter from the command line and assign to 
     string "UUID": '''
     
     UUID = flask.request.args.get('UUID')

     ''' Get the "tailnum" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "tail_num_str '''

     tail_num_str = flask.request.args.get('tailnum')
     tail_num = int(tail_num_str)

     animal_list = [] # Initialize empty list for animal dictionaries                                                                                                                                                                                                         

     ''' Define a "for loop" to iterate through each of the animals in the                                                                                                                                                                                                    
     "animals" json data structure. Append the animal with the UUID equal                                                                                                                                                                                                    
     to "UUID" value read in through the route, to a new list, "animal_list",
     and update the tail number (statisic) of this animal using the query parameter'''

     for i in range(0,len(animals['animals'])):
         if (animals['animals'][i]['UUID'] == UUID):
             
             animals['animals'][i]['tails'] = tail_num
             
             animal_list.append(animals['animals'][i])
             

     ''' Assemble "animal_list" data into a dictionary and create an exportable                                                                                                                                                                                               
     json object '''

     animal_struct = {'animals': animal_list}

     return animal_struct
 
    
 
''' Define route "/animals/delete" to delete a selection of animals by a date
range read in through the route. Note: This route is defined such that 
there are three pairs of query parameters, namely, minutes, seconds, and microseconds
In order for this route to return an updated list of animals, each of these
query parameters (6 in total) must be read in through the command line". In particular: 
    
    "initial_min" - string containing the initial minute of date range
    "final_min" - string containing the final minute of date range
    "initial_sec" - string containing the initial second of date range
    "final_sec" - string containing the final second of date range
    "initial_microsecond" - string containing the initial microsecond of date range
    "final_microsecond" - string containing the final microsecond of date range
    
Then, the updated list of animals will be returned to the console:'''

@app.route('/animals/delete', methods=['GET'])
def get_updated_animal_list():
    
     
     ''' Get the "initial_min" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "initial_min_str '''

     initial_min_str = flask.request.args.get('initial_min')
     initial_min = int(initial_min_str)

     ''' Get the "final_min" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "final_min_str '''

     final_min_str = flask.request.args.get('final_min')
     final_min = int(final_min_str)
     
     ''' Get the "initial_sec" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "initial_sec_str '''

     initial_sec_str = flask.request.args.get('initial_sec')
     initial_sec = int(initial_sec_str)
     
     ''' Get the "final_sec" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "final_sec_str '''

     final_sec_str = flask.request.args.get('final_sec')
     final_sec = int(final_sec_str)
     
     ''' Get the "initial_microsecond" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "initial_micro_str '''

     initial_micro_str = flask.request.args.get('initial_microsecond')
     initial_microsecond = int(initial_micro_str)
     
     ''' Get the "final_microsecond" query parameter from the command line and assign                                                                                                                                                                                                   
     to string "final_micro_str '''

     final_micro_str = flask.request.args.get('final_microsecond')
     final_microsecond = int(final_micro_str)

     ''' Initialize empty list to assign animals whose time stamps of creation
     fall outside of the specified query range for minute parameter '''

     animal_list_min = []                                                                                                                                                                                                       

     ''' Define a "for loop" to iterate through each of the animals in the                                                                                                                                                                                                    
     "animals" json data structure. Append the animal with a minute paramter
     that lies on the bounds, or outside of the initial and final bounds, to the list 
     "animal_list_min"  '''                                                                                                                                                                                                  

     for i in range(0,len(animals['animals'])):
         
         # Get the first character of minute from the timestamp: 
         
         timestamp_min_1 = animals['animals'][i]['timestamp'][14]
         
         # Get the second character of minute from the timestamp: 
             
         timestamp_min_2 = animals['animals'][i]['timestamp'][15]
         
         # Concatenate the two characters into a single string: 
             
         timestamp_min_str = timestamp_min_1 + timestamp_min_2
         
         # Convert the timestamp from a string to integer type: 
             
         timestamp_min = int(timestamp_min_str)
             
         # Append animal to list if minute of creation lies outside of range: 
             
         if (timestamp_min <= initial_min or timestamp_min >= final_min):
             
             animal_list_min.append(animals['animals'][i])


     ''' Assemble "animal_list_min" data into a dictionary and create 
     an exportable json object '''

     animals_struct = {'animals': animal_list_min}
     
     ''' Initialize empty list to assign animals whose time stamps of creation
     fall both fall in between the specified query ranges for minute and second
     of creation '''

     animal_list_min_sec = []                                                                                                                                                                                                       

     ''' Define a "for loop" to iterate through each of the animals list
     "animal_list_min". Append the animal with a secparamter
     that lies either on one of the bounds, or outside the initial and final
     bounds for the second parameters, to the list, "animal_list_min_sec"  '''                                                                                                                                                                                                  

     for i in range(0,len(animals_struct['animals'])):
         
         # Get the first character of second from the timestamp: 
         
         timestamp_sec_1 = animals_struct['animals'][i]['timestamp'][17]
         
         # Get the second character of minute from the timestamp: 
             
         timestamp_sec_2 = animals_struct['animals'][i]['timestamp'][18]
         
         # Concatenate the two characters into a single string: 
             
         timestamp_sec_str = timestamp_sec_1 + timestamp_sec_2
         
         # Convert the timestamp from a string to integer type: 
             
         timestamp_sec = int(timestamp_sec_str)
             
         ''' Append animal to list if second of creation lies outside of range
         or on one of the bounds '''
             
         if (timestamp_sec <= initial_sec or timestamp_sec >= final_sec):
             
             animal_list_min_sec.append(animals_struct['animals'][i])
      
     ''' Assemble "animal_list_min_sec" data into a dictionary and create 
     an exportable json object '''

     animals_struct = {'animals': animal_list_min_sec}       

     ''' Initialize empty list to assign animals whose time stamps of creation
     fall outside of, or on one of the bounds of the microsecond parameter time range: '''

     animal_list_min_sec_mic = []                                                                                                                                                                                                       

     ''' Define a "for loop" to iterate through each of the animals in list
     "animal_list_min_sec". Append the animal with a microsecond parameter
     that lies outside of, or on one of the bounds of the microsecond parameter
     time range, to the list, "animal_list_min_sec_mic"  '''                                                                                                                                                                                                      

     for i in range(0,len(animals_struct['animals'])):
         
         # Get the six characters of microsecond from the timestamp: 
         
         timestamp_micsec_1 = animals_struct['animals'][i]['timestamp'][20]
         timestamp_micsec_2 = animals_struct['animals'][i]['timestamp'][21]
         timestamp_micsec_3 = animals_struct['animals'][i]['timestamp'][22]
         timestamp_micsec_4 = animals_struct['animals'][i]['timestamp'][23]
         timestamp_micsec_5 = animals_struct['animals'][i]['timestamp'][24]
         timestamp_micsec_6 = animals_struct['animals'][i]['timestamp'][25]
         
         # Concatenate the characters into a single string: 
             
         timestamp_micsec_str = timestamp_micsec_1 + timestamp_micsec_2 + timestamp_micsec_3 \
             + timestamp_micsec_4 + timestamp_micsec_5 + timestamp_micsec_6
         
         # Convert the timestamp from a string to integer type: 
             
         timestamp_micsec = int(timestamp_micsec_str)
             
         ''' Append animal to list if microsecond of creation lies outside of
         the range or on one of the bounds '''
             
         if (timestamp_micsec < initial_microsecond or timestamp_micsec > final_microsecond):
             
             animal_list_min_sec_mic.append(animals_struct['animals'][i])

             
     ''' Assemble "animal_list_min_sec_mic" data into a dictionary and create 
     an exportable json object '''

     animal_struct = {'animals': animal_list_min_sec_mic}

     return animal_struct    

''' Define route "/animals/average_leg_num" to return the average number of
legs per animal: '''

@app.route('/animals/average_leg_num', methods=['GET'])
def get_avg_leg_num():

     ''' Initialize list to store the leg number for each animal: '''
     
     leg_num_list = []

     ''' Use a for loop to assign the leg number for each animal to the list'''

     for i in range(0,len(animals['animals'])):
         leg_num_list.append(animals['animals'][i]['legs'])
         
     ''' Evaluate the average leg number '''
     
     avg_leg_num = sum(leg_num_list) / len(leg_num_list)
     
     ''' Convert float type to string to return to console: '''
     
     avg_leg_num = str(avg_leg_num)

     return avg_leg_num

''' Define route "/animals/total_count" to return the total number of animals: '''

@app.route('/animals/total_count', methods=['GET'])
def get_total_animal_count():

     animal_count = len(animals['animals'])
     
     ''' Convert int type to string to return to console: '''
     
     animal_count = str(animal_count)

     return animal_count


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
