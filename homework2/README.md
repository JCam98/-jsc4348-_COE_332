General Description of Tools in "homework2" subdirectory: 

The python scripts in this homework subdirectory are used to 
build on the functionality of the programs in the "homework1" 
subdirectory, while adding a couple of new features such
as the incoporation of random species breeding, and application
of simple unit testing within the scope of these new features.
This subdirectory is also comprised of a Dockerfile that provides
the user with a list of commands that can be used to run the code
inside a containerized environment that is both machine independent 
and mountable. 


The "homework2" subdirectory is composed of five files: 

1) generate_animals.py

The contents of the "generate_animals.py" script remain unchanged 
relative to that of the file located with the "homework1" subdirectory. 

2) read_animals.py 

New features were added to the "read_animals.py" script. In particular, 
the script now incorporates an algorithm that uses the "random" module 
to randomly choose two animals of unique species, breed them,
and output the physical characteristics of both the parents 
and the offspring to the terminal. Two functions were defined in the script
for the purpose of simple unit testing using python's "unittest" framework. 

3) test_read_animals.py

The two functions defined within the scope of the script "read_animals.py"
are imported into the script "test_read_animals.py", and used to unit test
two parts of the algorithm associated with the new breeding feature of the
"read_animals.py" program when the former is executed. In particular, the 
"assertEqual()", and "assertRaises()" functions are invoked to ensure that
the algorithm produces expected numerical results, and that errors are raised
when input arguments are of an incompatible data type. 

4) Dockerfile

The dockerfile contains a list of commands that must be run in order to build 
the python scripts (with exception to "test_read_animals.py") within a container
such that they are executable. 

5) README.md 

Instructions on how to download and run the scripts directly 

To run each of the three scripts on a local machine, the user can 
use git command line utilities to pull the files from this subdirectory
onto their local machine. This can be accomplished through two steps: 

1) Open up a terminal and navigate to desired working directory on
local machine. Once at the desired directory, run "git init" to initialize
an empty repository at this location. 

2) The five files from this "homework2" subdirectory can be copied and
transferred to the working directory by running the following command: 

"git pull https://github.com/JCam98/-jsc4348-_COE_332.git"

The scripts "generate_animals.py", and "read_animals.py" can be executed
by running the following commands on the terminal "python3 generate_animals.py <filename.json>", 
and "python3 read_animals.py <filename.json>" respectively, and where "filename" is 
some string chosen by the user. 

The unit testing script, "test_read_animals.py", can be executed by running
"python3 test_read_animals.py". 

Important: Make sure that the "python3" interpreter and its dependencies
are installed on the local machine. 

Instructions on how to build an image with the Dockerfile provided

After executing the directives in the Dockerfile in this subdirectory, the 
image can be built using the following command:

"docker build -t <dockerhubusername>/homework_2:1.0 ."
  
(where "-t" is a flag that allows for the tagging of the 
image with a descriptive name <homework_2>, and an optional 
release number <1.0>, <dockerhubusername> is the 
user's dockerhub username, and the trailing dot, "." indicates 
the location, (current directory), of the Dockerfile.

Instructions on how to run the scripts inside a container

After an image has been built using the aforementioned commands
, the following command can be executed in the terminal, and 
local working directory of the built image to start a shell inside the image, 
and allow for the user to execute the python scripts "generate_animals.py",
and "read_animals.py" within the container (instance of image): 

"docker run --rm -it username/homework_2:1.0 /bin/bash"

(where "username" is the dockerhub username of the user).

After executing this command, the user will be inside the root directory
of the container where they can check that the two scripts are located
within the directory by running "ls /code" 

The user can then enter the command "cd /home" to change to the home
working directory of the container. 

Here, the script "generate_animals.py" can be executed by running 
"generate_animals.py <filename.json>", where "filename.json" is the output
file of the program containing the key value pairs of the animals. 

The second script, "read_animals.py", can then be executed by running 
"read_animals.py <filename.json>". The output will appear on the terminal.

Instructions on how to run the unit test(s)

The unit tests in the script "test_read_animals.py" can be evaluated by 
running "python3 test_read_animals.py" in the working directory
containing the three python scripts. 

Note: The script "test_read_animals.py" is 
not containerized. Make sure that the "python3" interpreter and its dependencies
have been installed on the local machine. 

