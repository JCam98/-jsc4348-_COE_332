General Description of Tools in "homework6" subdirectory:

The "homework6" subdirectory contains eight files:

"deployment-python-debug.yml"
"Dockerfile"
"jcam98-test-flask-deployment.yml"
"jcam98-test-flask-service.yml"
"jcam98-test-pvc.yml"
"jcam98-test-redis-deployment.yml"
"jcam98-test-redis-service.yml"
"README.md"

and two directories, "config", and "web" which contain the following: 

"config" - "redis.conf"

"web"  - "app.py", "requirements.txt"

################ Commands Used to Build and Run Resources #################### 

1) To build and run the persistent volume claim, run the following command: 

"kubectl apply -f jcam98-test-pvc.yml"

Output: "persistentvolumeclaim/jcam98-test-pvc created"

2) To build and run the python debug deployment, run the following command: 

"kubectl apply -f deployment-python-debug.yml"

Output: "deployment.apps/py-debug-deployment created"

3) To build and run the redis deployment, run the following command: 

"kubectl apply -f jcam98-test-redis-deployment.yml"

Output: "deployment.apps/jcam98-test-redis created"

4) To build and run the flask service, run the following command: 

"kubectl apply -f jcam98-test-flask-service.yml"

Output: "service/jcam98-test-flask-service created"

5) To build and run the redis service, run the following command:

"kubectl apply -f jcam98-test-redis-service.yml"

Output: "service/jcam98-test-redis-service created"

6) To get the IP address for the redis service, (which must be hardcoded
into the "jcam98-test-flask-deployment.yml" file before the flask deployment
is built and run), run the following command: 

"kubectl get services" 

Output: "

NAME                        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
jcam98-test-flask-service   ClusterIP   10.99.223.95    <none>        5000/TCP   3m52s
jcam98-test-redis-service   ClusterIP   10.97.112.162   <none>        6379/TCP   2m40s

"
7) To build and run the flask deployment, run the following command: 

"kubectl apply -f jcam98-test-flask-deployment.yml"

Output: "deployment.apps/jcam98-test-flask created"

#### Command Used to Demonstrate Curl to Flask API in Kubernetes Cluster #####

1) Return the name of the "py-debug-deployment" replica that is running in the 
namespace using the command: 

"kubectl get pods -o wide" 

Output: "

NAME                                   READY   STATUS    RESTARTS   AGE     IP             NODE                         NOMINATED NODE   READINESS GATES
jcam98-test-flask-86694cf45c-n2tj5     1/1     Running   0          4m42s   10.244.3.14    c01                          <none>           <none>
jcam98-test-flask-86694cf45c-n4d77     1/1     Running   0          4m42s   10.244.5.129   c04                          <none>           <none>
jcam98-test-redis-7fd9c55cf6-56kn5     1/1     Running   0          14m     10.244.15.70   c03                          <none>           <none>
py-debug-deployment-5cc8cdd65f-wk2cq   1/1     Running   0          16m     10.244.10.78   c009.rodeo.tacc.utexas.edu   <none>           <none>

"

2) Exec into the py-debug-deployment replica's container, and attach an interactive
shell to the "/bin/bash" directory by running the following command: 

"kubectl exec -it py-debug-deployment-5cc8cdd65f-wk2cq -- /bin/bash" 

Output: "root@py-debug-deployment-5cc8cdd65f-wk2cq:/#" 

3) Use the "pip" package installation manager to install redis module: 

"pip install redis"

Output: "

Collecting redis
  Downloading redis-3.5.3-py2.py3-none-any.whl (72 kB)
     |████████████████████████████████| 72 kB 931 kB/s 
Installing collected packages: redis
Successfully installed redis-3.5.3
WARNING: You are using pip version 21.0.1; however, version 21.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.

" 

4) Run a "python 3" interpreter in the container by running the following command: 

"python3"

Output: "

Python 3.9.2 (default, Feb 19 2021, 17:11:58) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

"

5) Import the "redis' module by running the following command: 

"import redis" 

6) Create a redis client object by running the "StrictRedis()" method using the 
redis service IP address as the host name: 

"rd=rd.redis.StrictRedis(host='10.97.112.162', port=6379, db=0)"

7) Invoke "hget()" method to return a UUID query parameter for an animal, 
whose key is defined as "animal1". This query parameter will be read into the 
flask API in "app.py" when a curl request is made to the route: "/animals/creature/UUID":

"rd.hget("animal1","UUID")"

Output: b'f9bea5e0-80e5-4935-9042-3cbba0d99f3a'

8) Copy the binary-to-string decoded return value

9) Exit the python3 interpreter and navigate back to the root directory of 
the container by running: 

"exit" 

10) Run a curl request to the route, "/animals/creature/UUID" through the 
flask service IP address making sure to paste the UUID query parameter that was 
copied in step 8. This returns a json-formatted dictionary of animal characteristics
of "animal1", whose UUID parameter was read into the route: 

"curl 10.99.223.95:5000/animals/creature/UUID?UUID=f9bea5e0-80e5-4935-9042-3cbba0d99f3a"

Output: 

"

{
  "animal": [
    "head:lion", 
    "body:jackal-kite", 
    "arms:10", 
    "legs:6", 
    "tails:16", 
    "UUID:f9bea5e0-80e5-4935-9042-3cbba0d99f3a", 
    "timestamp:2021-04-29 04:54:44.184481"
  ]
}

"



 