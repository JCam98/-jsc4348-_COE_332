''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    
    Subject: 
        
        Week 2: JSON, Unit Testing, Version Control '''


'''                    Working with JSON 
                    
In this module, we will learn how to work with the JSON data format. JSON 
stands for "Javascript Object Notation", and is a powerful, flexible, and
lightweight data format that will be used a lot throughout this course, 
especially when working with web apps and REST APIs. It's flexible meaning
that it can be used with a wide variety of programming languages such as python
java, javascript, C and C++, and more. In the context of web applications 
that will be built in this course, JSON files are used to send information 
to and from these applications. '''  


''' Import "json" from the Python Standard Library (PSL) so that
we can work with the "json" class'''

import json 


'''                      Sample JSON 
                    
Analogous to Python dictionaries, JSON is typically composed of key value pairs.
The universality of this data structure makes it ideal for exchanging information
between programs written in different languages and web applications. A simple
JSON object looks like this: '''

{ 
 "key1": "value1",
 "key2": "value2"
 }

''' Although less common in this course, simple arrays of information (analogous)                  
to Python lists) are also valid JSON objects. Elements of JSON files must be 
unique: '''
    
[
 "thing1","thing2", "thing3"
 ]

''' JSON offers a lot of flexibility on the placement of white space 
and newline characters. Types can also be mixed together forming complex 
data structures: '''

{
 "department": "COE",
 "number": 332,
 "name": "Software Engineering and Design",
 "inperson": False,
 "instructors": ["Joe", "Charlie","Brandi","Joe"],
 "prerequisites": [
     {"course": "COE 332", "instructor": "Victor"},
     {"course": "SDS 332", "instructor": "Victor"}
     ]
      }

''' Use the "with open" statement to open a "json" file downloaded read-only 
into a filehandle called "f" '''

with open('states.json','r') as f: 
    states = json.load(f)
    
''' We use the "load" method of the "json" class to load the contents of the 
JSON file into an object called "states" '''
    
    
print(type(states))
print(type(states['states']))
print(type(states['states'][0]))
print(type(states['states'][0]['name']))
print(type(states['states'][0]['name'][0]))

print(states)
print(states['states'])
print(states['states'][0])
print(states['states'][0]['name'])
print(states['states'][0]['name'][0])
    
''' Let's Write a few Functions to determine whether or not the state abbreviations
are unique and thus abide by the rules of JSON objects: '''

''' The function "check_char_count()" checks whether there are exactly two 
characters in each of the abbreviations'''

def check_char_count(myabr):
    
    assert isinstance(myabr,str) # Input to this function should be a string
    
    if (len(myabr) == 2): 
        return(myabr + " count passes")
    else: 
        return (myabr + " count FAILS")  

''' The function "check_char_type()" is used to check whether both characters
are actually uppercase letters, and not something else like a number or a 
special character or a lowercase letter'''

def check_char_type(myabr):
    if (myabr.isalpha() and myabr.isupper()):
        return (myabr + " type passes")
    else: 
        return (myabr + " type FAILS")
        
''' The function "compare_first_char()" is used to check that the first character
of each abbreviation matches the first character of the corresponding state'''

def compare_first_char(myabr,mystate):
    if (myabr[0] == mystate[0]):
        return (myabr + " first character agrees with the state name")
    else: 
        return (myabr + " first character does not agree with the state name")
    
for i in range(50): 
    print(check_char_count(states['states'][i]['abbreviation']))     
    print(check_char_type(states['states'][i]['abbreviation'])) 
    print(compare_first_char(states['states'][i]['abbreviation'],\
                             states['states'][i]['name']))
    


