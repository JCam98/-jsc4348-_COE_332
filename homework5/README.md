General Description of Tools in "homework5" subdirectory:

The "homework5" subdirectory contains three files: 

  1) "pod-basic.yml"
  2) "deployment-basic.yml"
  3) README.md
  
//Description of "pod-basic.yml" file and Associated Run Commands and Output//

The "pod-basic.yml" file is a YAML configuration file that contains the 
architecture of the pod, "hello", that when configured, and run, returns the message 
"Hello, Justin Campbell" to the console. 

To configure the pod and return the message to the console the following steps 
must be taken: 

   1) Run the command "kubectl apply -f pod-basic.yml" on the command line
   
   Output: "pod/hello created"
   
   2) Run the command "kubectl logs hello" on the command line
   
   Output: "Hello, Justin Campbell" 
   

//Description of "deployment-basic.yml" file and Associated Run Commands and Output //

The "deployment-basic.yml" is a YAML configuration file that contains the 
architecture of the deployment, "hello", that, when configured, and run, 
returns the message "Hello, Justin Campbell from "<pod_ip_address>"". Note: 
The deployment runs three pod replicas with private IP addresses whose values
are returned in this message. 


To configure the deployment and return the message specific to the deployment
replica/pod (of which there are 3), the following steps must be taken: 

    1) Run the command "kubectl apply -f deployment-basic.yml" on the command line
    
    Output: "deployment.apps/hello-deployment created"
    
    2) Run the command "kubectl get pods -o wide" to output each of the pod
    replicas in the deployment and their associated private IP addressed
    
    Output (Sample):
    
    NAME                                READY   STATUS    RESTARTS   AGE   IP             NODE   NOMINATED NODE   READINESS GATES
hello                               1/1     Running   0          10m   10.244.12.85   c12    <none>           <none>
hello-deployment-659c58bfd5-fpr84   1/1     Running   0          42s   10.244.12.88   c12    <none>           <none>
hello-deployment-659c58bfd5-qn2lk   1/1     Running   0          42s   10.244.3.73    c01    <none>           <none>
hello-deployment-659c58bfd5-qx5xz   1/1     Running   0          42s   10.244.13.76   c11    <none>           <none>

    
    
    Output (Generic):
    
    NAME                                                                     READY   STATUS    RESTARTS   AGE   IP                           NODE   NOMINATED NODE   READINESS GATES
hello                                                                        1/1     Running   0          10m   <some_rand_gen_private_IP>   c12    <none>           <none>
hello-deployment-<rand_gen_10_alphanumeric_ID>-<rand_gen_5_alphanumeric_ID>  1/1     Running   0          42s   <some_rand_gen_private_IP>   c12    <none>           <none>
hello-deployment-<rand_gen_10_alphanumeric_ID>-<rand_gen_5_alphanumeric_ID>  1/1     Running   0          42s   <some_rand_gen_private_IP>    c01    <none>           <none>
hello-deployment-<rand_gen_10_alphanumeric_ID>-<rand_gen_5_alphanumeric_ID>  1/1     Running   0          42s   <some_rand_gen_private_IP>   c11    <none>           <none>

    
    3) Run the command "kubectl logs <deployment_pod_name>" on the command line
    
    Output (Sample): 
    
    a) "kubectl logs hello-deployment-659c58bfd5-fpr84"
    
        Output: Hello, Justin Campbell from IP 10.244.12.88
    
    b) "kubectl logs hello-deployment-659c58bfd5-qn2lk"
    
        Output: Hello, Justin Campbell from IP 10.244.3.73
        
    c) "kubectl logs hello-deployment-659c58bfd5-qx5xz"
    
        Output: Hello, Justin Campbell from IP 10.244.13.76
        
    Output (Generic):
    
    "kubectl logs <deployment_pod_name>"
    
        Output: Hello, Justin Campbell from IP <some_rand_gen_private_IP>
            
    
    