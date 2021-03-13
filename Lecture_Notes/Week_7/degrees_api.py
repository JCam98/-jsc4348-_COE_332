''' Property of Justin Campbell; UT eID: jsc4348                                                                                                                                                                                                                              
    Purpose of Use: COE 332: Software Engineering and Design                                                                                                                                                                                                                  
    Script File Name: degrees_api.py                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                              
    Subject:                                                                                                                                                                                                                                                                  
                                                                                                                                                                                                                                                                              
        Week 7: Advanced Flask, Containerizing Flask                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                              
    Description: '''

import json, requests
import flask

app = flask.Flask(__name__)

''' Add a route "/degrees" that responds to HTTP "GET" verb and returns the                                                                                                                                                                                                   
complete list of data returned by "get_data": '''

@app.route('/degrees', methods=['GET'])
def get_data():

     ''' Serialize the list into a JSON-formatted string using the "json"                                                                                                                                                                                                     
         library. '''

     return json.dumps([{'id': 0, 'year': 1990, 'degrees': 5818}, \
            {'id': 1, 'year': 1991, 'degrees': 5725}, \
            {'id': 2, 'year': 1992, 'degrees': 6005}, \
            {'id': 3, 'year': 1993, 'degrees': 6123}, \
            {'id': 4, 'year': 1994, 'degrees': 6096}])

''' Make a "GET" request to the "/degrees" URL and capture response in "r":                                                                                                                                                                                                   
                                                                                                                                                                                                                                                                              
r = requests.get(url='http://127.0.0.1:5005/')                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                              
Verify that the status code and content are correct                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                              
print(r.status_code)                                                                                                                                                                                                                                                          
print(r.content)                                                                                                                                                                                                                                                              
print(r.json()) '''

''' The issue with the code above has to do with the content-type header                                                                                                                                                                                                      
being returned by the degrees API'''

''' Define method "set_json()" to write python object to a json file called"stats.json" '''

def set_json():

    with open('stats.json', 'w') as out:

        json.dump([{'id': 0, 'year': 1990, 'degrees': 5818}, \
            {'id': 1, 'year': 1991, 'degrees': 5725}, \
            {'id': 2, 'year': 1992, 'degrees': 6005}, \
            {'id': 3, 'year': 1993, 'degrees': 6123}, \
            {'id': 4, 'year': 1994, 'degrees': 6096}],out, indent=2)


''' Call function "set_json()" to write id, year, and degrees data to json file'''

set_json()

''' Define "read_json()" function to read in json file "stats.json" into a                                                                                                                                                                                                    
json object called "stats": '''

@app.route('/degreescheck', methods=['GET'])
def read_json():
    with open('stats.json', 'r') as f:
        stats = json.load(f)

        return json.dumps(stats)

''' Define route to characterize a third method of returning the contents                                                                                                                                                                                                     
of a JSON string from exportable python object using the "jsonify()" method: '''

@app.route('/degreesjsonify', methods=['GET'])
def get_json_jsonify():

    ''' Check response from the url '''

    response = requests.get(url="http://localhost:5005/stats.json")

    print(response.headers)
    print(response.status_code)

    ''' Print the value of the "id" query parameter(According to the url defined above, there should be no query parameters. This should return "None" '''

    print(flask.request.args.get('id'))

    return flask.jsonify([{'id': 0, 'year': 1990, 'degrees': 5818}, \
            {'id': 1, 'year': 1991, 'degrees': 5725}, \
            {'id': 2, 'year': 1992, 'degrees': 6005}, \
            {'id': 3, 'year': 1993, 'degrees': 6123}, \
            {'id': 4, 'year': 1994, 'degrees': 6096}])


''' Define a route to characterize a fourth method of returning the contents                                                                                                                                                                                                  
of a JSON string from an exportable python object. In particular, this route                                                                                                                                                                                                  
will use a "limit" query to give the user the option to limit the number of                                                                                                                                                                                                   
degrees that will be returned to the terminal '''

@app.route('/degrees/limit', methods=['GET'])
def get_formatted_json():

        limit_str = flask.request.args.get('limit')
        limit = int(limit_str)

        stats = json.dumps([{'id': 0, 'year': 1990, 'degrees': 5818}, \
            {'id': 1, 'year': 1991, 'degrees': 5725}, \
            {'id': 2, 'year': 1992, 'degrees': 6005}, \
            {'id': 3, 'year': 1993, 'degrees': 6123}, \
            {'id': 4, 'year': 1994, 'degrees': 6096}])

        ''' Loop through each of the degrees, if the value is greater than the                                                                                                                                                                                                
                                                                                                                                                                                                                                                                              
        threshold limit read in from the query, replace it with that value '''

        degree1 = int(stats[36] + stats[37] + stats[38] + stats[39])
        degree2 = int(stats[78] + stats[79] + stats[80] + stats[81])
        degree3 = int(stats[120] + stats[121] + stats[122] + stats[123])
        degree4 = int(stats[162] + stats[163] + stats[164] + stats[165])
        degree5 = int(stats[204] + stats[205] + stats[206] + stats[207])

        degrees = [degree1,degree2,degree3,degree4,degree5]

        ''' Assumption is made that the limit will be in the thousands (4 digits) '''

        stats_new=[] # Initialize empty list because lists in python are immutable                                                                                                                                                                                            

        for i in range(0,len(stats)):
            stats_new.append('0')

        ''' Assign all non-numeric(unchanging) values from old to new stats list '''

        for i in range(0,35):
            
            stats_new[i] = stats[i]

        for i in range(40,77):
                 stats_new[i] = stats[i]

        for i in range(82,119):
                 stats_new[i] = stats[i]

        for i in range(124,161):
                 stats_new[i] = stats[i]

        for i in range(166,203):
                 stats_new[i] = stats[i]

        for i in range(208,210):
                 stats_new[i] = stats[i]

        ''' Loop through "degrees" list to check if number exceeds threshold set by                                                                                                                                                                                           
        "limit". If so, assign "limit" value to the appropriate indices in the new                                                                                                                                                                                            
        list '''


        for i in range(0,5):
            if (degrees[i] > limit):

                if (i == 1):
                    stats_new[36*i] = limit_str[0]
                    stats_new[(36*i)+1] = limit_str[1]
                    stats_new[(36*i)+2] = limit_str[2]
                    stats_new[(36*i)+3] = limit_str[3]
                else:
                    stats_new[36 + (42*(i-1))] = limit_str[0]
                    stats_new[36 + (42*(i-1)) + 1] = limit_str[1]
                    stats_new[36 + (42*(i-1)) + 2] = limit_str[2]
                    stats_new[36 + (42*(i-1)) + 3] = limit_str[3]

        # Pack new list into JSON file object:                                                                                                                                                                                                                                

        stats_return = json.dumps(stats_new)

        return stats_return

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')