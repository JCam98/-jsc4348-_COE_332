''' Property of Justin Campbell; UT eID: jsc4348
    Purpose of Use: COE 332: Software Engineering and Design
    Script File Name: api.py
    
    
    Description: This module contains the flask web API definition, 
    along with the synchronous endpoints/routes that are used to load, create,
    update, delete, and retrieve temperature data from a redis database. '''

# Import modules:    
    
from __future__ import print_function #Enables compatibility of python2 print statements to python3 syntax  
from flask import Flask, request, send_file
import json, uuid
from jobs import add_job, rd_jobs, rd_temp, rd_im, q

app = Flask(__name__) # Instantiate Flask Web API                                                                                                                                                         

''' Define function that reads temperature data points into database from json file. 
The format for making a curl request to this route takes on the following form: 
    
    "curl Flask_Service_IP:5000/read_temp_data" '''

@app.route('/read_temp_data', methods=['GET'])    
def read_data():
    
    ''' Read contents of json file into json datastructure: '''

    with open('Input_Data/Global_Temp_Data.json','r') as f: 
            temp_data = json.load(f)
             
        
    # Set the data to a redis database: 
     
    i = 0    
        
    for temp in temp_data:
        
        # Invoke "uuid4()" method to assign random unique identifier to temperature
        
        UUID = str(uuid.uuid4())
        
        # Assign keyname to temperature:
        
        temp_key = i
        
        rd_temp.hmset(temp_key, {"dt": temp["dt"], "GALT (Celsius)": \
                            temp["GALT (Celsius)"], "GMAXLT (Celsius)": \
                                temp["GMAXLT (Celsius)"], "GMINLT(Celsius)": \
                                    temp["GMINLT(Celsius)"], "UUID": \
                                        UUID})
            
        i = i + 1    
    
    
    return_status = "Data Loaded Successfully"
    
    return return_status

temp_num = rd_temp.dbsize() # Get the number of temperature dictionaries in database   

''' Define endpoint that updates one or more temperature values 
for a particular date. The only requirements for the query parameters
are that the user must pass in the UUID for the appropriate data and at least 
one temperature value. The format for making a curl request to this route takes
on the following form: 
    
    "curl Flask_Service_IP:5000/update_data?UUID=<some_valid_UUID>&Global_Average_Land_Temp
    =<updated_avg_temp_value&Global_Maximum_Land_Temp=<updated_max_temp_value>'&Global_Minimum_Land_Temp=
    <updated_min_temp_value>" '''
    
''' NOTE: THE USER SHOULD KEEP IN MIND THAT THE TEMPERATURE VALUES ARE 
REPORTED IN DEGREES CELSIUS. THUS, TO AVOID ANY ANOMALIES IN THE TIME-SERIES
TEMPERATURE READINGS, MAKE SURE TO MAKE NECESSARY CONVERSIONS TO READ IN 
TEMPERATURE VALUES IN DEGREES CELSIUS'''
    
@app.route('/update_data', methods=['GET'])
def update_data_api():
    
    temp_num = rd_temp.dbsize() # Get the number of temperature dictionaries in database 
    
    # Query the UUID for date with historical temperature value(s) to be updated: 
        
    UUID = request.args.get('UUID')
    
     # Get the temp_key from the database using UUID: 
        
    for i in range(0, temp_num ):
        
        UUID_rd = rd_temp.hget(i, "UUID")# Get the UUID from database
        
        ''' If UUID returned from database equals UUID query value, define
        "temp_key" value and break '''
        
        if (UUID_rd == UUID):
            
            # Assign keyname to temperature:
        
            temp_key = i
            
            break
    
    # Query the Global Average Land Temperature (GALT) in Celsius
    
    GALT_str = request.args.get('Global_Average_Land_Temp')
    
    # If "GALT_str" query value is defined update value in database:
    
    if (GALT_str != None):
        
        GALT = float(GALT_str)
        rd_temp.hset(temp_key, "GALT (Celsius)", GALT)
    
    # Query the Global Maximum Land Temperature (GMAXLT) in Celsius
    
    GMAXLT_str = request.args.get('Global_Maximum_Land_Temp')
    
     # If "GMAXLT_str" query value is defined update value in database:
        
    if (GMAXLT_str != None):
        
        GMAXLT = float(GMAXLT_str)
        rd_temp.hset(temp_key, "GMAXLT (Celsius)", GMAXLT)
    
    
    # Query the Global Minimum Land Temperature (GMINLT) in Celsius
    
    GMINLT_str = request.args.get('Global_Minimum_Land_Temp')
    
     # If "GMINLT_str" query value is defined update value in database:    
        
    if (GMINLT_str!= None):
        
        GMINLT = float(GMINLT_str)
        rd_temp.hset(temp_key, "GMINLT(Celsius)", GMINLT)

        
    return_status = "Data Updated Successfully"
    
    return return_status


''' Define endpoint that creates new temperature data points for a particular,
and newly created, date and stores them in a database. Note: The date must be 
of a value that is not currently stored in database and take on the format: "MM/DD/YYYY".
The user must set a value for all three temperature fields. The format
for making a curl request to this route takes on the following form: 
    
    "curl Flask_Service_IP:5000/create_data?date=<some_valid_date>&Global_Average_Land_Temp=
    <new_avg_temp_value>&Global_Maximum_Land_Temp=<new_max_temp_value>'&
    Global_Minimum_Land_Temp= <new_min_temp_value>" '''

@app.route('/create_data', methods=['GET'])
def create_data_api():
    
    temp_num = rd_temp.dbsize() # Get the number of temperature dictionaries in database 
    
    # Query the data for historical temperature value(s) to be created and stored: 
        
    date_in = request.args.get('date')
    
    # Query the Global Average Land Temperature (GALT) in Celsius
    
    GALT_str = request.args.get('Global_Average_Land_Temp')
    GALT = float(GALT_str)
    
    # Query the Global Maximum Land Temperature (GMAXLT) in Celsius
    
    GMAXLT_str = request.args.get('Global_Maximum_Land_Temp')
    GMAXLT = float(GMAXLT_str)
    
    # Query the Global Minimum Land Temperature (GMINLT) in Celsius
    
    GMINLT_str = request.args.get('Global_Minimum_Land_Temp')
    GMINLT = float(GMINLT_str)
    
    create_cond = True # Initialize data creation condition to true  
    
    for i in range(0,temp_num):
        
        
         ''' Return date parameters for "temp_key" from database: '''
         
         temp_key = i # Assign keyname to temperature
         date_db = rd_temp.hget(temp_key, "dt") # Return date for "temp_key"
         
         ''' Conditional to compare input date of creation to date in database: '''
        
         if (date_in == date_db):
                 
                 create_cond = False
                 break
         
         
    if (create_cond == True):
        
        temp_key = temp_num + 1
        
        # Set value of date "date_in" in database: 
            
        rd_temp.hset(temp_key, "dt", date_in)
  
        # Set value of GALT in database:
        
        rd_temp.hset(temp_key, "GALT (Celsius)", GALT)
            
        # Set value of GMAXLT in database:
            
        rd_temp.hset(temp_key, "GMAXLT (Celsius)", GMAXLT)
            
        # Set value of GMINLT in database:    
            
        rd_temp.hset(temp_key, "GMINLT(Celsius)", GMINLT)
        
        # Invoke "uuid4()" method to assign random unique identifier to temperature
        
        UUID = str(uuid.uuid4())
        
        rd_temp.hset(temp_key, "UUID", UUID)
            
        return_status = "Data Created and Stored Successfully"
    
    return return_status


''' Define endpoint that returns all fields values between a start and end date
to the console.  Note: The dates must take on the format: "MM/DD/YYYY".
The formatfor making a curl request to this route takes on the following form: 
    
    "curl Flask_Service_IP:5000/retrieve_data?date_lower_bound=<some_valid_date>&
    date_upper_bound=<some_valid_date> '''

   
@app.route('/retrieve_data', methods=['GET'])
def retrieve_data_api():
    
    temp_num = rd_temp.dbsize() # Get the number of temperature dictionaries in database 
    
    # Query the dates for historical temperature value(s) to be created and stored: 
        
    date_low = request.args.get('date_lower_bound')
    date_up = request.args.get('date_upper_bound')
    
    
    ''' Extract date parameters from lower bound: '''
    
    year_low = int(date_low[6:10])
    month_low = int(date_low[0:2])
    day_low = int(date_low[3:5])
    
    ''' Extract date parameters from upper bound: '''
    
    year_up = int(date_up[6:10])
    month_up = int(date_up[0:2])
    day_up = int(date_up[3:5])
    
    
    temp_output = [] # Initialize list to store output data
    
    # Use a for loop to return field values between start and end date:
        
    for i in range(0, temp_num):
        
        temp_key = i # Assign keyname to temperature
        
        ''' Extract the date parameters from the database: '''
        
        date_db = rd_temp.hget(temp_key, "dt")
        year_db = int(date_db[6:10])
        month_db = int(date_db[0:2])
        day_db = int(date_db[3:5])
        
        out_cond = True # Initialize output condition to true 
        
        ''' Use while loop with nested if statements to check if date from 
        database falls within range: '''
            
        while (out_cond == True):
            
           if (year_db > year_up or year_db < year_low):
               
               out_cond = False 
               break
           
           elif (year_db == year_up and month_db > month_up):
               
               out_cond = False 
               break
           
           elif (year_db == year_low and month_db < month_low):
               
               out_cond = False 
               break 
           
           elif (year_db == year_up and month_db ==  month_up and day_db > day_up):
               
               out_cond = False 
               break 
           
           elif (year_db == year_low and month_db ==  month_low and day_db < day_low):
               
               out_cond = False 
               break  
            
           break
       
           ''' Append field values from database to output list if the condition 
           "out_cond" is true: '''
            
        if (out_cond == True):
            
             temp_output.append(rd_temp.hgetall(temp_key))
    
    # Store data in json formatted dictionary:
    
    temp_dict = {"Earth Surface Temperature Data": temp_output}
    
    return temp_dict

''' Define endpoint that deletes data between an initial and final date. Note: 
The dates must take on the format: "MM/DD/YYYY". The format for making a curl 
request to this route takes on the following form: 
    
    "curl Flask_Service_IP:5000/delete_data?date_lower_bound=<some_valid_date>&
    date_upper_bound=<some_valid_date> "'''
 

@app.route('/delete_data', methods=['GET'])
def delete_data_api():
    
    temp_num = rd_temp.dbsize() # Get the number of temperature dictionaries in database 
    
    # Query the date bounds for historical temperature value(s) to be deleted: 
        
    date_low = request.args.get('date_lower_bound')
    date_up = request.args.get('date_upper_bound')
    
    
    ''' Extract date parameters from lower bound: '''
    
    year_low = int(date_low[6:10])
    month_low = int(date_low[0:2])
    day_low = int(date_low[3:5])
    
    ''' Extract date parameters from upper bound: '''
    
    year_up = int(date_up[6:10])
    month_up = int(date_up[0:2])
    day_up = int(date_up[3:5])
    
    
    temp_store = [] # Initialize list to store data outside range of deletion:
    
    # Use a for loop to return field values between start and end date:
        
    for i in range(0, temp_num):
        
        temp_key = i # Assign keyname to temperature
        
        ''' Extract the date parameters from the database: '''
        
        date_db = rd_temp.hget(temp_key, "dt")
        year_db = int(date_db[6:10])
        month_db = int(date_db[0:2])
        day_db = int(date_db[3:5])
        
        sto_cond = True # Initialize storage condition to true 
        
        ''' Use while loop with nested if statements to check if date from 
        database falls within range: '''
            
        while (sto_cond == True):
            
           if (year_db < year_up and year_db > year_low):
               
               sto_cond = False 
               break
           
           elif (year_db == year_up and month_db < month_up and month_db > month_low):
               
               sto_cond = False 
               break
           
           elif (year_db == year_low and month_db > month_low and month_db < month_up):
               
               sto_cond = False 
               break 
           
           elif (year_db == year_up and month_db ==  month_up and day_db < day_up and day_db > day_low):
               
               sto_cond = False 
               break 
           
           elif (year_db == year_low and month_db ==  month_low and day_db > day_low and day_db < day_up):
               
               sto_cond = False 
               break  
           
           break  
       
        ''' Append field values from database to data storage list if the condition 
           "sto_cond" is true: '''
            
        if (sto_cond == True):
            
              temp_store.append(rd_temp.hgetall(temp_key))
         
    temp_store_num = len(temp_store)
        
    rd_temp.flushall() # Clear all elements from the redis database                                                                                                                                                                             

    ''' Store new data structure in redis database: '''

    for i in range(0,temp_store_num):

        temp_key = i # Assign keyname to temperature                                             

        ''' Set data points that lie outside range of deletion to database: '''

        rd_temp.hmset(temp_key, {"dt": temp_store[i]["dt"], "GALT (Celsius)": \
                            temp_store[i]["GALT (Celsius)"], "GMAXLT (Celsius)": \
                                temp_store[i]["GMAXLT (Celsius)"], "GMINLT(Celsius)": \
                                    temp_store[i]["GMINLT(Celsius)"], "UUID": \
                                        temp_store[i]["UUID"]})


    return_status = "Temperature Data Deleted Successfully"
    
    return return_status


# Define endpoint that sets jobs in redis database:

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(add_job(job['start'], job['end']))


''' Define endpoint that downloads analysis plot to local file system. The format
for making a curl request to this route takes on the following form: 
    
    "curl Flask_Service_IP:5000/download_plot<jobid>" '''
    
@app.route('/download_plot/<jobid>', methods=['GET'])
def download(jobid):                                                                                        
        path = f'/app/{jobid}.png'                                                               
        with open(path, 'wb') as f:                                                                        
            f.write(rd_im.hget(f'job.{jobid}', 'image'))                                             
        return send_file(path, mimetype='image/png', as_attachment=True)                                       
                                                                                                           
              

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
