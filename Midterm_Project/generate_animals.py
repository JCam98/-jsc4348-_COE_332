''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    Script File Name: generate_animals.py 
 
        
     Midterm Project:  The Island of Dr. Moreau
        
Description: This script represents a modification of the "generate_animals.py"
script developed in Homework1 where a timestamp, and unique identifier are added
as key-value pair elements to the animals data structure. In turn, the associated
"animals.json" file that is written out at the end of the program, in conjnuction
with this "generate_animals.py" script will be included in the submission for 
this project.                                         
                                                                                                        
'''

# Import modules:       
    
import json, petname, random, datetime, uuid 

''' Initialize list "head_choices" with the five animal head choices: '''

head_choices = ["snake", "bull", "lion", "raven", "bunny"]
animal_list = [] # Initialize data structure to contain dictionaries of animals

for i in range(0,20):
    
    ''' Invoke "random()" method to randomly generate one of the head choices: '''
    
    head_type = head_choices[random.randint(0,4)]
    
    ''' Invoke "name()" method to randomly generate two animal strings for 
    the two body components: '''
    
    body_comp_1 = petname.name()
    body_comp_2 = petname.name()
    
    ''' Employ "while loop" to ensure that the two components of the body 
    are not identical '''
    
    while (body_comp_1 == body_comp_2):
        body_comp_2 = petname.name()
    
    
    ''' Generate a random even number of arms between 2 and 10 inclusive: '''
    
    arms_number = random.randint(2,10)
    
    ''' Employ "while loop" to ensure that the number of arms meets the 
    aforementioned criteria: '''
    
    while ((arms_number % 2) > 0):
        arms_number = random.randint(2,10)
    
    ''' Generate a random number of legs that is both a multiple of three and 
    between the numbers 3, and 12 inclusive: '''
   
    legs_number = random.randint(3,12)
   
    ''' Employ "while loop" to ensure that the number of legs meets the 
    aforementioned criteria: '''
    
    while ((legs_number % 3) != 0):
        legs_number = random.randint(3,12)
        
    
    ''' Append a non-random number of tails that is equal to the sum of the 
    number of arms and legs: '''
    
    tails_num = arms_number + legs_number
    
    # Invoke "uuid4()" method to assign random unique identifier to animal
    
    UUID = str(uuid.uuid4())
    
    # Invoke "now()" method from "datetime" module to assign random timestamp
    
    timestamp = str(datetime.datetime.now())
      
    animal_list.append({'head': head_type, \
                        'body': body_comp_1 + "-" + body_comp_2, \
                            'arms': arms_number, 'legs': legs_number, \
                                'tails': tails_num, 'UUID': UUID, 'timestamp':timestamp})
        
''' Insert the list of dictionaries data structure "animal_list" into a 
dictionary to create an exportable JSON object: '''

animal_struct = {'animals': animal_list}
    
''' Use the JSON library to dump the data structure into a file called 
"animals.json": '''

with open('animals.json', 'w') as out:
    json.dump(animal_struct, out, indent=2)
