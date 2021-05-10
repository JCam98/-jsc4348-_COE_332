###### README File Documentation for Users ########

This file provides step-by-step instructions that a user needs to follow in order
to successfully interact with the Flask API contained within the "api.py" 
module. Throughout the instructions, the user will be provided with a list
of synchronous endpoints in the API that perform load, create, update, delete, 
and retrieve operations on a temperature dataset, "Global_Temp_Data.json", 
that is used for the analysis. Example responses that the user should receive
on their console when successful curl routes are performed to each of these
endpoints will then be listed. 

General Description of Tools in "production-final-project" subdirectory:

The "production-final-project" subdirectory contains  files:

"deployment-python-debug.yml"
"Dockerfile"
"jcam989-prod-flask-deployment.yml"
"jcam98-prod-flask-service.yml"
"jcam98-prod-pvc.yml"
"jcam98-prod-redis-deployment.yml"
"jcam98-prod-redis-service.yml"
"jcam98-prod-worker-deployment.yml"


The "production-final-project" subdirectory contains directories:

1) "config":
    
   The "config" subdirectory contains: 
    
    1) "redis.conf"


2) "source_files":

   The "source_files" subdirectory contains: 
   
   1) "api.py"
   2) "jobs.py"
   3) "worker.py"
   4) "requirements.txt"
   5) "Input_Data":
   
      The "Input_Data" subdirectory contains: 
      
      1) "Global_Temp_Data.json"


3) "docs":

   The "docs" subdirectory contains: 

   1) "README_prod_user.md"
   2) "README_prod_developer.md"



################ Commands Used to Curl to Flask API Endpoints #################### 



1) Return the name of the "py-debug-deployment" replica that is running in the 
namespace using the command: 

"kubectl get pods -o wide" 

Output: "

NAME                                   READY   STATUS    RESTARTS   AGE     IP              NODE                         NOMINATED NODE   READINESS GATES
jcam989-test-flask-fd984cf5-br8b5      1/1     Running   0          5m18s   10.244.15.198   c03                          <none>           <none>
jcam989-test-redis-756875fd64-s4mnl    1/1     Running   0          14m     10.244.13.220   c11                          <none>           <none>
jcam989-test-worker-9d4cb8bb6-dc4xz    1/1     Running   0          4m59s   10.244.3.72     c01                          <none>           <none>
py-debug-deployment-5cc8cdd65f-4t8lp   1/1     Running   0          14m     10.244.10.127   c009.rodeo.tacc.utexas.edu   <none>           <none>

"

2) Exec into the py-debug-deployment replica's container, and attach an interactive
shell to the "/bin/bash" directory by running the following command: 

"kubectl exec -it py-debug-deployment-5cc8cdd65f-4t8lp -- /bin/bash" 

Output: "root@py-debug-deployment-5cc8cdd65f-4t8lp:/#"

3) Use the "pip" package installation manager to install redis module: 

"pip install redis"

Output: "

Collecting redis
  Downloading redis-3.5.3-py2.py3-none-any.whl (72 kB)
     |████████████████████████████████| 72 kB 1.5 MB/s 
Installing collected packages: redis
Successfully installed redis-3.5.3
WARNING: You are using pip version 21.0.1; however, version 21.1.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.

" 

4) Before any operations on the data can be performed, it must be loaded into
a redis database. This can be accomplished by curling to the route "/read_temp_data"
using the following command: 

    "curl Flask_Service_IP:5000/read_temp_data"
    
Output: "Data Loaded Successfully"


The second route defined in the "api.py" is used to update one or more 
temperature field values in the database for a particular date. Before being
able to curl to this route, the user must obtain a  UUID value from the 
redis database associated with the date whose temperature values are to be 
updated. This can be accomplished by entering the python3 terminal. 

5) Import the "redis" module by running the following command: 

"import redis"

6) Instantiate a redis database for the temperature data by running the 
"StrictRedis()" method using the redis service IP address as the host name: 

"rd_temp=redis.StrictRedis(host='10.108.190.203', port=6379, db=1, decode_responses = True)"

Note: The hostname must be equal to that of the redis service, and the 
database number, "db" must equal that of the database in "jobs.py" used
to store the temperature data, namely, it must take on a value of "1".

7) Run the "hget(key, hash)" method to return a UUID for the desired date (
where "key" is equal to some integer value, where key values are assigned to dates
in ascending order, and where "hash"  = "UUID"):

   "rd_temp.hget(1,"UUID")"
   
Output: '584093cb-5689-49fb-b9bb-b1fff6db6d92'

8) Exit the python3 interpreter by running "exit()"

9) Curl to the route "/update_data" by running the following command: 


   "curl Flask_Service_IP:5000/update_data?UUID=<some_valid_UUID>&Global_Average_Land_Temp                    
    =<updated_avg_temp_value&Global_Maximum_Land_Temp=<updated_max_temp_value>'&Global_Minimum_Land_Temp=      
    <updated_min_temp_value>"
    
Sample Command: "curl "10.106.77.199:5000/update_data?UUID=584093cb-5689-49fb-b9bb-b1fff6db6d92&Global_Average_Land_Temp=10.0&Global_Maximum_Land_Temp=20&Global_Minimum_Land_Temp=0""

Sample Output: "Data Updated Successfully"

The third route defined in "api.py" is used to create new temperature field
values for a particular, and newly created date, and stores them in a database.
The date must be a value that is not currently stored in database and take on
the format: "MM/DD/YYYY". The user must set a value for all three temperature 
fields. 

10) Curl to the route, "/create_data" by running the following command:                                          
                                                                                                               
    "curl Flask_Service_IP:5000/create_data?date=<some_valid_date>&Global_Average_Land_Temp=                   
    <new_avg_temp_value>&Global_Maximum_Land_Temp=<new_max_temp_value>'&                                       
    Global_Minimum_Land_Temp= <new_min_temp_value>"
    
Sample Command:  "curl "10.106.77.199:5000/create_data?date=01/01/2020&Global_Average_Land_Temp=10.0&Global_Maximum_Land_Temp=20&Global_Minimum_Land_Temp=0""

Sample Output: "Data Created and Stored Successfully"



The fourth route defined in "api.py" is used to return all temperature field
values between a start and end date to the console. Now, due to the large 
amount of data stored in the database, the database will need to be flushed
of its content before a curl request can be made to this route. 


11) This can be accomplished by pulling up the python3 interpreter, importing redis, 
instantiating the "rd_temp" redis object as done above, and then by running the 
following command: 

    "rd_temp.flushall()"
    
Output: "True"

Then, the user must exit the interpreter, return to the root directory of the 
container, and curl to the "/read_temp_data" route to re-populate the database
as executed previously. 

    

12) Curl to the route, "/retrieve_data" by running the following command:                              
                                                                                                               
    "curl Flask_Service_IP:5000/retrieve_data?date_lower_bound=<some_valid_date>&                              
    date_upper_bound=<some_valid_date>"
    
    Note: The dates must take 
    on the format: "MM/DD/YYYY".                                        

    
Sample Command: "curl "10.106.77.199:5000/retrieve_data?date_lower_bound=01/01/2000&date_lower_bound=01/01/2000&date_upper_bound=03/01/2000""

Sample Output: 

"
{
  "Earth Surface Temperature Data": [
    {
      "GALT (Celsius)": "2.95", 
      "GMAXLT (Celsius)": "8.349", 
      "GMINLT(Celsius)": "-2.322", 
      "UUID": "9b24d9e3-df45-45b0-aeff-935b98b09902", 
      "dt": "01/01/2000"
    }, 
    {
      "GALT (Celsius)": "4.184", 
      "GMAXLT (Celsius)": "9.863", 
      "GMINLT(Celsius)": "-1.371", 
      "UUID": "165fecb0-f441-42a2-92cb-d70735e74f30", 
      "dt": "02/01/2000"
    }, 
    {
      "GALT (Celsius)": "6.219", 
      "GMAXLT (Celsius)": "12.205", 
      "GMINLT(Celsius)": "0.376", 
      "UUID": "996b6062-9ff7-44c7-8b7b-88be64662fbd", 
      "dt": "03/01/2000"
    }
  ]
}

"

The fifth route defined in the "api.py" module is used to delete 
data between an initial and final date. Note: The dates must take on the 
format: "MM/DD/YYYY".                                                             
                                                                                                               
13) Curl to the route "/delete_data" by running the following command: 

    "curl Flask_Service_IP:5000/delete_data?date_lower_bound=<some_valid_date>&                                
    date_upper_bound=<some_valid_date> "

Sample Command: "curl "10.106.77.199:5000/delete_data?date_lower_bound=01/01/2000&date_lower_bound=01/01/2000&date_upper_bound=03/01/2000""

Sample Output: "Temperature Data Deleted Successfully"


The sixth route defined in the "api.py" module is used to set jobs to the 
jobs redis database.

14) Curl to the "/jobs" route to set a job by running the following command: 

   "curl -X POST -H "content-type: application/json" -d '{"start": "<start_date>", "end": "<end_date>"}' Flask_Service_IP:5000/jobs"
   
Sample Command: "curl -X POST -H "content-type: application/json" -d '{"start": "01/01/2000", "end": "01/01/2001"}' 10.106.77.199:5000/jobs"

Sample Output: "{"id": "eb130e82-4711-46b1-b9e3-df667aab9ae7", "status": "submitted", "start": "01/01/2000", "end": "01/01/2001"}"

The seventh, and final route defined in the "api.py" module is used to download
an analysis plot generated in the "worker.py" module to the user's local file 
system. 

15) Curl to the "/download_plot" route by running the following command: 

   "curl Flask_Service_IP:5000/download_plot<jobid> > <output_image_name.png>"
   
Sample Command: "curl 10.106.77.199:5000/download_plot/1b194db2-954f-4a9a-9dd6-f3392e64e610 > image.png"

Sample Output: 

 % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 95543  100 95543    0     0  5831k      0 --:--:-- --:--:-- --:--:-- 6220k

In order for the user to be able to view the image, it must first be copied
and transferred from the container into the isp02 machine file system. 

16) Run the following command to create a copy of the image inside the 
container and to transfer that image from the container to the file system
in the isp02 machine: 

   "scp <output_image_name.png> username@hostname:/path_to_desired/directory"
   
Sample Command: "scp image.png jcam98@isp02.tacc.utexas.edu:~/"

"jcam98@isp02.tacc.utexas.edu's password: "

Sample Output: "image.png           100%   93KB  12.2MB/s   00:00  "

The last step is for the user to create a copy of the image inside the 
directory in this remote environment and to transfer that copy from the 
current directory to the file system in the user's local machine.. 

17) Run the  following command inside a terminal in the local machine 
to create a copy of the image inside the directory in the remote environment 
and to transfer that copy from the current directory to the file system into
the local machine:

   "scp username@hostname:/path_to_desired_directory/<output_image_name.png> ."
   
   
Sample Command: "scp jcam98@isp02.tacc.utexas.edu:~/image.png ."

"jcam98@isp02.tacc.utexas.edu's password:"

Sample Output: "" image.png                  100%   93KB 385.7KB/s   00:00 "

Note: In this example the image, "image.png" was copied from the remote 
host, "isp02@tacc.utexas.edu" to the home directory in the user's local machine.
This command was run in the home directory on a terminal in the user's 
local machine. '

18) Navigate to the appropriate directory and open the image using an 
image viewer application. The author elected to use "Preview" on his 
Mac OS. 

An output image is provided in the "docs" folder in the repository.

