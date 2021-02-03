''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    
    Subject: 
        
        Week 2: JSON, Unit Testing, Version Control '''


'''    Creation of Objects and Writing to JSON files '''

import json

data = {}
data['class'] = 'COE332'
data['title'] = 'Software Engineering and Design'
data['subjects'] = []
data['subjects'].append( {'week': 1, 'topic': ['linux', 'python']} )
data['subjects'].append( {'week': 2, 'topic': ['json', 'unittest', 'git']} )

with open('class.json', 'w') as out:
    
    ''' The "json.dump()" method only requires two arguments - the object that
    should be written to the file, and the filehandle. The "indent = 2" 
    argument is optional, but it makes the output file look a little nicer
    and easier to read.'''
    
    json.dump(data, out, indent=2)
    
    
