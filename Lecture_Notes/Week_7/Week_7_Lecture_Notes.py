''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    
    Subject: 
        
        Week 7: Advanced Flask, Containerizing Flask 
        
    Description: In this seventh week of class, we will dive deeper into the 
    Flask framework to see how it can employ multiple URLs/endpoints, 
    receive and decode JSON data, and handle query parameters. We will also
    containerize a Flask app using Docker. 


                               Defining the URLs of Our API
                               
The first basic goal of our API is to provide an interface to our dataset, 
which is a set of data points in a time series. Since the URLs in a 
REST API are defined by the "nouns" or collections of the application domain, 
we can use a noun that represents. 

For example, suppose that we have the following dataset that represents the 
number of students earning an undergraduate degree for a given year: '''

def get_data(): 
    return [{'id': 0, 'year': 1990, 'degrees': 5818}, \
            {'id': 1, 'year': 1991, 'degrees': 5725}, \
            {'id': 2, 'year': 1992, 'degrees': 6005}, \
            {'id': 3, 'year': 1993, 'degrees': 6123}, \
            {'id': 4, 'year': 1994, 'degrees': 6096}]

''' In this case, the collection described by the data is "degrees". So, 
we can define a route, "/degrees" that by default, returns all of the data 
points. '''

''' Does "curl localhost:5005/degrees" return the entire list as expected?? 

The answer is NO! 

Flask only allows the user three options for creating responses: 
    
    1) Return a string (str) object
    2) Return a raw bytes object
    3) Return a flask.Response object
    
Important Notes: 
    
    1) Option 1 is good for text or html such as when returning a web page
    or text file. 
    2) Option 2 is useful when returning binary data such as an image or
    an audio file. 
    3) Option 3 gives you the most flexibility, as it allows for you to 
    customize the headers and other aspects of the response
    
For our REST API, we will return JSON data, which is a string that has been 
formatted in a special way. But, instead of returning a string directly, 
we will use a flask helper function, flask.jsonify

                                 Working with JSON 
                                 
JSON is a data serialization format that is becoming one of the most popular
data formats on the web. Recall the basics of JSON: 
    
    1) JSON allows for one to convert from structured data objects (ex: Python
    lists or dictionaries) to strings that can be transmitted over a network 
    as "messages".
    2) JSON also allows one to convert these strings back to structured data 
    objects.
    3) The process of converting from structured data to a string is called
    "encoding". 
    4) The reverse process of converting JSON-formatted string to a structured
    data object is called "decoding"/ 
    
Modern programming languages provide libraries for "encoding" and "decoding"
JSON data. For Python: 
    
    1) The "json" library is part of the standard library and can be imported 
    with "import json". 
    2) The "json.dumps()" function will encode a Python object and return a 
    string. 
    3) The "json.loads()" function will decode a JSON string and create a Python
    object
    4) Only relatively "simple" Python objects can be encoded; just built-in
    types: str, int, bool, float, list, dict. 
    5) Only properly formatted JSON strings can be decoded, otherwise a 
    "JSONDecodeError" exception will be thrown.


                               HTTP Headers

1) Requests and Responses have "headers" which describes additional 
metadata about them. 
2) Headers are "key:value" pairs (much like dictionary entries.) The key is 
called the header name and the value is the header value. 
3) There are many pre-defined headers for common metadata such as specifying
the size of the message (Contet-Length), the domain the server is listening
on (Host) and the type of content included in the message (Content-Type)
                                  
                                  
                                Media Type (Mime Type)
                                
The allowed values for the "Content-Type" header are the defined "media types" 
(formerly, mime types).The main thing you want to know about media types 
are that they: 
    
    1) Consist of a type and subtype
    2) the most common types are "application", "text", "audio", "image", and 
    "multipart".
    3)The most common values (type and subtype) are "application/json", 
    "application/xml", "text/html", "audio/mpeg", "image/png", and 
    "multipart.form-data")
                                                                    
                             Content Types in Flask
                             
The Flask library has the following built-in conventions that you want to 
keep in mind: 
    
    1) When returning a string as part of a route function in Flask, a 
    "Content-Type" of "text/html" is returned
    2) To convert a Python object to a JSON-formatted string and set the 
    content type properly, use the "flask.jsonify()" function. 
                                                            
For example, "return flask.jsonify(['a', 'b', 'c'])" will convert the list to a
JSON string and return a content type of application/json.

                             Query Parameters 
                             
The HTTP spec allows for parameters to be added to the URL in form 
"key=value" pairs. Query parameters come after a "?" character and are 
separated by "&" characters; for example the following request: 
    
    "GET https://api.example.com/degrees?limit=3&offset=2"
    
passes two query parameters: "limit=3" and "offset=2" 

In REST architectures, query parameters are often used to allow clients to 
provide additional, optional arguments to the request. 

Common uses of query parameters in RESTful API:
    
    
    1) Pagination: Specifying a specific page of results from a collection
    2) Search Terms: Filtering the objects within a collection by additional
    search attributes
    3) Other parameters that might apply to most if not all collections such 
    as an ordering attribute (ascending vs. descending) 
    
                   Extracting Query Parameters in Flask
    
Flask makes the query parameters available on the "request.args" object, 
which is a "dictionary-like" object. To work with the query parameters 
supplied on a request, add the following: 

1) Import the "request" object at the top of your program: 
                                                                    
"from flask import request" 

2) In your route function, use the "get.()" method on the "request.args"
object to get the value of a parameter

For example: 
    
    from flask import Flask, request
    
    @app.route('/degrees', methods=['GET'])
    def degrees():
        start = request.args('start')
        
Note: The "start" variable will be the value of the "start" parameter, if 
one is passed, or it will be "None" otherwise. Also, "request.args.get()" 
will always return a string regardless of the type of data being passed in


                              Dockerizing Flask
                              
The following steps walk through the process of containerizing - Dockerizing
a Flask application

1) Create your web directory and change directories to it
                                                                    
"mkdir web"
"cd web"

2) Save/Create your web application script (ex: app.py) in this folder
                                                                    
3) Create a requirements file "requirements.txt" in your web directory 
and add Flask==1.1.1

4) Create your dockerfile: 
                                                                    
FROM ubunutu: latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

5) Build your image: 
                                                                    
"docker build -t flask-helloworld:latest ."

6) Run the container: 
                                                                    
"docker run --name "give your container a name" -d -p <your port number>:5000 flask-helloworld"

7) Verify that Container is Running: 
                                                                    
"docker ps -a"

Note: If things are good, you should see your container running on your port

7a) If things aren't right: 

"docker logs "your container name" 

or "docker logs "your container number" 

8) Curl your port:
                                                                    
"curl localhost:<your portnumber>"

9) Conserve Memory: 
                                                                    
To clean up after yourself, find your containe number, and pause it. 

"docker ps -a"

"docker stop <your container number>"

'''



        
