''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    
    Subject: 
        
        Week 2: JSON, Unit Testing, Version Control '''

      
    
import json

''' The function "check_char_count()" checks whether there are exactly two 
characters in each of the abbreviations'''

def check_char_count(myabr):
    if (len(myabr) == 2): 
        return(myabr + "count passes")
    else: 
        return (myabr + "count fails")  
    
''' Two element lists will pass through as arguments in this function. This 
function must be fixed such that lists do not pass through. '''

''' The function "check_char_type()" is used to check whether both characters
are actually uppercase letters, and not something else like a number or a 
special character or a lowercase letter'''

def check_char_type(myabr):
    if (myabr.isalpha() and myabr.isupper()):
        return (myabr + "type passes")
    else: 
        return (myabr + "type fails")
        
''' The function "compare_first_char()" is used to check that the first character
of each abbreviation matches the first character of the corresponding state'''

def compare_first_char(myabr,mystate):
    if (myabr[0] == mystate[0]):
        return (myabr + "first character agrees with the state name")
    else: 
        return (myabr + "first character does not agree with the state name")


def main():
    
    with open('states.json','r') as f: 
        states = json.load(f)
    
    for i in range(50): 
        print(check_char_count(states['states'][i]['abbreviation']))     
        print(check_char_type(states['states'][i]['abbreviation'])) 
        print(compare_first_char(states['states'][i]['abbreviation'],\
                                 states['states'][i]['name']))   
            
''' The last two lines make it so that the "main()" function is only called
if this script is executed directly, and not if it is imported into another 
script '''

if __name__ == '__main__':
    main()                                                         