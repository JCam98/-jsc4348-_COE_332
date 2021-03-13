''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    
    Subject: 
        
        Week 6: Intro to APIs Introduction to Flask 
        
    Description: In this sixth week of class, we will be introduced to 
    Application Programming Interfaces (APIs). This will form the foundation
    of our ultimate goal to create large, complex, python-based applications
    that are accessible through the web. The particular REST API framework 
    we will be working with most is called Flask. 



        Introduction to APIs: 
            
        An Application Programming Interface (API) establishes the protocols
        and methods for one piece of a program to communicate with another. 
        APIs are useful for three things: 
            
            1) Allowing larger software systems to be built from smaller components
            2) Allowing the same component/code to be used by different systems
            3) Insulating consumers from changes to the implementation
    
    Some Examples of APIs: 
        
        1) In OOP languages, abstract classes provide the interface for all 
    concrete classes to implement
        2) Software libraries provide an external interface for consuming programs
        3) Web APIs (or "web services") provide interfaces for computer programs
    to communicate over the internet 
    
    
    Web APIs: 
        
        In this course, we will focus on Web APIs (or HTTP APIs). These are 
        interfaces that are exposed over HTTP. There are a number of advantages
        to Web-based APIs that we will use in this class: 
            
            1) A Web API is accessible from any computer or application 
    that has access to the public internet
            2) No software installation is required on the client's side to 
    consume a Web API. 
            3) Web APIs can change their implementation without clients 
    knowing (or caring).
            4) Virtually every modern programming language provides one more
    libraries for interacting with a web API - thus "language agnostic"
    
    HTTP - The Protocol of the Internet
    
    HTTP (Hyper Text Transfer Protocol) is one way for two computers on the 
    internet to communicate with each other. It was designed to enable the 
    exchange of data (specifically, "hypertext"). In particular, our web
    browsers use HTTP when communicating with web servers running web 
    applications. HTTP uses a message-based, client-server model: clients
    make requests to servers by sending a message, and servers respond by 
    sending a message back to the client. 
    
    HTTP is an "application layer" protocol in the language of the Internet 
    Protocols; it assumes a lower level transport layer protocol. While this can
    be swapped, in practice it is almost always TCP. The basics of the protocol: 
        
        1) Web resources are identified with URL's (Uniform Resource Locators).
    Originally, resources were just files/directories on a server, but today 
    resources refer to more general objects. 
        2) HTTP "verbs" represent actions to take on the resource. The most 
    common verbs are: "GET", "POST", "PUT", "DELETE"
        3) A request is made up of a URL, an HTTP verb, and a message. 
        4) A response consists of a status code (numerical between 100 - 599), 
    and a message. The first digit of the status code specifies the kind of 
    response: 
        
        a) 1xx - informational
        b) 2xx - success
        c) 3xx - redirection 
        d) 4xx - error in the request (client)
        e) 5xx - error in fulfilling a valid request (server)
    
    REST APIs - Overview: 
        
        REST (Representational State Transfer) is a way of building APIs for 
        computer programs on the internet leveraging HTTP. In other words, 
        a program on computer 1 interacts with a program on computer 2 by 
        making an HTTP request to it. 
        
        In HTTP terms, "resources" are the nouns of the application domain and 
        are associated with URLs. The API has a base URL from which all other
        URLs in that API are formed. ex: "https://api.github.com/"
        
        The other URLs in the API are either collections: 
            
            1) <base_url>/users
            2) <base_url>/files
            3) <base_url>/programs
    
        or they are specific items in a collection: 
            
            1) <base_url>/users/12345
            2) <base_url>/files/test.txt
            3) <base_url>/programs/myapplication
    
        or subcollections / items in subcollections: 
            
            1) <base_url>/companies/<company_id>/employees
            2) <base_url>/companies/<company_id>/employees/<employee_id>
    
    Continuing along with HTTP terms, "operations" are the actions that can 
    be taken on the resources and are associated with HTTP verbs: 
        
        1) "GET" - list items in a collectoin or retrieve a specific item in 
    the collection
        2) "POST" - create a new item in the collection based on the description
    in the message
        3) "PUT" - replace an item in a collection with the description in the
    message
        4) "DELETE" - delete an item in a collection 
    
    Response messages often make use of some data serialization format standard
    such as "JSON" or "XML"
    
    
    REST APIs - Toy Examples: 
        
        Virtually every application domain can be mapped into a REST API 
        architecture. Some examples may include: 
            
            1) Articles in a collection (ex: on a blog, or wiki) with 
    author attributes: 
        
        a) <base_url>/articles
        b) <base_url>/articles/<id>
        c) <base_url>/articles/<id>/authors
    
            2) Properties in a real estate database with associated purchase
    history: 
        
        a) <base_url>/properties
        b) <base_url>/properties/<id>
        c) <base_url>/properties/<id>/purchases
    
            3) A catalog of countries, cities, and neighborhoods: 
    
        a) <base_url>/countries
        b) <base_url>/countries/<country_id>/cities
        c) <base_url>/countries/<country_id>/cities/<city_id>/neighborhoods
    
    
    REST APIs - A Real Example: 
        
        Bitbucket is a website for managing git repositories. The base URL
        is "https://bitbucket.org/"
        
        Let's now take a look at the Bitbucket Web API. Open a web browser
        and navigate to "https://api.bitbucket.org/2.0/repositories" 
        
        When you opened that page, your browser made a "GET" request to 
        the Bitbucket API. What you see is a JSON object describing 
        public repositories. 
        
        Notice that there are three top level objects in the response: 
            "pagelen" (int), "values" (list), and "next" (str). What do you 
            think each of these represents? 
            
    Web APIs for popular sites (like Bitbucket) often come with online 
    documentation. 
    
    
    Using Python to Interact with Web APIs: 
        
        Viewing API response messages in a web browser is of limited use. 
        We can interact with Web APIs in a much more powerful and programmatic
        way using the Python "requests" library. 
        
        
        
     The basic usage of the "requests" library is as follows: '''
     
import requests
     
# response = requests.<method>(url=some_url, data=some_message,<other_options>
# The command above makes a request

# An example of request: 

response = requests.get(url = 'https://api.bitbucket.org/2.0/repositories') 

# return the status code: 

print(response.status_code)

# return the raw content: 

print(response.content)

# return a Python list or dictionary from the response message: 

print(response.json())      


''' If we wanted to, we could now extract specific information from 
the repositories and their features. '''

# Retrieve a list of public bitbucket repositories for a particular user: 
    
response = requests.get(url = "https://api.bitbucket.org/2.0/repositories/user/")    
    

''' Introduction to the Flask Web Server Microframework: 
    
Flask is a Python library and framework for building web servers. We want to 
learn how to provide web services. Some of the defining characteristics of 
Flask make it a good fit for the project: 

1) Flask is small, relatively easy to use and setup
2) Flask is "robust" - a great fit for REST APIs and "microservices". 
3) When used correctly, Flask is performant enough to handle the traffic of 
sites with 100K users. 

What is a Microservice????

Microservices - also known as the microservice architecture - is an architectural
style that structures an application as a collection of services that are: 

1) Highly maintainable and testable
2) Loosely coupled
3) Independently deployable
4) Organized around business capabilities 

The microservices architecture enables the continous delivery/deployment of 
large, complex applications. It also enables an organization to evolve its
technology stack. Sites that use microsevices include: 

1) Netflix 
2) Amazon 
3) eBay      
    
                             Ports: 
    
Ports are a concept from networking that allow multiple services or programs
to be running at the same time, listening for messages over the internet, 
on the same computer. 

1) For us, ports will always be associated with a specific IP address. In 
general, we specify a port by combining it with an IP separated by a colon 
character. For example, "129.114.97.16:5000". 

2) One and only one program can be listening on a given port at a time. 

3) Some ports are designated for specific activities; Port 80 is reserved
for HTTP, port 443 for HTTPS (encrypted HTTP) but other ports can be used for
HTTP/HTTPS traffic. 

    
Now, we'll use the command line HTTP client "curl" to make a request to our
Flask app on port 5005 (on linux machine): 
    
Curl Basics: 
    
    Intro: You can think of "curl" as a command-line version of a web browser:
        it is just an HTTP client. 
        
        1) The basic syntax is "curl<some_url>:<some_port>". This will make 
    a GET request to the URL and port print the message response. 
        2) "curl" will default to using port 80 for http and port 443 for https
        3) You can specify the HTTP verb to use with the "-x" flag. 
    For example, "curl -X GET <some_url>" (though "-X GET" is redundant because
        "curl" defaults to making a GET request) 
        4) You can set "verbose mode" with the "-v" flag, which will then show
    additional information such as the headers passed back and forth (more on 
         this later). 
        
    To make a request on a linux machine type "curl localhost:5005" 
    
    However, we will receive a 404 error message in HTML format that says 
    that the server could not find the resource we requested. 
    
    It's time to add some routes!!!! 
    
                                 Routes in Flask
                                 
    In a Flask app, you define the URLs in your application using the 
    "app.route" decorator: 
        
        1) "app.route" is a decorator - place it on the line before the 
    declaration of a python function.
        2) "app.route" requires a string argument which is the path of the 
    URL (not including the base_url). 
        3) "app.route" takes an argument "methods" which should be a list of 
    strings containing  the names of valid HTTP methods. 
        4) When the URL + HTTP method combination is requested, Flask will 
    call the decorated function. 
    
    
    What is a Python decorator????? 
    
    1) A decorator is a function that takes another function as an input and
    returns a different function, then extends the behavior in some way. 
    2) The decorator must return a function which includes a call to the 
    original function plus the extended behavior. 
    3) The typical structure of a decorator is as follows: '''

'''
    
def my_decorator(some_func):
    def func_to_return():
         extend the behavior of some_fun by doing some processing before 
        it is called (optional) 
        
        do_something_before()
        
        # Call the original function: 
            
        some_func(*args, **kwargs)
        
        Extend the behavior of some_fun by doing some processing after 
        it is called (optional): 
        
        do_something_after()
    
    return func_to_return


''' 
''' Consider this test program as an example: '''

def print_dec(f): 
    def func_to_return(*args, **kwargs):
        print("args: {}; kwargs: {}".format(args,kwargs))
        val = f(*args, **kwargs)
        print("return: {}".format(val))
        return val
    return func_to_return

@print_dec
def foo(a):
    return a+1

result = foo(2)
print("Got the result: {}".format(result))

''' Note: Our print decorator gets executed automatically when we call "foo(2)"
'''


'''                            Routes with URL Parameters          

Flask makes it easy to create Routes (or URLs) with variable in the URL. 
Here are the basics: 
    
    1) We put the variable name in angled brackets (<>) within the app.route()
    decorator statement; for example "@app.route(/<year>)" for a variable, 
    "year"
    
    2) We make the variable a parameter to the decorated function and use it
    just like any other variable. '''
