''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    Script File Name: app.py
    
    Subject: 
        
        Week 6: Intro to APIs Introduction to Flask 
        
    Description: This script uses the "Flask" microservice framework 
    to run a local host'''
    
    
''' Import the Flask class. At the heart of every flask-based web program
is a "Flask application" object. The application object holds the primary
configuration and behaviors of the web program: '''

from flask import Flask 

''' Create a "Flask" application object passing "__name__" to the constructor
Note that "__name__" is a special python variable that gets set to either 
the module's actual name OR "main" in the case where the module was executed
directly by the python interpreter '''

app = Flask(__name__)

''' Define a "hello world" route for the base url by adding the following 
lines. Note: This will only work in the linux isp machine: '''

@app.route('/', methods=['GET'])

def hello_world():
    return "Hello world\n" 

# Define a route with URL parameters: 
    
@app.route('/<name>', methods=['GET'])
def hello_worlds(name):
    return "Hello {}\n".format(name)

'''Note: We put the variable name in angled brackers within the app route decorator.
We make the variable a parameter to the decorated function and use it just 
like any other variable. 

Then, the command "curl localhost:5005" can be run to return this string '''

# The following statement should usually appear at the bottom of a flask app: 
 
''' Launch the development server using the "app.run()" method if the "app.py"
module is executed from the command line: '''   

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
    
''' Notes: The "debug = True" tells flask to print verbose debug statements
while the server is running. The "host = 0.0.0.0" instructs the server to 
listen on all network interfaces; basically this means that you can reach 
the server from inside and outside the host VM. '''

''' There are two main ways of starting the flask service. For now, we would 
like you to start the service using a unique port number. The "-p 5000" 
indicates that flask is running on port 5000. You will need to use your own 
assigned port. Run the following commands to start a flask service (in linux machine): 
    
    "export FLASK_APP = app.py"
    "export FLASK_ENV = development"
    "flask run -h localhost -p 5005 "
    
    VERY IMPORTANT: Anytime I run "flask run" to create an active server 
    session in the foreground, I must use my designated port number (5005)
    
Now we have a server up and running!!!!!

Notes: 
    
    1) Note that the program took over the entire shell; we could have put 
    in the background, but for now we want to leave it in the foreground. 
    (Multiple PIDs are started for the flask app when started in daemon mode;
     to get them, find all processes listening on the port 5000 socket with 
     "lsof -i:5005")
    
    2) If we make changes to our flask app while the server is running, the 
    server will detect changes automatically and "reload"; you will see a 
    log to the effect of "Detected change in <file>"
    
    3) We can stop the program with "control + c" and put the server in the 
    background by running "control + z" followed by "bg"
    
    4) If we stop our flask program, the server will no longer be listening 
    and our requests will fail. '''

    
