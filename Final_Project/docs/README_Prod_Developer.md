###### README File Documentation for Developers ########

This file provides step-by-step instructions that an operator/developer needs
to follow in order to successfully deploy the system on a Kubernetes cluster.
In particular, step-by-step instructions on how to build, and run resources
such as services, deployments, and pvc's from YAML configuration files that
are needed to establish an environment that users who have access to these
resources will be able to use to interact with data through the API. Additionally,
sample commands, and corresponding output messages will be included to help
guide the developer in the process.

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



################ Commands Used to Build and Run Resources #################### 

1) To build and run the persistent volume claim, run the following command: 

"kubectl apply -f jcam989-prod-pvc.yml"

Output: "persistentvolumeclaim/jcam989-prod-pvc created"

2) To build and run the python debug deployment, run the following command: 

"kubectl apply -f deployment-python-debug.yml"

Output: "deployment.apps/py-debug-deployment created"

3) To build and run the redis deployment, run the following command: 

"kubectl apply -f jcam989-prod-redis-deployment.yml"

Output: "deployment.apps/jcam989-prod-redis created"

4) To build and run the flask service, run the following command: 

"kubectl apply -f jcam989-prod-flask-service.yml"

Output: "service/jcam989-prod-flask-service created"

5) To build and run the redis service, run the following command:

"kubectl apply -f jcam989-prod-redis-service.yml"

Output: "service/jcam989-prod-redis-service created"

6) To get the IP address for the redis service, (which must be hardcoded
into the "jcam989-prod-flask-deployment.yml" file before the flask deployment
is built and run), run the following command: 

"kubectl get services" 

Output: "

NAME                        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
app1                         NodePort    10.109.62.99     <none>        5000:31358/TCP   5d11h
jcam989-prod-flask-service   ClusterIP   10.106.77.199    <none>        5000/TCP   39s
jcam989-prod-redis-service   ClusterIP   10.108.190.203   <none>        6379/TCP   20s

"

7) Open the "jcam989-prod-flask-deployment.yml" file in edit mode and 
input the ClusterIP address for the "jcam989-prod-redis-service" into 
the "value" field for the "REDIS_IP" environment variable.

8) Repeat step 7) for the worker deployment configuration file in 
"jcam989-prod-worker-deployment.yml".

9) To build and run the flask deployment, run the following command: 

"kubectl apply -f jcam989-prod-flask-deployment.yml"

Output: "deployment.apps/jcam989-prod-flask created"

10) To build and run the worker deployment, run the following command: 

"kubectl apply -f jcam989-prod-worker-deployment.yml"

Output: "deployment.apps/jcam989-prod-worker created"

The system and all of its resources should now be deployed on the Kubernetes 
cluster; see "README_Test_User.md" for instructions on how to curl to the 
synchronous endpoints/routes in the Flask web API,  and examples of 
expected output from these requests. 
